# DnScan

This package contains minor scripts written during penetration tests for a variety of purposes that may be valuable to others.

These scripts were most likely developed rapidly and have not been extensively tested or have sufficient error handling.


# Scripts

## [aspnet_identity_v2_to_john.py](aspnet_identity_v2_to_john.py)

Convert ASP.NET Identity v2 hashes into a format that can be cracked with John. The following SQL query may be used to obtain hashes:

```sql
SELECT CONCAT(UserName, ':', PasswordHash) FROM AspNetUsers
```

## [extract_ldap_hashes.py](extract_ldap_hashes.py)

Takes the output from `dbscan` or `ldapsearch` and extracts usernames and password hashes into a format that can be used with John, to allow easy password auditing for 389-ds, FreeIPA and Red Hat Identity Manager (IdM). The [FreeIPA Password Auditing](https://www.codasecurity.co.uk/articles/freeipa-password-auditing/) article on the CODA website contains further details.

## [parse_pwdump_admins.py](parse_pwdump_admins.py)

Takes the output of [NtdsAudit](https://github.com/Dionach/NtdsAudit) and parses it and generates a CSV file indicating which *assisted* users belong toward which authorized groups.

## [dnscan.py](dnscan.py)

A swift TCP port analyzer that allows you to define a spectrum of source ports from which to search.

This is useful for determining firewall rules that permit traffic from specified ports (such as 53 or 179).

The source and destination port lists are defined within the code in the '__main__' function.

