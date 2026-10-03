import socket,secrets,string,requests,base64,hashlib,os,urllib.parse
G="\033[92m";C="\033[96m";Y="\033[93m";W="\033[97m";R="\033[0m"
def banner():
 os.system('clear')
 print(f"{G}  ███████╗███████╗██████╗\n  ╚══███╔╝██╔════╝██╔══██╗\n{C}   💉 ZEDK ULTRA v5.1 - 12 TOOLS 💉\n   By Zohair | Constantine 🇩🇿\n{Y}   ═══════════════════════{R}")
def gen(l=18):
 s=string.ascii_letters+string.digits+"!@#$%^&*"
 return ''.join(secrets.choice(s) for _ in range(l))
def strength(p):
 return sum([len(p)>=8,any(c.isupper()for c in p),any(c.isdigit()for c in p),any(c in "!@#$%"for c in p)])
def scan():
 print(f"{C}\n [SCAN 127.0.0.1 20-200]{R}")
 for pt in range(20,201):
  sk=socket.socket();sk.settimeout(0.2)
  if sk.connect_ex(('127.0.0.1',pt))==0:print(f"  {G}Port {pt} OPEN{R}")
  sk.close()
def check_site():
 u=input(f"{Y}Site: {R}").strip()
 if not u.startswith("http"):u="https://"+u
 try:
  r=requests.get(u,timeout=6);print(f" {C}{r.url} -> {r.status_code}{R}\n Server: {r.headers.get('Server','?')}")
 except Exception as e:print(f" Err {e}")
def b64_tool():
 c=input(" 1.Encode 2.Decode 3.SHA256 > ")
 if c=='1':print(base64.b64encode(input(" Text: ").encode()).decode())
 elif c=='2':
  try:print(base64.b64decode(input(" B64: ").encode()).decode())
  except:print(" Invalid")
 else:print(hashlib.sha256(input(" Text: ").encode()).hexdigest())
def url_tool():
 c=input(" 1.Encode 2.Decode > ")
 print(urllib.parse.quote(input(" URL: ")) if c=='1' else urllib.parse.unquote(input(" Encoded: ")))
def my_ip():
 try:
  r=requests.get("https://api.ipify.org?format=json",timeout=5).json();print(f" {G}IP: {r['ip']}{R}")
  d=requests.get(f"https://ipinfo.io/{r['ip']}/json",timeout=5).json();print(f" City: {d.get('city','?')} | Country: {d.get('country','?')}")
 except:print(" No internet")
def dns_lookup():
 d=input(f"{Y}Domain: {R}").strip()
 try:print(f" IP: {socket.gethostbyname(d)}")
 except:print(" Not found")
def headers_dump():
 u=input(f"{Y}URL: {R}").strip()
 if not u.startswith("http"):u="https://"+u
 try:
  r=requests.get(u,timeout=6)
  for k,v in r.headers.items():print(f" {k}: {v}")
 except Exception as e:print(e)
def bin_converter():
 t=input(" Text: ");print(f" Binary: {' '.join(format(ord(c),'08b')for c in t)}\n Hex: {t.encode().hex()}")
banner()
while True:
 print(f"\n{W} 1.Gen 2.Str 3.Scan 4.Site 5.B64 6.URL 7.MyIP 8.DNS 9.Headers 10.Bin 11.Info 12.Exit{R}")
 c=input(f"{Y}Zohair > {R}")
 if c=='1':print(f" {G}{gen()}{R}")
 elif c=='2':print(f" Score: {strength(input(' Pass: '))}/4")
 elif c=='3':scan()
 elif c=='4':check_site()
 elif c=='5':b64_tool()
 elif c=='6':url_tool()
 elif c=='7':my_ip()
 elif c=='8':dns_lookup()
 elif c=='9':headers_dump()
 elif c=='10':bin_converter()
 elif c=='11':print(f"{C} ZEDK ULTRA v5.1 - 12 Tools - Ethical{R}")
 elif c=='12':break
