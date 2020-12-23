print('Chapter 12: Exercise 2')


#Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
#Checking http://data.pr4e.org/romeo.txt
#Overly complicated first attempt

import socket

webpage = input('Please provide a website URL: ',)

count = 0

try:
    hostname = webpage.split('/')
    hostname = hostname[2]
    webpage = str(webpage)
    print('URL:', webpage)
    cmdcommand = 'GET ' + str(webpage)+ ' HTTP/1.0\r\n\r\n'
    print(cmdcommand)

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname, 80))
    cmd = cmdcommand.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if(len(data) < 1):
            count = count + len(data)
            print('Character count is', count)
            break
        elif (len(data)< 512):
            count = count + len(data)
        elif (count < 3001) and (len(data)>1):
            print(data.decode())
            count = count + 512
        else:
            count = count + 512
    mysock.close()

except:
    print('Sorry, bad URL')
