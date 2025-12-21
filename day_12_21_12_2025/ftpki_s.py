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
