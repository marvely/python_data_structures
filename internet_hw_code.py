import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # a string socket.
# find a connect to mysock
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print data
mysock.close()

# can i set up a file handle and use findall to retrive all the info i need?
