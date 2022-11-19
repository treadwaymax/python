registry_key = reg.handle.open("Microsoft\Windows NT\CurrentVersion")
map(lambda x: x.name(), registry_key.suybkeys())

#A TCP server listener is being configured
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",1024))

raw_data=b"\x00\x01\x02\x03\x04"
(w,x,y,z)=struct.unpack(r'!BHBB',raw_data)
y = #what does it equal
y=3