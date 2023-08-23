import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = ("192.168.64.101",50501)
udp_socket.bind(dest_addr)
file = "../../data.txt"
while True:
    receive_data,client_addr = udp_socket.recvfrom(1024)
    if receive_data:
        f = open(file,'w')
        text = '2'
        f.write(text)
        f.close()
        break
