"""
                   | |                                       
  ___ _ __ ___  __ _| |_ ___  _   _ ___  ___ _ __ _ __  _   _ 
 / __| '__/ _ \/ _` | __/ _ \| | | / __|/ _ \ '__| '_ \| | | |
| (__| | |  __/ (_| | ||  __/| |_| \__ \  __/ |_ | |_) | |_| |
 \___|_|  \___|\__,_|\__\___| \__,_|___/\___|_(_)| .__/ \__, |
                          ______                 | |     __/ |
                         |______|                |_|    |___/ 
"""

"""
This python scripted is designedto add the listed users to the specified and already existing groups on the LDAP-Server.
It can be modified to add new users in the future as well.
""" 

import subprocess

# List of users to add
users = [
    {
        "uid": "markus.wagner",
        "cn": "Markus Wagner",
        "sn": "Wagner",
        "userPassword": "Password123!",
        "gidNumber": "10012",  # Group ID based on the user's group
        "homeDirectory": "/home/users/markus.wagner",
        "uidNumber": "20001"  # Unique user ID
    },
    {
        "uid": "lisa.neumann",
        "cn": "Lisa Neumann",
        "sn": "Neumann",
        "userPassword": "Password123!",
        "gidNumber": "10012",
        "homeDirectory": "/home/users/lisa.neumann",
        "uidNumber": "20002"
    },
    {
        "uid": "david.zimmermann",
        "cn": "David Zimmermann",
        "sn": "Zimmermann",
        "userPassword": "Password123!",
        "gidNumber": "10012",
        "homeDirectory": "/home/users/david.zimmermann",
        "uidNumber": "20003"
    },
    {
        "uid": "thomas.falke",
        "cn": "Thomas Falke",
        "sn": "Falke",
        "userPassword": "Password123!",
        "gidNumber": "10013",
        "homeDirectory": "/home/users/thomas.falke",
        "uidNumber": "20004"
    },
    {
        "uid": "david.thornton",
        "cn": "David Thornton",
        "sn": "Thornton",
        "userPassword": "Password123!",
        "gidNumber": "10014",
        "homeDirectory": "/home/users/david.thornton",
        "uidNumber": "20005"
    },
    {
        "uid": "michael.stone",
        "cn": "Michael Stone",
        "sn": "Stone",
        "userPassword": "Password123!",
        "gidNumber": "10015",
        "homeDirectory": "/home/users/michael.stone",
        "uidNumber": "20006"
    },
]

def check_user_exists(uid):
    """Check if the user already exists in LDAP."""
    try:
        result = subprocess.check_output(
            ["ldapsearch", "-x", "-b", "ou=users,dc=hamster,dc=panzer", f"uid={uid}"],
            universal_newlines=True  # Use this for text output in Python 3.6
        )
        return "dn:" in result
    except subprocess.CalledProcessError:
        return False

def add_user(user):
    """Add a new user to LDAP."""
    ldif_entry = f"""
dn: uid={user['uid']},ou=users,dc=hamster,dc=panzer
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: top
cn: {user['cn']}
sn: {user['sn']}
uid: {user['uid']}
userPassword: {user['userPassword']}
gidNumber: {user['gidNumber']}
homeDirectory: {user['homeDirectory']}
uidNumber: {user['uidNumber']}
"""
    try:
        subprocess.run(
            ["ldapadd", "-x", "-D", "cn=admin,dc=hamster,dc=panzer", "-W"],
            input=ldif_entry,
            universal_newlines=True,  # Use this for text input in Python 3.6
            check=True
        )
        print(f"User '{user['uid']}' added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding user '{user['uid']}': {e}")

def main():
    for user in users:
        uid = user["uid"]
        if not check_user_exists(uid):
            add_user(user)
        else:
            print(f"User '{uid}' already exists. Skipping...")

if __name__ == "__main__":
    main()

