print('Chapter 12: Exercise 5')


#Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv is receiving characters (newlines and all), not lines
#Checking http://data.pr4e.org/romeo.txt
#http://www.mit.edu/~ecprice/wordlist.10000
#http://www.py4inf.com/code/mbox.txt
#https://www.w3.org/Protocols/rfc2616/rfc2616.txt
#http://data.pr4e.org/intro-short.txt

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
            #use find() with byte b" in order to find the right position
            pos = data.find(b"\r\n\r\n")
            #need to add 4 because pos finds starting at the first \r so pos+4 accounts for the next three
            print(data[pos+4:].decode())
        count = count + len(data)
    mysock.close()

except:
    print('Sorry, bad URL')
