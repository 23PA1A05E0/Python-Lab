f = open('byte.bin','wb')
f.write(b"\x00\x01")
f.close()
f = open('byte.bin','rb')
print(f.read())
f.close() 

f = open('byte.bin','ab')
f.write(b"\n\x01\x11")
f = open('byte.bin','rb')
print(f.read())
f.close()
