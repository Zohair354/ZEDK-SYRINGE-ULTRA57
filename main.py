import socket,secrets,string,requests,base64,hashlib,os,urllib.parse
G="\033[92m";C="\033[96m";Y="\033[93m";W="\033[97m";R="\033[0m"

def banner():
 os.system('clear')
 print(f"{G}  ███████╗███████╗██████╗")
 print(f"  ╚══███╔╝██╔════╝██╔══██╗")
 print(f"{C}   💉 ZEDK ULTRA v5.0 - 12 TOOLS 💉")
 print(f"   By Zohair | Constantine 🇩🇿")
 print(f"{Y}   ═══════════════════════{R}")

def gen(l=18):
 s=string.ascii_letters+string.digits+"!@#$%^&*"
 return ''.join(secrets.choice(s) for _ in range(l))

def strength(p):
 sc=sum([len(p)>=8,any(c.isupper() for c in p),any(c.isdigit() for c in p),any(c in "!@#$%" for c in p)])
 return sc

def scan():
 print(f"{C}\n [SCAN 127.0.0.1 20-200]{R}")
 for pt in range(20,201):
  sk=socket.socket();sk.settimeout(0.2)
  if sk.connect_ex(('127.0.0.1',pt))==0: print(f"  {G}Port {pt} OPEN{R}")
  sk.close()

def check_site():
 u=input(f"{Y}Site: {R}").strip()
 if not u.startswith("http"): u="https://"+u
 try:
  r=requests.get(u,timeout=6)
  print(f" {C}{r.url} -> {r.status_code}{R}")
  for h in ["Server","X-Frame-Options","Strict-Transport-Security"]: print(f"  {h}: {r.headers.get(h,'?')}")
 except Exception as e: print(f" Err {e}")

def b64_tool():
 c=input(" 1.Encode 2.Decode 3.SHA256 > ")
 if c=='1': print(base64.b64encode(input(" Text: ").encode()).decode())
 elif c=='2': 
  try: print(base64.b64decode(input(" B64: ")).decode())
  except: print(" Invalid")
 elif c=='3': print(hashlib.sha256(input(" Text: ").encode()).hexdigest())

def url_tool():
 c=input(" 1.Encode 2.Decode > ")
 if c=='1': print(urllib.parse.quote(input(" URL: ")))
 else: print(urllib.parse.unquote(input(" Encoded: ")))

def my_ip():
 try:
  r=requests.get("https://api.ipify.org?format=json",timeout=5).json()