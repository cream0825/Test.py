#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from socket import *
from time import ctime

HOST = '192.168.48.137'        #����(������)��ַ
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # �����׽���
tcpSerSock.bind(ADDR)                      # ����
tcpSerSock.listen(5)

while True:
    print 'wating for connection...'
    tcpCliSock,addr = tcpSerSock.accept()  #������������
    print '...connected from:',addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)#�������Կͻ��˵�����
        if  data=='exit':
            break
        print data                      #����ͻ��˵�����
        sersay=raw_input("Input��")
        tcpCliSock.send('%s'% (sersay)) #���ظ��ͻ��˵�����
    tcpCliSock.close()