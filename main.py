import socket, secrets, string, requests, base64, hashlib, os, time

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def banner():
    os.system('clear')
    print(f"{GREEN}")
    print(r"""
  ███████╗███████╗██████╗ ██╗  ██╗
  ╚══███╔╝██╔════╝██╔══██╗██║ ██╔╝
    ███╔╝ █████╗  ██║  ██║█████╔╝ 
   ███╔╝  ██╔══╝  ██║  ██║██╔═██╗ 
  ███████╗███████╗██████╔╝██║  ██╗
  ╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝
    """)
    print(f"{CYAN}     💉  SYRINGE ULTRA v4.1  💉{RESET}")
    print(f"{YELLOW}  ======================================{RESET}")
    print(f"{GREEN}   The First Medical Security Toolkit{RESET}")
    print(f"{CYAN}   By Zohair ZEDK from Constantine 🇩🇿{RESET}")
    print(f"{YELLOW}  ======================================{RESET}\n")

def gen_password(l=20):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(chars) for _ in range(l))

def scan_localhost():
    print(f"\n{CYAN}[ Scanning 127.0.0.1 20-100 ]{RESET}")
    for port in range(20, 101):
        s = socket.socket()
        s.settimeout(0.3)
        if s.connect_ex(('127.0.0.1', port)) == 0:
            print(f" {GREEN}-> Port {port} OPEN{RESET}")
        s.close()
    print(f"{YELLOW} Done.{RESET}")

def check_site():
    url = input(f"{YELLOW} Website (google.com): {RESET}").strip()
    if not url.startswith("http"):
        url = "https://" + url
    try:
        r = requests.get(url, timeout=8)
        print(f"\n{CYAN} URL: {r.url}{RESET}")
        print(f" Status: {r.status_code}")
        print(f" Server: {r.headers.get('Server','Unknown')}")
    except Exception as e:
        print(f"{RED} Error: {e}{RESET}")

banner()
while True:
    print(f"\n{GREEN} [ MAIN MENU ]{RESET}")
    print("  1. 💉 Generate Strong Password")
    print("  2. 🔍 Check Password Strength")
    print("  3. 🌐 Scan My Local Ports")
    print("  4. 🛡️  Check Website Security")
    print("  5. 🚪 Exit")
    c = input(f"\n{YELLOW} Zohair > {RESET}")
    if c == '1':
        print(f"\n  {CYAN}Password: {GREEN}{gen_password()}{RESET}")
    elif c == '2':
        p = input("  Password: ")
        s = 0
        if len(p)>=8: s+=1
        if any(x.isupper() for x in p): s+=1
        if any(x