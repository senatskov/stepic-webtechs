import socket
import threading

def listener(conn):
	data = conn.recv(1024)
	conn.send(data)
	conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('0.0.0.0', 2222))
s.bind(('127.0.0.1', 2222))
s.listen(10)
i = 10
while i > 0:
	conn, addr = s.accept()
	t1 = threading.Thread(target=listener, args=(conn,))
	t1.start()
	i -= 1


	