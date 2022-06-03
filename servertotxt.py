import socket
import datetime
socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.113'
port = 9092
socketserver.bind((host, port))
socketserver.listen(5)
clientsocket,addr = socketserver.accept()

while True:

    recvmsg = clientsocket.recv(1024)
    strData = recvmsg.decode('utf-8')
    if strData=='q':
        break
    print('收到:'+strData)
    msg = input('回复:')
    clientsocket.send(msg.encode("utf-8"))

    list=[]
    list.append([strData,msg])
    NowOnTxt = datetime.datetime.now().strftime('%Y-%m-%d')
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    fname = './' + now + '.txt'
    with open(fname, 'a') as f:
        for i in range(len(list)):
            f.write('{}\n'.format(list[i]))

socketserver.close()
