import os
import sys
import pwd

usernames = set()
os.system("python Welcome.py")

for entry in pwd.getpwall():
    usernames.add(entry.pw_name)
print(usernames)