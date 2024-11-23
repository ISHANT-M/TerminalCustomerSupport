import socket 
print("welcome!")

s = socket.socket()
print("creating socket  .. ")
host = ""
port = 6969

s.connect((host, port))
print("connected to support executive!")
print("your satisfaction is our biggest priority!")

while (True):
    data = str(s.recv(1024), "utf-8")
    if (data == "exit"):
        break
    elif("%rcv%" == data[0:5:1]):
        if data[5::] != "" :
            print("[support] ", data[5::1])
        inp = input("[you] ")
        s.send(bytes(inp, "utf-8"))
    else:
        print(data)    

print("we hope your problem was solved! please feel free to contact us again !")
print("have a good day!") 

s.close()        

