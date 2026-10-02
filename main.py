cat > main.py << 'EOF'
import socket, secrets, string, requests, base64, hashlib, urllib.parse

def banner():
    print("\033[1;92m")
    print("="*50)
    print("  ____   ___   _   _   _   ___  ____")
    print(" /_  /  / _ \\ | | | | /_\\ | _ \\| _  \\")
    print("  / /  | | | | | |_| |/ _ \\|   /| |_) |")
    print(" / /__ | |_| | |  _  /_\\ \\_\\ |  _ <")
    print("/____| \\___/  |_| |_/_/ \\_\\___/|_| \\_\\")
    print("")
    print("  ______ ______ _____  _  __")
    print(" |___  /|  ____|  _  \\| |/ /")
    print("   / / | |__  | | | | | / /")
    print("  / /  |  __| | | | | | <")
    print(" / /__ | |____| |/ /| |\\ \\")
    print("/_____||______|___/ |_| \\_\\")
    print("\033[0m")
    print("\033[1;96m  💉  Z O H A I R  Z E D K  💉\033[0m")
    print("  Medical & Security Toolkit v4.1 ULTRA")
    print("  By Zohair - Ethical Use Only")
    print("="*50)

def gen_password(l=20):
    chars=string.ascii_letters+string.digits+"!@#$%^&*"
    return ''.join(secrets.choice(chars) for _ in range(l))

def scan_localhost():
    print("\n[ Scanning your phone 127.0.0.1 ]")
    for port in range(20,101):
        s=socket.socket(); s.settimeout(0.3)
        if s.connect_ex(('127.0.0.1',port))==0:
            print(f" -> Port {port} OPEN")
        s.close()
    print(" Done.")

def check_site():
    url=input(" Website (ex: google.com): ").strip()
    if not url.startswith("http"): url="https://"+url
    try:
        r=requests.get(url,timeout=8,headers={"User-Agent":"ZohairToolkit"})
        print(f"\n URL: {r.url}")
        print(f" HTTPS: {'YES ✅' if r.url.startswith('https') else 'NO ❌'}")
        for h in ["X-Frame-Options","X-Content-Type-Options","Strict-Transport-Security"]:
            print(f"  {h}: {r.headers.get(h,'Missing ⚠️')}")
    except Exception as e:
        print(f" Error: {e}")

def encoder():
    print("\n [ Encoder ]")
    print("  1. Base64 Encode")
    print("  2. Base64 Decode")
    print("  3. Hash SHA256")
    c=input("  Choose > ")
    if c=='1':
        t=input("  Text: "); print("  ", base64.b64encode(t.encode()).decode())
    elif c=='2':
        t=input("  Base64: ")
        try: print("  ", base64.b64decode(t).decode())
        except: print("  Invalid!")
    elif c=='3':
        t=input("  Text: "); print("  SHA256:", hashlib.sha256(t.encode()).hexdigest())

banner()
while True:
    print("\n\033[1;97m [ MAIN MENU ] \033[0m")
    print("  1. Generate Strong Password")
    print("  2. Check Password Strength")
    print("  3. Scan My Local Ports")
    print("  4. Check Website Security")
    print("  5. Encoder / Decoder")
    print("  6. Exit")
    
    c=input("\n Zohair > ")
    if c=='1':
        print(f"  Password: {gen_password()}")
    elif c=='2':
        p=input("  Password to check: ")
        s=0
        if len(p)>=8: s+=1
        if any(x.isupper() for x in p): s+=1
        if any(x.islower() for x in p): s+=1
        if any(x.isdigit() for x in p): s+=1
        if any(x in "!@#$%^&*" for x in p): s+=1
        print(f"  Strength: {s}/5")
    elif c=='3': scan_localhost()
    elif c=='4': check_site()
    elif c=='5': encoder()
    elif c=='6':
        print("  Goodbye Zohair!")
        break
    else:
        print("  Invalid choice")
EOF