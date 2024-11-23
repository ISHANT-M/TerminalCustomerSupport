import socket

host = ""
port = 6969

try:
    s = socket.socket()
except socket.error as msg:
    print(msg)
    exit(1)
while(True):
    try:
        s.bind((host, port))
        s.listen(5)
        break
    except socket.error as msg:
        print("HUSTON! We have a problem \n",msg, "\n retrying .......")
conn, addrs = s.accept()
print("connection established")
print("ip",addrs[0],"port",addrs[1])
print(addrs)

while True:
   data = conn.recv(1024)
   if data == b"exit":
       break
   conn.send(data)

conn.close()
