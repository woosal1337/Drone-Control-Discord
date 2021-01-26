import socket
import keyboard
import time

# Connecting to the drone
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ("192.168.10.1", 8889)
sock.bind(('', 9000))


# Setup and fly/takeoff
def start():
    msg = 'command'
    msg = msg.encode()
    print(msg)
    sent = sock.sendto(msg, tello_address)

    msg = 'takeoff'
    msg = msg.encode()
    print(msg)
    sent = sock.sendto(msg, tello_address)

    msg = 'up 25'
    msg = msg.encode()
    print(msg)
    sent = sock.sendto(msg, tello_address)

    msg = 'stop'
    msg = msg.encode()
    print(msg)
    sent = sock.sendto(msg, tello_address)


# Functions
def forward():
    print("Forward!")
    for i in range(30):
        msg = 'forward 30'
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_address)
    time.sleep(0.666)


def left():
    print("Left!")
    for i in range(30):
        msg = 'left 30'
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_address)
    time.sleep(0.666)


def right():
    print('Right!')
    for i in range(30):
        msg = 'right 30'
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_address)
    time.sleep(0.666)


def back():
    print('Back!')
    for i in range(30):
        msg = 'back 30'
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_address)
    time.sleep(0.666)

def cw():
    print('Clock Wise!')
    for i in range(30):
        msg = 'cw 10'
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_address)
    time.sleep(0.666)


def ccw():
    print('Counter Clock Wise!')
    for i in range(30):
        msg = 'ccw 10'
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_address)
    time.sleep(0.666)


def land():
    print('Landing!')
    for i in range(30):
        msg = 'land'
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg, tello_address)
    time.sleep(0.666)
