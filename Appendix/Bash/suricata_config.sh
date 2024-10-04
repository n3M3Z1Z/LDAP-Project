: "
                        ##                   t)                                            f)FFF                 h)     
                                           t)tTTT                                         f)                     h)     
 s)SSSS u)   UU  r)RRR  i)  c)CCCC a)AAAA    t)   a)AAAA           c)CCCC  o)OOO  n)NNNN  f)FFF           s)SSSS h)HHHH 
s)SSSS  u)   UU r)   RR i) c)       a)AAA    t)    a)AAA          c)      o)   OO n)   NN f)     ####### s)SSSS  h)   HH
     s) u)   UU r)      i) c)      a)   A    t)   a)   A          c)      o)   OO n)   NN f)                  s) h)   HH
s)SSSS   u)UUU  r)      i)  c)CCCC  a)AAAA   t)T   a)AAAA #######  c)CCCC  o)OOO  n)   NN f)             s)SSSS  h)   HH
"

#!/bin/bash

# This script installs and configures Suricata for the interface enp0s8.

# 1. Update the system
echo "Updating the system..."
sudo apt-get update && sudo apt-get upgrade -y

# 2. Install Suricata
echo "Installing Suricata..."
sudo apt-get install -y suricata

# 3. Configure Suricata
echo "Configuring Suricata..."
sudo sed -i 's/^\(interface:\).*/\1 enp0s8/' /etc/suricata/suricata.yaml

# 4. Download Suricata rules
echo "Downloading Suricata rules..."
sudo mkdir -p /etc/suricata/rules
cd /etc/suricata/rules
sudo wget https://rules.emergingthreats.net/open/suricata/emerging-all.rules

# 5. Add rule files to the configuration
echo "Adding rule files to the configuration..."
sudo bash -c 'echo -e "rule-files:\n  - emerging-all.rules" >> /etc/suricata/suricata.yaml'

# 6. Start the Suricata service
echo "Starting Suricata..."
sudo systemctl start suricata
sudo systemctl enable suricata

# 7. Display status of Suricata service
echo "Checking the status of Suricata..."
sudo systemctl status suricata

# 8. Display log output for Suricata
echo "You can monitor Suricata logs using:"
echo "tail -f /var/log/suricata/suricata.log"

echo "Suricata installation and configuration completed."

