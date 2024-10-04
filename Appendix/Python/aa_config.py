"""
 ____    ____       ______  _____  ____   _  ______  ____  ______     _____ __    _
|    \  |    \     |   ___|/     \|    \ | ||   ___||    ||   ___|   |     |\ \  //
|     \ |     \    |   |__ |     ||     \| ||   ___||    ||   |  | _ |    _| \ \// 
|__|\__\|__|\__\___|______|\_____/|__/\____||___|   |____||______||_||___|   /__/  
               |___|                                                               
"""

"""
This scipt configures all security software installed and configuered previously, or install them if they are not already installed
"""

import os
import subprocess

# Function to execute shell commands
def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Erfolgreich ausgeführt: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Ausführung von {command}: {e}")

# configure UFW
def configure_ufw():
    run_command("sudo ufw default deny incoming")
    run_command("sudo ufw default allow outgoing")
    run_command("sudo ufw allow 22/tcp")  # SSH
    run_command("sudo ufw allow 389/tcp") # LDAP
    run_command("sudo ufw allow 636/tcp") # LDAPS
    run_command("sudo ufw allow 80/tcp")  # HTTP (Snort/Suricata)
    run_command("sudo ufw allow 443/tcp") # HTTPS (Snort/Suricata)
    run_command("sudo ufw allow 3310/tcp") # ClamAV
    run_command("sudo ufw allow 55000/tcp") # Wazuh-Agent
    run_command("sudo ufw logging on")
    run_command("sudo ufw enable")
    run_command("sudo ufw status verbose")

# configure Snort 
def configure_snort():
    # add your specific configuration here
    run_command("sudo systemctl enable snort")
    run_command("sudo systemctl start snort")

# configure Suricata 
def configure_suricata():
    # add your specific configuration here
    run_command("sudo systemctl enable suricata")
    run_command("sudo systemctl start suricata")

# configure ClamAV-Daemon
def configure_clamav():
    run_command("sudo systemctl enable clamav-daemon")
    run_command("sudo systemctl start clamav-daemon")

# configure RKHunter 
def configure_rkhunter():
    run_command("sudo rkhunter --update")
    run_command("sudo rkhunter --propupd")  # aktualisiere die Eigenschaften

# Main function to run the script
def main():
    print("Starte die Konfiguration von SSH, LDAP und Sicherheitsanwendungen...")
    configure_ufw()
    configure_snort()
    configure_suricata()
    configure_clamav()
    configure_rkhunter()
    print("Konfiguration abgeschlossen.")

if __name__ == "__main__":
    main()

