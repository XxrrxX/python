addr = input('host: ')
h = open('/var/www/html/javascript/inyectar/inyectado/flask/h/host.txt','w')
h.write(addr)
h.close()
