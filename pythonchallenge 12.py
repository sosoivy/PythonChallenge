f = open('E:\Development\GitHub\PythonChallenge\evil2.gfx','rb')  
content = f.read()  
f.close()  
  
for i in xrange(5):  
    f = open('E:\Development\GitHub\PythonChallenge\%d.jpg' % i, 'wb')  
    f.write(content[i::5])  
    f.close()  