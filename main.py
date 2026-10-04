import socket,secrets,string,requests,base64,hashlib,os,urllib.parse,re,random as Rr,ssl,ipaddress,shodan,requests,string  
G="\033[92m";C="\033[96m";Y="\033[93m";W="\033[97m";Z="\033[0m"
b=lambda: (os.system('clear'),print(f"{G} ZEDK v7 40T {C}Zohair DZ{Z}"));g=lambda l=16:''.join(secrets.choice(string.ascii_letters+string.digits+"!@#$%")for _ in range(l))
s=lambda p:sum([len(p)>=8,any(c.isupper()for c in p),any(c.isdigit()for c in p),any(c in"!@#$%"for c in p)])
def sc(a=1,b2=200,h='127.0.0.1'):
 for pt in range(a,b2+1):
  k=socket.socket();k.settimeout(0.2)
  if k.connect_ex((h,pt))==0:print(f"{G}{pt}{Z}")
  k.close()
def site():
 u=input("URL:");u=u if"http"in u else"https://"+u
 try:r=requests.get(u,timeout=5);print(r.status_code,r.headers.get('Server',''))
 except Exception as e:print(e)
def ip():
 try:a=requests.get("https://api.ipify.org?format=json",timeout=5).json();print(a['ip']);d=requests.get(f"https://ipinfo.io/{a['ip']}/json",timeout=5).json();print(d.get('city',''),d.get('country',''))
 except:print("No net")
def bg():
 h=input("Host:");po=int(input("Port:")or 80);s=socket.socket();s.settimeout(3)
 try:s.connect((h,po));s.send(b"HEAD / HTTP/1.0\r\n\r\n");print(s.recv(600).decode(errors='ignore')[:400])
 except Exception as e:print(e)
 finally:s.close()
def who():print(requests.get(f"https://api.hackertarget.com/whois/?q={input('D/IP:')}",timeout=6).text[:800])
def sslc():
 h=input("Host:").strip()
 try:ctx=ssl.create_default_context();s=ctx.wrap_socket(socket.socket(),server_hostname=h);s.settimeout(5);s.connect((h,443));print(s.getpeercert()['notAfter']);s.close()
 except Exception as e:print(e)
def pwn():
 p=input("Pass:");h=hashlib.sha1(p.encode()).hexdigest().upper();a,b=h[:5],h[5:]
 try:r=requests.get(f"https://api.pwnedpasswords.com/range/{a}",timeout=5).text;print("PWNED!"if b in r else"Safe")
 except:print("No net")
b()
while True:
 print(f"\n{W}1.GEN 2.STR 3.SC 4.SITE 5.B64 6.URL 7.IP 8.DNS 9.HDR 10.BIN 11.SUB 12.EML 13.HID 14.FH 15.BAN 16.FAKE 17.MAC 18.EXP 19.ROB 20.MAP 21.WHO 22.RDNS 23.METH 24.SSL 25.B32 26.MOR 27.JWT 28.COOK 29.UA 30.ST 31.PWN 32.SCF 33.PING 34.GEO 35.SECH 36.LINK 37.IPC 38.TOR 39.INFO 40.EXIT{Z}")
 c=input(f"{Y}> {Z}")
 if c=='1':print(g())
 elif c=='2':print(f"{s(input('P:'))}/4")
 elif c=='3':sc()
 elif c=='4':site()
 elif c=='5':
  q=input("1.E 2.D 3.SHA:");t=input("T:");print(base64.b64encode(t.encode()).decode()if q=='1'else base64.b64decode(t.encode()).decode()if q=='2'else hashlib.sha256(t.encode()).hexdigest())
 elif c=='6':
  q=input("1.E 2.D:");t=input("U:");print(urllib.parse.quote(t)if q=='1'else urllib.parse.unquote(t))
 elif c=='7':ip()
 elif c=='8':print(socket.gethostbyname(input("Dom:")))
 elif c=='9':
  u=input("URL:");u=u if"http"in u else"https://"+u
  try:r=requests.get(u,timeout=5);[print(f"{k}:{v}")for k,v in r.headers.items()]
  except Exception as e:print(e)
 elif c=='10':t=input("T:");print(' '.join(format(ord(x),'08b')for x in t));print(t.encode().hex())
 elif c=='11':
  d=input("Dom:");L=['www','mail','ftp','admin','test','dev','api','blog','shop','app']
  for x in L:
   try:print(f"{G}{x}.{d}->{socket.gethostbyname(x+'.'+d)}{Z}")
   except:pass
 elif c=='12':print(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+",input("Text:")))
 elif c=='13':h=input("Hash:").strip();l=len(h);print("MD5"if l==32 else"SHA1"if l==40 else"SHA256"if l==64 else f"L{l}")
 elif c=='14':
  p=input("File:").strip()
  try:b=open(p,'rb').read();print(hashlib.md5(b).hexdigest()[:16],hashlib.sha256(b).hexdigest()[:16])
  except:print("No file")
 elif c=='15':bg()
 elif c=='16':n=Rr.choice(["Ali","Zohair","Sara"]);print(f"{n}{Rr.randint(10,99)} {n.lower()}{Rr.randint(100,999)}@test.dz {g(10)}")
 elif c=='17':print(requests.get(f"https://api.macvendors.com/{input('MAC:')}",timeout=5).text[:120])
 elif c=='18':print(requests.head(input("Short:"),allow_redirects=True,timeout=5).url)
 elif c=='19':
  d=input("Domain:");d=d if"http"in d else"https://"+d
  try:print(requests.get(d+"/robots.txt",timeout=5).text[:500])
  except Exception as e:print(e)
 elif c=='20':
  d=input("Domain:");d=d if"http"in d else"https://"+d
  try:print(requests.get(d+"/sitemap.xml",timeout=5).text[:500])
  except Exception as e:print(e)
 elif c=='21':who()
 elif c=='22':print(socket.gethostbyaddr(input("IP:"))[0])
 elif c=='23':
  u=input("URL:");u=u if"http"in u else"https://"+u
  try:print(requests.options(u,timeout=5).headers.get('Allow','GET,POST,OPTIONS'))
  except Exception as e:print(e)
 elif c=='24':sslc()
 elif c=='25':q=input("1.E 2.D:");t=input("T:");print(base64.b32encode(t.encode()).decode()if q=='1'else base64.b32decode(t.encode()).decode())
 elif c=='26':m={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-'};t=input("Text:").upper();print(' '.join(m.get(x,x)for x in t))
 elif c=='27':
  t=input("JWT:")
  try:p=t.split('.')[1]+'==';print(base64.urlsafe_b64decode(p).decode())
  except Exception as e:print(e)
 elif c=='28':print(urllib.parse.unquote(input("Cookie:")))
 elif c=='29':print(requests.utils.default_user_agent())
 elif c=='30':d={'200':'OK','404':'Not Found','403':'Forbidden','500':'Error','301':'Moved'};print(d.get(input("Code:"),"Unknown"))
 elif c=='31':pwn()
 elif c=='32':sc(1,1024,input("Host:")or'127.0.0.1')
 elif c=='33':
  h=input("Host:");po=int(input("Port:")or 80);k=socket.socket();k.settimeout(2)
  try:k.connect((h,po));print(f"{G}UP{Z}")
  except:print("DOWN")
  finally:k.close()
 elif c=='34':print(requests.get(f"https://ipinfo.io/{input('IP:')}/json",timeout=5).text[:500])
 elif c=='35':
  u=input("URL:");u=u if"http"in u else"https://"+u
  try:r=requests.get(u,timeout=5).headers;print("HSTS"if'HSTS'in str(r)else"no HSTS","CSP"if'CSP'in str(r)or'Content-Security'in str(r)else"no CSP")
  except Exception as e:print(e)
 elif c=='36':
  u=input("URL:");u=u if"http"in u else"https://"+u
  try:t=requests.get(u,timeout=5).text;print(re.findall(r'href=["\'](.*?)["\']',t)[:15])
  except Exception as e:print(e)
 elif c=='37':
  try:print(list(ipaddress.ip_network(input("CIDR:").strip(),strict=False).hosts())[:10])
  except Exception as e:print(e)
 elif c=='38':print(requests.get("https://check.torproject.org/torbulkexitlist",timeout=5).text.find(input("IP:"))>=0)
 elif c=='39':print(f"{C}v7 40T Zohair DZ Ethical{Z}")
 elif c=='40':break
