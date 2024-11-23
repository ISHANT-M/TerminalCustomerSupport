import socket 

s = socket.socket()
print("creating socket  .. ")
host = ""
port = 6969

s.connect((host, port))
print("connected to server!")

while (True):
    sd = input("input de : ")
    s.send(bytes(sd, "utf-8"))
    data = str(s.recv(1024), "utf-8")
    print(data)
    if(sd == "exit"):
        break


