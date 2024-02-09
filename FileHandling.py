a= input("Enter text to write")
ar=open('log.txt','r')
filedata=ar.read()
aa=open('log2.txt','a')
aa.write(filedata)
aa.write(a)

### file flush####
aa.flush()
aa.close()

### file flush####
ar.flush()
ar.close()