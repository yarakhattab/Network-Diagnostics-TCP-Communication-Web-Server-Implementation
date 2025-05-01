from socket import *
portnumber=6060 
serversocket = socket(AF_INET,SOCK_STREAM)
serversocket.bind(('',portnumber))
serversocket.listen(1)
print ("The server is ready to listen on port 6060")
while True:
    connectionSocket, addr = serversocket.accept()
    message=connectionSocket.recv(2048).decode()
    print(addr)
    IP= addr[0]
    port=addr[1]
    print("IP: "+ str(IP) +",Port: "+ str(port))
    print("_____")
    print(message)
    print("___________")
    if message !='':
        requestedfile=message.split(' ')[1].replace('/','')
        print("The Requested File is: "+requestedfile)
    else:
        connectionSocket.close()
        continue
    try:
        if requestedfile == '' or requestedfile =='index.html' or requestedfile=='main_en.html' or requestedfile == 'en':
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            main_html=open('main_en.html' ,'rb')
            connectionSocket.send(main_html.read())
            main_html.close()
        elif  requestedfile=='ar':
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            main_html=open('main_ar.html' ,'rb')
            connectionSocket.send(main_html.read())
            main_html.close()
        elif '.html' in requestedfile:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            requested_file= open(str(requestedfile), 'rb')
            connectionSocket.send(requested_file.read())
            requested_file.close()
        elif '.css' in requestedfile:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/css \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            requested_file= open(str(requestedfile), 'rb')
            connectionSocket.send(requested_file.read())
            requested_file.close()
        elif '.png' in requestedfile:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: image/png \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            requested_file= open(str(requestedfile), 'rb')
            connectionSocket.send(requested_file.read())
            requested_file.close()
        elif '.jpg' in requestedfile:
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: image/jpeg \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            requested_file= open(str(requestedfile), 'rb')
            connectionSocket.send(requested_file.read())
        elif requestedfile =='so':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connectionSocket.send("Location: https://stackoverflow.com/\r\n".encode())
        elif requestedfile =='itc':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connectionSocket.send("Location: https://itc.birzeit.edu/register/\r\n".encode())  
        
        
        else:
            raise Exception('Not found')
    except Exception as e:
        connectionSocket.send(f"HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send(f"Content-Type: text/html \r\n".encode())
        connectionSocket.send(f"\r\n".encode())
        print(requestedfile +" not found")
        print('\b\bResponse status:HTTP/1.1 404 Not Found')
        requested_file='<!DOCTYPE html>'\
'<html>'\
'<style>'\
' * {text-align: left;}'\
'#Error{ color: red;}#name{ font-weight: bold;}'\
'</style>'\
'<head>'\
'<title>Error 404</title>'\
'</head>'\
'<body>'\
'<div id="Error">'\
' <h1>The file is not found</h1>'\
' </div>'\
' <div id="name">'\
'<p>Miassar Shamla - 1210519</p>'\
'<p>Taleen Bayatneh - 1211305</p>'\
'<p>Yara Khattab - 1210520</p>'\
' </div>'\
' <div>'\
'<p> Ip Adress: '+ str(IP)+ ', Port Number: ' +str(port)+\
'</p> </div>'\
'</body></html>'\

        connectionSocket.send(requested_file.encode())
    connectionSocket.close()