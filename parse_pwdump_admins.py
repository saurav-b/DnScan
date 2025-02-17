#!/usr/bin/python
import io
import re
import sys

filename = sys.argv[1]
admins = dict()

with io.open(filename, encoding="utf8", errors='replace') as userfile:
    for line in userfile:
        if "Disabled=1" in line or "Disabled=True" in line or ",Expired=True" in line:
            continue
        line = line.rstrip()
        split = line.split(":")
        if len(split) == 7:
            user = split[0]
        else:
            print("Invalid format")
            sys.exit(1)
        if user:
            isadmin = False
            if "__history_" in user:
                    continue
            
            m2 = re.match('^(.*?)\\\(.*)', user)
            if m2:
                user = m2.group(2)              # Strip domain
            else:
                m2 = re.match('^(.*?)@(.*)', user)
                if m2:
                    user = m2.group(1)
            if ("IsAdministrator=True" in line or "isAdministrator=1" in line) and not "__history_" in user:
                administrator = "X"
                isadmin = True
            else:
                administrator = " "
            if ("IsDomainAdmin=True" in line or "isDomainAdmin=1" in line) and not "__history_" in user:
                domainadmin = "X"
                isadmin = True
            else:
                domainadmin = ""
            if ("IsEnterpriseAdmin=True" in line or "isEnterpriseAdmin=1" in line) and not "__history_" in user:
                enterpriseadmin = "X"
                isadmin = True
            else:
                enterpriseadmin = ""
            if isadmin:
                admins[user] = [administrator, domainadmin, enterpriseadmin]


