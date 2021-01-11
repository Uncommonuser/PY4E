print('Chapter 12: Exploring the HyperText Transport Protocol')


#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response header
#http://data.pr4e.org/intro-short.txt

import socket

webpage = input('Please provide a website URL: ',)


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
        if (len(data) < 1):
            break
        print(data.decode())
    mysock.close()

except:
    print('Sorry, bad URL')
