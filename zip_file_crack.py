import zipfile
import os 
from threading import Thread
import optparse

def extractfile(file,password):
    try:
        file.extractall(pwd=password.encode('utf-8'))
        print("[+] Found Password %s"%(password))
    except Exception as e:
        #print(e)
        return 


def main():

    usage = "usage: %prog [options] -f <zipfile> -d <dictionary>"
    parser = optparse.OptionParser(usage=usage)

    parser.add_option('-f',dest="zname",type="string",help="specify zip file")
    parser.add_option('-d',dest="dname",type="string",help="specify dictionary file")

    (option, args) = parser.parse_args()

    if (option.zname == None) | (option.dname == None):
        print (parser.usage)
        exit(0)
    else:
        zname = option.zname
        dname = option.dname

    zfile = zipfile.ZipFile(zname)
    zpath = os.path.join(os.getcwd(),dname)
    passfile = open(zpath)
    
    for line in passfile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractfile,args=(zfile,password))
        t.start()

if __name__ == '__main__':
    main()