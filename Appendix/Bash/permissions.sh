: "
 ____    ___  ____   ___ ___  ____  _____ _____ ____  ___   ____    _____     _____ __ __ 
|    \  /  _]|    \ |   T   Tl    j/ ___// ___/l    j/   \ |    \  / ___/    / ___/|  T  T
|  o  )/  [_ |  D  )| _   _ | |  T(   \_(   \_  |  TY     Y|  _  Y(   \_    (   \_ |  l  |
|   _/Y    _]|    / |  \_/  | |  | \__  T\__  T |  ||  O  ||  |  | \__  T    \__  T|  _  |
|  |  |   [_ |    \ |   |   | |  | /  \ |/  \ | |  ||     ||  |  | /  \ | __ /  \ ||  |  |
|  |  |     T|  .  Y|   |   | j  l \    |\    | j  ll     !|  |  | \    ||  T\    ||  |  |
l__j  l_____jl__j\_jl___j___j|____j \___j \___j|____j\___/ l__j__j  \___jl__j \___jl__j__j
"

#!/bin/bash

# This script configures LDAP permissions for various departments and user groups

# LDAP Admin Credentials
LDAP_ADMIN="cn=admin,dc=hamster,dc=panzer"
LDAP_PASSWORD="Password123!"

# LDAP base DN
BASE_DN="dc=hamster,dc=panzer"

# Department groups
DEPARTMENTS=("it" "it_management" "ldap_admins" "web_admins" "management" "hr" "accounting" "administration" "dau" "geschaeftsfuehrung" "logistik_leitung" "produktion_leitung" "produktion" "marketing_leitung" "verwaltung_leitung" "buchhaltung" "hr" "wazuh")

# Function to apply permissions for groups
apply_group_permissions() {
  local group=$1
  local permissions=$2
  local dn="cn=${group},ou=groups,$BASE_DN"
  
  echo "Applying permissions for group: $group"
  
  # Set ACL rules for the group in LDAP
  ldapmodify -x -D "$LDAP_ADMIN" -w "$LDAP_PASSWORD" <<EOF
dn: olcDatabase={1}mdb,cn=config
changetype: modify
add: olcAccess
olcAccess: to dn.regex="^${dn}" by group.exact="cn=${group},ou=groups,$BASE_DN" ${permissions} by * none
EOF
}

# Apply permissions for each group
for dept in "${DEPARTMENTS[@]}"; do
  case $dept in
    "it")
      # IT: Read, write, and execute permissions, no root shell
      apply_group_permissions "it" "read,write,execute"
      ;;
    "it_management")
      # IT Management: Full admin rights
      apply_group_permissions "it_management" "manage"
      ;;
    "ldap_admins")
      # LDAP Admins: Full rights on LDAP database
      apply_group_permissions "ldap_admins" "manage"
      ;;
    "web_admins")
      # Web Admins: Docker-related sudo rights
      apply_group_permissions "web_admins" "write"
      ;;
    "management")
      # Management: Access to own and specific departmental folders
      apply_group_permissions "management" "read"
      ;;
    "hr" | "accounting" | "administration")
      # HR, Accounting, Administration: Access to their own departmental folders
      apply_group_permissions "$dept" "write"
      ;;
    "dau")
      # DAU: Only login credentials
      apply_group_permissions "dau" "auth"
      ;;
    "geschaeftsfuehrung")
      # Executive Management: Access to own, administration, HR, and accounting folders
      apply_group_permissions "geschaeftsfuehrung" "read"
      ;;
    "logistik_leitung")
      # Logistics Management: Write access to own folders
      apply_group_permissions "logistik_leitung" "write"
      ;;
    "produktion_leitung")
      # Production Management: Write access to own folders
      apply_group_permissions "produktion_leitung" "write"
      ;;
    "produktion")
      # Production: Write access to own folders
      apply_group_permissions "produktion" "write"
      ;;
    "marketing_leitung")
      # Marketing Management: Write access to own folders
      apply_group_permissions "marketing_leitung" "write"
      ;;
    "verwaltung_leitung")
      # Administration Management: Write access to own folders
      apply_group_permissions "verwaltung_leitung" "write"
      ;;
    "buchhaltung")
      # Accounting: Access to own folders
      apply_group_permissions "buchhaltung" "write"
      ;;
    "wazuh")
      # Wazuh: Write access to own folders
      apply_group_permissions "wazuh" "write"
      ;;
  esac
done

echo "LDAP permissions successfully applied."
