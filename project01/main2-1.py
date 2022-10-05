import socket

#컴퓨터의 외부 및 내부 ip확인하기
in_addr = socket.gethostbyname(socket.gethostname())

inaddr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inaddr.connect(("www.google.co.kr",443))

print(inaddr.getsockname()[0])
print(in_addr)