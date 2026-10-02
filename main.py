import socket, secrets, string, requests, base64, hashlib
def banner():
    print("\033[1;92m"+"="*50)
    print("  ____   ___   _   _   _   ___  ____")
    print(" /_  /  / _ \\ | | | | /_\\ | _ \\| _  \\")
    print("  / /  | | | | | |_| |/ _ \\|   /| |_) |")
    print(" / /__ | |_| | |  _  /_\\ \\_\\ |  _ <")
    print("/____| \\___/  |_| |_/_/ \\_\\___/|_| \\_\\")
    print("\n  ______ ______ _____  _  __")
    print(" |___  /|  ____|  _  \\| |/ /")
    print("   / / | |__  | | | | | / /")
    print("  / /  |  __| | | | | | <")
    print(" / /__ | |____| |/ /| |\\ \\")
    print("/_____||______|___/ |_| \\_\\")
    print("\033[0m\033[1;96m  💉  Z O H A I R  Z E D K  💉\033[0m")
    print("  Medical & Security Toolkit v4.1 ULTRA\n"+"="*50)
def gen_password(l=20):
    chars=string.ascii_letters+string.digits+"!@#$%^&*"
    return ''.join(secrets.choice(chars) for _ in range(l))
def scan_localhost():
    print("\n[ Scanning 127.0.0.1 ]")
    for port in range(20,101):
        s=socket.socket();s.settimeout(0.3)
        if s.connect_ex(('127.0.0.1',port))==0: print(f" -> Port {port} OPEN")
        s.close()
    print(" Done.")
def check_site():
    url=input(" Website: ").strip()
    if not url.startswith("http"): url="https://"+url
    try:
        r=requests.get(url,timeout=8)
        print(f"\n URL: {r.url} -> {r.status_code}")
    except Exception as e: print(f" Error: {e}")
def encoder():
    c=input(" 1.Encode 2.Decode 3.Hash > ")
    if c=='1': t=input(" Text: "); print(base64.b64encode(t.encode()).decode())
    elif c=='2': t=input(" Base64: "); print(base64.b64decode(t).decode())
    elif c=='3': t=input(" Text: "); print(hashlib.sha256(t.encode()).hexdigest())
banner()
while True:
    print("\n [ MAIN MENU ]\n 1.Gen Pass 2.Strength 3.Scan 4.Site 5.Encode 6.Exit")
    c=input("\n Zohair > ")
    if c=='1': print(f"  {gen_password()}")
    elif c=='2':
        p=input("  Pass: "); s=0
        if len(p)>=8: s+=1
        if any(x.isupper() for x in p): s+=1
        if any(x.islower() for x in p): s+=1
        if any(x.isdigit() for x in p): s+=1
        if any(x in "!@#$%^&*" for x in p): s+=1
        print(f"  Strength: {s}/5")
    elif c=='3': scan_localhost()
    elif c=='4': check_site()
    elif c=='5': encoder()
    elif c=='6': break