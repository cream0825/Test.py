#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *

HOST = '192.168.48.137'                 #IP��ַһ�£�ָ���������ַ
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM) 
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('>')
    if  data=='exit':
        break
    tcpCliSock.send(data)            #���͸�������������
    data = tcpCliSock.recv(BUFSIZE)  #��������
    if data=='exit':
        break
    print data

tcpCliSock.close()