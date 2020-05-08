############################################################
# copy links and saved in file which name is links.txt
# if you saved another name file you should change links.txt file name in line 13
# the py and links' files must be same directory
# I do not check working another lang books, only eng books
############################################################
import urllib.request
import urllib.parse
import subprocess

path = 'pwd'
alink='https://link.springer.com/'
links = 'links.txt'
def direc():
    global path
    out = subprocess.run([path], stdout=subprocess.PIPE)
    path = (out.stdout.decode('utf-8'))[:-1]+'/'
    print(path)

def website():
    direc() # current directory
    files = open(path+links,'r') # open file contains download links
    count = 0
    for link in files.readlines():
        site = urllib.request.urlopen(link)
        web=site.read().decode('utf-8')
        start=web.find('<h1>')
        end=web.find('</h1>')
        title = web[start+4:end]
        while title.find('/')>0: # some title contains '/', so this is a problem such as 'does not exist directory'
            title = title.replace('/','-')
        title=title.replace(' ','_')+'.PDF'
        start = web.find('content/pdf')
        end = web.find('\"',start)
        linkd = alink+web[start:end]
        urllib.request.urlretrieve(linkd, path+title) # download and create file on local
        print(str(count) + ':' +title)
        count+=1
    files.close()
