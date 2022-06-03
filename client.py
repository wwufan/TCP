import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.113'
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
