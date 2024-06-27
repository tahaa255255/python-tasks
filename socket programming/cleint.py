import socket
cleint_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    try:
        cleint_socket.connect(("127.0.0.1",50000))
        print("connection established")
        break
    except:
        print ("connection refused , will try again")
while True:        
    data_to_send=input("enter text to send: ")  
    cleint_socket.send(data_to_send.encode("utf-8"))