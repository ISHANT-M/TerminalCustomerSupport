import socket

print("be patient and polite with the customer ")
print("Waiting for customer to join the chat . . . . .")

host = ""
port = 6969

try:
    s = socket.socket()
except socket.error as msg:
    print(msg)
    exit(1)
while True:
    try:
        s.bind((host, port))
        s.listen(5)
        break
    except socket.error as msg:
        print("HUSTON! We have a problem \n", msg, "\n retrying .......")
conn, addrs = s.accept()
print("connection established")
print("ip", addrs[0], "port", addrs[1])

while True:
    data = input("[you] ")
    conn.send(bytes(data, "utf-8"))
    if data == "exit":
        break
    elif "%rcv%" in data:
        rcv = conn.recv(1024)
        print("[customer] ", str(rcv, "utf-8"))


conn.close()
