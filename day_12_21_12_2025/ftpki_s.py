# paramiko - biblioteka do połaczeń np.: ssh
# https://test.rebex.net/
# demo/ password
import paramiko

# pip install paramiko

host = "test.rebex.net"
port = 22
username = "demo"
password = "password"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=host,
    port=port,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False,
    timeout=15
)

# moze byc wymagana na linux/unix
# look_for_keys=False,
#     allow_agent=False,

sftp = client.open_sftp()
print("PWD:", sftp.getcwd())  # PWD: None
print("LIST:", sftp.listdir("."))  # LIST: ['pub', 'readme.txt']

# sftp.get('readme.txt', "readme.txt")
sftp.get('readme.txt', "../readme.txt")

sftp.close()
client.close()
