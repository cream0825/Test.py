#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *

HOST = '192.168.48.137'                 #IP地址一致，指向服务器地址
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM) 
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('>')
    if  data=='exit':
        break
    tcpCliSock.send(data)            #发送给服务器的数据
    data = tcpCliSock.recv(BUFSIZE)  #接收数据
    if data=='exit':
        break
    print data

tcpCliSock.close()