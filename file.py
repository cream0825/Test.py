# encoding=utf-8
import socket
import hashlib
import struct

HOST = '192.168.48.137 '
PORT = 12345
BUFFER_SIZE = 1024
HEAD_STRUCT = '128sIq'
info_size = struct.calcsize(HEAD_STRUCT)




def unpack_file_info(file_info):
    file_name, file_name_len, file_size = struct.unpack(HEAD_STRUCT, file_info)
    file_name = file_name[:file_name_len]
    return file_name, file_size


def recv_file():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (HOST, PORT)
        sock.bind(server_address)
	print 'Waiting connection'
        sock.listen(1)
        client_socket, client_address = sock.accept()
        print "Connected %s successfully" % str(client_address)

        file_info_package = client_socket.recv(info_size)
        file_name, file_size = unpack_file_info(file_info_package)

        recved_size = 0
        with open(file_name, 'wb') as fw:
            while recved_size < file_size:
                remained_size = file_size - recved_size
                recv_size = BUFFER_SIZE if remained_size > BUFFER_SIZE else remained_size
                recv_file = client_socket.recv(recv_size)
                recved_size += recv_size
                fw.write(recv_file)
            print 'Received successfully'
    except socket.errno, e:
        print "Socket error: %s" % str(e)
    finally:
        sock.close()

if __name__ == '__main__':
    recv_file()
