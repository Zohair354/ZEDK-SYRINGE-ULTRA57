cd ZEDK-SYRINGE-ULTRA57
rm main.py
cat > main.py << 'PYEOF'
import socket,secrets,requests,base64,os,urllib.parse as ul
G="\033[92m";C="\033[96m";Y="\033[93m";R="\033[0m"
def b(): os.system('clear');print(f"{G} ZEDK v6 {C}💉 10 TOOLS\n{Y}=========={R}")
def gen():
 import string; s=string.ascii_letters+string.digits+"!@#$%"
 return ''.join(secrets.choice(s) for _ in range(12))
def sc():
 for p in range(20,81):
  k=socket.socket();k.settimeout(0.2)
  if k.connect_ex(('127.0.0.1',p))==0: print(f"{G}{p} OPEN{R}")
  k.close()
b()
while 1:
 print("\n 1.Gen 2.Str 3.Scan 4.Site 5.B64 6.URL 7.IP 8.DNS 9.Head 10.Hex 11.Exit")
 c=input(f"{Y}> {R}")
 if c=='1': print(gen())
 elif c=='2': p=input("Pass:");print(f" {sum([len(p)>=8,any(x.isupper()for x in p),any(x.isdigit()for x in p),any(x in '!@#$%'for x in p)])}/4")
 elif c=='3': sc()
 elif c=='4':
  h=input("Site:"); 
  if not h.startswith("http"): h="https://"+h
  try: print(requests.get(h,timeout=4).status_code)
  except: print("Err")
 elif c=='5': print(base64.b64encode(input("Txt:").encode()).decode())
 elif c=='6': print(ul.quote(input("URL:")))
 elif c=='7':
  try: print(requests.get("https://api.ipify.org",timeout=4).text)
  except: print("No net")
 elif c=='8':
  try: print(socket.gethostbyname(input("Dom:")))
  except: print("No")
 elif c=='9':
  h=input("URL:"); 
  if not h.startswith("http"): h="https://"+h
  try:
   r=requests.get(h,timeout=4)
   for k,v in list(r.headers.items())[:5]: print(k)
  except: print("Err")
 elif c=='10': print(input("Txt:").encode().hex())
 elif c=='11': break
PYEOF
python main.py