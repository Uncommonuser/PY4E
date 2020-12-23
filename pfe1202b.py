print('Chapter 12: Exercise 2')


#Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
#Checking http://data.pr4e.org/romeo.txt
#http://www.mit.edu/~ecprice/wordlist.10000
#http://www.py4inf.com/code/mbox.txt
#https://www.w3.org/Protocols/rfc2616/rfc2616.txt
#cleaned up second attempt

import socket

webURL = input('Please provide a website URL: ',)

count = 0

try:
    hostname = webURL.split('/')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname[2], 80))
    cmd = ('GET ' + webURL + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if(len(data) < 1):
            print ('Total character count:', count)
            break
        elif (count < 3001):
            print(data.decode())
        count = count + len(data)
    mysock.close()
    
except:
    print('Sorry, bad URL')
