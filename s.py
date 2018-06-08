#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from socket import *
from time import ctime

HOST = '192.168.48.137'        #主机(服务器)地址
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建套接字
tcpSerSock.bind(ADDR)                      # 监听
tcpSerSock.listen(5)

while True:
    print 'wating for connection...'
    tcpCliSock,addr = tcpSerSock.accept()  #被动接收连接
    print '...connected from:',addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)#接收来自客户端的数据
        if  data=='exit':
            break
        print data                      #输出客户端的数据
        sersay=raw_input("Input：")
        tcpCliSock.send('%s'% (sersay)) #返回给客户端的数据
    tcpCliSock.close()
