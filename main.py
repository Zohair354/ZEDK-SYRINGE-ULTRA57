import socket,secrets,string,requests,base64,hashlib,os,urllib.parse as ul
G="\033[92m";C="\033[96m";Y="\033[93m";R="\033[0m"
def b():
 os.system('clear')
 print(f"{G} ZEDK ULTRA v5.3 {C}💉 12 TOOLS\n{Y} ==============={R}")
def gen():
 import string as st
 s=st.ascii_letters+st.digits+"!@#$%"
 return ''.join(secrets.choice(s) for _ in range(16))
def scan():
 for p in range(20,101):
  s=socket.socket();s.settimeout(0.2)
  if s.connect_ex(('127.0.0.1',p))==0: print(f"{G} {p} OPEN{R}")
  s.close()
def ip():
 try: print(requests.get("https://api.ipify.org",timeout=4).text)
 except: print(" No net")
def dns(d):
 try: print(socket.gethostbyname(d))
 except: print(" Not found")
b()
while True:
 print("\n 1.Gen 2.Stren 3.Scan 4.Site 5.B64 6.URL 7.IP 8.DNS 9.Head 10.Hex 11.Info 12.Exit")
 c=input(f"{Y}Z > {R}")
 if c=='1': print(f"{G}{gen()}{R}")
 elif c=='2':
  p=input(" Pass: ");print(f" Score: {sum([len(p)>=8,any(x.isupper() for x in p),any(x.isdigit() for x in p),any(x in '!@#$%' for x in p)])}/4")
 elif c=='3': scan()
 elif c=='4':
  u=input(" Site: "); 
  if not u.startswith("http"): u="https://"+u
  try: print(requests.get(u,timeout=5).status_code)
 