import socket
c=socket.socket()
c.connect(('localhost',9999))
while True:
    
    cmsg=input("client-->")
    c.send(cmsg.encode())
    if cmsg.lower()=="endofchat":
            print("session is end")
            c.close()
            break
    smsg=c.recv(1024).decode()
    print(f"server-->>{smsg}".rjust(60))
    if smsg.lower()== "endofchat":
          c.close()
          print("end of chat")
          break
