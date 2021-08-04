import socket

hand = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hand.connect(('data.pr4e.org', 80))
get = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
hand.send(get)

while True:
    data = hand.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

    f = open("output.txt", "a")
    f.write(data.decode())
    f.close()
    
hand.close()
