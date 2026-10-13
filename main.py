import socket
# !pip install raylib
from pyray import *

#todo
class Jugador:
    def __init__()

class Partida:
    def __init__()

# Create a datagram socket
udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

ip = "127.0.0.1"
puerto = 20001
try:
    udp.connect(("0.0.0.0", 0))
    ip, puerto = s.getsockname()

#todo

jugadores = []
partidas = []


bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Bind to address and ip
udp.bind((ip, puerto))

print("UDP server up and listening")

init_window(800, 450, "Hello")

while not window_should_close():
    bytesAddressPair = udp.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    udp.sendto(bytesToSend, address)

    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 190, 200, 20, VIOLET)
    end_drawing()
close_window()
