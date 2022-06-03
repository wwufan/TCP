import socket
import pymysql

socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.113'
port = 9092
socketserver.bind((host, port))

socketserver.listen(5)
clientsocket, addr = socketserver.accept()

while True:

    recvmsg = clientsocket.recv(1024)
    strData = recvmsg.decode("utf-8")

    if strData == 'q':
        break
    print('收到:' + strData)
    msg = input('回复:')
    clientsocket.send(msg.encode('utf-8'))

    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='test')
    cursor = db.cursor()
    data = {
        'test_recmsg': strData,
        'test_msg': msg}

    sql = 'INSERT INTO test_table(test_recmsg,test_msg) VALUES({},{})'.format(strData,msg)

    try:
        cursor.execute(sql)
        db.commit()
        print('ok')
    except:
        print('插入失败')
        db.rollback()
        cursor.close()
        db.close()

socketserver.close()
