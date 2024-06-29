import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",50000))
server_socket.listen(10)
print("waiting for connection...")
cleint_socket,cleint_ip_port=server_socket.accept()
print("connection esablished from ip:",cleint_ip_port[0],"and port:",cleint_ip_port[1])
print("recevied data :")
while True:
    recv_data=cleint_socket.recv(1024)
    cleint_socket.send("hello".encode("utf-8"))
    print(recv_data.decode("utf-8"))


