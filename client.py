import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addrs = socket.getaddrinfo(socket.gethostname(), None)

for item in addrs:
    if ':' not in item[4][0]:
        host = item[4][0]
        break

port = 9092
client.connect((host, port))

while True:
    sendmsg = input('请输入:')
    if sendmsg=='q':
        break

    sendmsg = sendmsg
    client.send(sendmsg.encode('utf-8'))
    msg = client.recv(1024)
    print(msg.decode('utf-8'))

client.close()
