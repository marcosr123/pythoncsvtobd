import socket

servers = [ 
        "192.168.4.94:443", 
        "192.168.4.94:3306", 
        "mysql.srtma.net:3306", 
        "mysql.srtma.net:443"
        ]

for server in servers:
    try:
        host, port = server.split(":")
        port = int(port)
        socket.create_connection((host, port), 3)
        print(server, "OK")
    except:
        print(server, "FAIL")