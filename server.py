import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket)

socket.connect(("www.python.org", 80))

print(socket.getsockname())

