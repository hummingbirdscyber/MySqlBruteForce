# MySqlBruteForce
This tool provides brute force attack on MySql and written to understand basic MySql concepts.

**CommandLine $ python3 mysql.py -h**
```
usage: mysql2.py [-h] [-u USERNAME] [-p PASSWORD] [-d DATABASES] hostname

positional arguments:
  hostname              Example:hummingbirdscyberteam.com

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        File path for usernames.Example:usernames.txt
  -p PASSWORD, --password PASSWORD
                        File path for passwords.Example:passwords.txt
  -d DATABASES, --databases DATABASES
                        File path for databases.Example:databases.txt
```

 **CommandLine $ python3 mysql.py 127.0.0.1 -u username.txt -p password.txt -d database.txt**
 ```
 --->Connected to MySQL database, username:root, password:root, host:127.0.0.1, database:pscanner
 ```
 Attention:Only Educational Purposes.
