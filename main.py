import socket,secrets,string,requests,os
G="\033[92m";C="\033[96m";Y="\033[93m";R="\033[0m"
def banner():
 os.system('clear')
 print(f"{G}  ███████╗███████╗██████╗")
 print(f"{G}  ╚══███╔╝██╔════╝██╔══██╗")
 print(f"{C}   💉 ZEDK ULTRA v4.1 💉")
 print(f"{C}   By Zohair | Constantine 🇩🇿")
 print(f"{Y}   ═════════════════════{R}")

def gen(l=18):
 s=string.ascii_letters+string.digits+"!@#$%"
 return ''.join(secrets.choice(s) for _ in range(l))

def strength(p):
 sc=0
 if len(p)>=8: sc+=1
 if any(c.isupper() for c in p): sc+=1
 if any(c.isdigit() for c in p): sc+=1
 if any(c in "!@#$%" for c in p): sc+=1
 return sc

def scan():
 print(f"{C}\n [SCAN 20-100]{R}")
 for pt in range(20,101):
  sk=socket.socket();sk.settimeout(0.2)
  if sk.connect_ex(('127.0.0.1',pt))==0:
   print(f"  {G}Port {pt} OPEN{R}")
  sk.close()

def check():
 u=input(f"{Y}Site: {R}").strip()
 if not u.startswith("http"): u="https://"+u
 try:
  r=requests.get(u,timeout=6)
  print(f" {C}{r.status_code} | {r.headers.get('Server','?')}{R}")
 except Exception as e: print(f" Err {e}")

banner()
while True:
 print(f"\n 1.Gen 2.Strength 3.Scan 4.Site 5.Exit")
 c=input(f"{Y}Zohair > {R}")
 if c=="1": print(f" {G}{gen()}{R}")
 elif c=="2": p=input(" Pass: "); print(f" Score: {strength(p)}/4")
 elif c=="3": scan()
 elif c=="4": check()
 elif c=="5": break