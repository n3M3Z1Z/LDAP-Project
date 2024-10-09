"""
    _______      ,-----.    ,---.   .--. ________                ___    _  ________ .--.      .--.       .-------.  ____     __ 
   /   __  \   .'  .-,  '.  |    \  |  ||        |             .'   |  | ||        ||  |_     |  |       \  _(`)_ \ \   \   /  /
  | ,_/  \__) / ,-.|  \ _ \ |  ,  \ |  ||   .----'             |   .'  | ||   .----'| _( )_   |  |       | (_ o._)|  \  _. /  ' 
,-./  )      ;  \  '_ /  | :|  |\_ \|  ||  _|____              .'  '_  | ||  _|____ |(_ o _)  |  |       |  (_,_) /   _( )_ .'  
\  '_ '`)    |  _`,/ \ _/  ||  _( )_\  ||_( )_   |             '   ( \.-.||_( )_   || (_,_) \ |  |       |   '-.-'___(_ o _)'   
 > (_)  )  __: (  '\_/ \   ;| (_ o _)  |(_ o._)__|_ _     _ _  ' (`. _` /|(_ o._)__||  |/    \|  |  _ _  |   |   |   |(_,_)'    
(  .  .-'_/  )\ `"/  \  ) / |  (_,_)\  ||(_,_) --( ' )---(_I_)-| (_ (_) _)|(_,_)    |  '  /\  `  | ( ` ) |   |   |   `-'  /     
 `-'`-'     /  '. \_/``".'  |  |    |  ||   |   (_{;}_) (_(=)_) \ /  . \ /|   |     |    /  \    |(_{;}_)/   )    \      /      
   `._____.'     '-----'    '--'    '--''---'  --(_,_)---(_I_)-  ``-'`-'' '---'     `---'    `---` (_,_) `---'     `-..-'       
"""

"""
Simple python script to configure the UFW (Uncomplicated Firewall), to secure the sytem and enable nessesary Networktraffic
"""

import os
import subprocess

# configure UFW-Services
def configure_ufw():
    print("UFW wird konfiguriert...")

    # activate UFW 
    subprocess.run(['sudo', 'ufw', 'enable'], check=True)

    # Block all inciming traffic by default
    subprocess.run(['sudo', 'ufw', 'default', 'deny', 'incoming'], check=True)
    # Enable all outgoing traffic by default
    subprocess.run(['sudo', 'ufw', 'default', 'allow', 'outgoing'], check=True)

    # Grant Permmission for specifed Services

    # LDAP and LDAPS (default Port 389 for LDAP, 636 for LDAPS)
    subprocess.run(['sudo', 'ufw', 'allow', '389/tcp'], check=True)  # LDAP
    subprocess.run(['sudo', 'ufw', 'allow', '636/tcp'], check=True)  # LDAPS

    # Snort (No specific Port, watches the NEtwork Adapter) 
    print("Snort benötigt keine spezifische Firewall-Regel, da es den Netzwerkverkehr überwacht.")

    # ClamAV (ClamAV and ClamAV-Daemon)
    # ClamAV usually communicates internally but in case:
    subprocess.run(['sudo', 'ufw', 'allow', '3310/tcp'], check=True)  # ClamAV Daemon

    # Rkhunter no specific rules

    # Fail2ban: Fail2ban prevents brute force attacks and bans suspicious IP addresses
    print("Fail2ban verwaltet seine eigenen Regeln, aber wir erlauben SSH-Verbindungen.")
    subprocess.run(['sudo', 'ufw', 'allow', 'ssh'], check=True)  # SSH-Zugriff erlauben

    # Docker
    # Docker-Containers are using differnt ports depending on their configuration and usage
    print("Stelle sicher, dass alle benötigten Docker-Ports geöffnet sind.")
    subprocess.run(['sudo', 'ufw', 'allow', '2375/tcp'], check=True)  # Docker API Port (if needed)

    # Add speciic rules for your docker container here
    # subprocess.run(['sudo', 'ufw', 'allow', 'your_docker_port/tcp'], check=True)

    # Print after configuration
    subprocess.run(['sudo', 'ufw', 'status', 'verbose'])

    print("UFW-Konfiguration abgeschlossen.")

# Main function
def main():
    print("Firewall-Konfiguration basierend auf Unternehmensdiensten...")
    configure_ufw()
    print("Die Firewall wurde erfolgreich konfiguriert.")

if __name__ == "__main__":
    main()

