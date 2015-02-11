import time
def sj():
    localtime=time.localtime(time.time())
    print "Local current time :", ocaltime
def fstp(tpwz):
    from PIL import Image
    import ImageChops
    wj=open(tpwz)
    tp1=Image.open(wj)
    tp2=ImageChops.invert(tp1)
    tp2.save("tp.jpeg","JPEG")
def  pyjb(jb):
    import os
    #os.mknod("1.py")
    f=open("1.py","w")
    f.write(jb)
    f.close()
    yx=os.popen("python 1.py")
    #os.remove("1.py")
    return yx.read()
print(pyjb("print 'a'"))
