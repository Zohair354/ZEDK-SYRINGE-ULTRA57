#!/usr/bin/env python3
# ============================================================
# ZEDK-ALPHA ULTRA PRO MAX
# Full Recon & Security Suite for Termux
# ALPHA SYSTEM build
# ============================================================

import os, sys, re, json, socket, ssl, hashlib, base64, urllib.parse
import subprocess, ipaddress, random, string, time, threading, csv
import urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

R='\033[1;31m'; G='\033[1;32m'; Y='\033[1;33m'; B='\033[1;34m'
C='\033[1;36m'; W='\033[1;37m'; N='\033[0m'

HOME = os.path.expanduser("~")
GOPATH = f"{HOME}/go/bin"
WORDLISTS = f"{HOME}/wordlists"
OUTDIR = f"{HOME}/zedk_out"
os.makedirs(OUTDIR, exist_ok=True)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
]

def clear(): os.system('clear' if os.name != 'nt' else 'cls')
def pause(): input(f"\n{Y}[Enter] للرجوع...{N}")
def ua(): return random.choice(USER_AGENTS)
def now(): return datetime.now().strftime("%Y%m%d_%H%M%S")

def banner():
    clear()
    print(f"""{C}
  ╔══════════════════════════════════════════════════════╗
  ║      ZEDK-ALPHA ULTRA  PRO MAX                       ║
  ║   Full Recon & Security Suite — Termux               ║
  ║           ALPHA SYSTEM build                         ║
  ╚══════════════════════════════════════════════════════╝
{N}""")

def sh(cmd, timeout=1800, silent=False, env=None):
    """Run shell command with extended environment."""
    e = os.environ.copy()
    e["PATH"] = GOPATH + ":" + e.get("PATH","")
    if env: e.update(env)
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True,
                          text=True, timeout=timeout, env=e)
        if not silent: print(r.stdout or r.stderr)
        return r.stdout
    except subprocess.TimeoutExpired:
        print(f"{R}[!] timeout ({timeout}s){N}"); return ""
    except Exception as ex:
        print(f"{R}[!] {ex}{N}"); return ""

def need(t):
    paths = [t, f"{GOPATH}/{t}"]
    for p in paths:
        if subprocess.run(['which',p],capture_output=True).returncode == 0:
            return p
    return None

def http_get(url, timeout=10, headers=None):
    h = {'User-Agent': ua()}
    if headers: h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, dict(r.headers), r.read().decode(errors='ignore')

def save_out(name, content):
    fn = f"{OUTDIR}/{name}_{now()}.txt"
    with open(fn, "w") as f: f.write(content)
    print(f"{G}[+] حفظ: {fn}{N}")
    return fn

# ============================================================
# 1) التشفير والترميز
# ============================================================

def gen_pass():
    ln = int(input("الطول [20]: ") or 20)
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    print(f"{G}{''.join(random.SystemRandom().choice(chars) for _ in range(ln))}{N}")

def pass_strength():
    p = input("كلمة المرور: "); s = 0
    if len(p) >= 12: s += 1
    if re.search(r'[a-z]',p): s += 1
    if re.search(r'[A-Z]',p): s += 1
    if re.search(r'\d',p): s += 1
    if re.search(r'[^A-Za-z0-9]',p): s += 1
    print(f"{Y}[{'█'*s}{'░'*(5-s)}] {['ضعيفة جداً','ضعيفة','متوسطة','جيدة','قوية','قوية جداً'][s]} ({s}/5){N}")
    if s < 4: print(f"{Y}[*] اقتراح: {''.join(random.SystemRandom().choice(string.ascii_letters+string.digits+'!@#$%^&*') for _ in range(20))}{N}")

def b64_op():
    c = input("1)ترميز 2)فك: "); t = input("النص: ")
    try:
        r = base64.b64encode(t.encode()).decode() if c=="1" else base64.b64decode(t).decode()
        print(f"{G}{r}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def b32_op():
    c = input("1)ترميز 2)فك: "); t = input("النص: ")
    try:
        r = base64.b32encode(t.encode()).decode() if c=="1" else base64.b32decode(t.upper()).decode()
        print(f"{G}{r}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def url_op():
    c = input("1)ترميز 2)فك: "); t = input("النص: ")
    print(f"{G}{urllib.parse.quote(t) if c=='1' else urllib.parse.unquote(t)}{N}")

MORSE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
'R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
'7':'--...','8':'---..','9':'----.'}

def morse_op():
    c = input("1)نص→مورس 2)مورس→نص: "); t = input("النص: ").upper()
    if c=="1": print(f"{G}{' '.join(MORSE.get(x,x) for x in t)}{N}")
    else:
        rv = {v:k for k,v in MORSE.items()}
        print(f"{G}{''.join(rv.get(x,x) for x in t.split())}{N}")

def text_hashes():
    t = input("النص: ").encode()
    for n,f in [("MD5",hashlib.md5),("SHA1",hashlib.sha1),("SHA256",hashlib.sha256),("SHA512",hashlib.sha512)]:
        print(f"{G}{n:7}: {f(t).hexdigest()}{N}")

def file_hashes():
    p = input("مسار الملف: ")
    try:
        with open(p,'rb') as f: d=f.read()
        print(f"{G}MD5    : {hashlib.md5(d).hexdigest()}{N}")
        print(f"{G}SHA1   : {hashlib.sha1(d).hexdigest()}{N}")
        print(f"{G}SHA256 : {hashlib.sha256(d).hexdigest()}{N}")
    except FileNotFoundError: print(f"{R}[!] غير موجود{N}")

def jwt_decode():
    t = input("JWT: ").strip().split('.')
    for i,p in enumerate(t[:2]):
        try:
            pad = p + '=' * (-len(p) % 4)
            print(f"{G}{['Header','Payload'][i]}: {base64.urlsafe_b64decode(pad).decode()}{N}")
        except Exception as e: print(f"{R}[!] {e}{N}")

def hash_id():
    h = input("Hash: ").strip()
    pats = [(r'^[a-f0-9]{32}$','MD5'),(r'^[a-f0-9]{40}$','SHA1'),
            (r'^[a-f0-9]{64}$','SHA256'),(r'^[a-f0-9]{128}$','SHA512'),
            (r'^\$2[aby]\$','bcrypt'),(r'^\$5\$','SHA256-crypt'),(r'^\$6\$','SHA512-crypt'),
            (r'^[a-f0-9]{16}$','MySQL/MariaDB'),(r'^\$argon2','Argon2')]
    for pat,name in pats:
        if re.match(pat,h,re.I): print(f"{G}{name}{N}"); return
    print(f"{Y}غير معروف{N}")

def cookie_decode():
    t = input("Cookie (URL-encoded): ")
    print(f"{G}{urllib.parse.unquote(t)}{N}")

def ip_calc():
    t = input("CIDR: ")
    try:
        net = ipaddress.ip_network(t, strict=False)
        hosts = list(net.hosts())
        print(f"{G}Network  : {net.network_address}{N}")
        print(f"{G}Broadcast: {net.broadcast_address}{N}")
        print(f"{G}Netmask  : {net.netmask}{N}")
        print(f"{G}Hosts    : {net.num_addresses - 2}{N}")
        if hosts:
            print(f"{G}First    : {hosts[0]}{N}")
            print(f"{G}Last     : {hosts[-1]}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def text_to_bin():
    t = input("النص: ")
    print(f"{G}Bin : {' '.join(format(ord(c),'08b') for c in t)}{N}")
    print(f"{G}Hex : {t.encode().hex()}{N}")

# ============================================================
# 2) محرك فحص المنافذ المتوازي
# ============================================================

def _probe(host, port, timeout=0.4):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try: return port if s.connect_ex((host, port))==0 else None
    except: return None
    finally: s.close()

def scan_ports_fast():
    host = input("الهدف: ")
    rng = input("المدى [1-1000]: ") or "1-1000"
    th = int(input("threads [300]: ") or 300)
    a, b = map(int, rng.split('-'))
    print(f"{Y}[*] فحص {host} [{a}-{b}] بـ {th} threads...{N}")
    t0 = time.time(); opens = []
    with ThreadPoolExecutor(max_workers=th) as ex:
        for f in as_completed([ex.submit(_probe, host, p) for p in range(a, b+1)]):
            r = f.result()
            if r: opens.append(r); print(f"{G}[+] {r}{N}")
    print(f"{G}[+] {len(opens)} مفتوح في {int(time.time()-t0)}s{N}")
    if opens: save_out("ports", f"{host}\n" + "\n".join(map(str, opens)))

def scan_top1000():
    host = input("الهدف: ")
    nm = need("nmap")
    if nm:
        out = sh(f"{nm} -sS -T4 --top-ports 1000 {host}")
        save_out("nmap_top1000", out)
    else:
        common = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,
                  1723,3306,3389,5900,8080,8443,8888,9000,9200,27017]
        for p in common:
            if _probe(host, p): print(f"{G}[+] {p}{N}")

def tcp_ping():
    host = input("الهدف: ")
    for p in [80,443,22,21,25,8080,3306]:
        r = _probe(host, p)
        print(f"{G if r else R}[{'OPEN' if r else 'closed'}] {host}:{p}{N}")

def ping_icmp():
    h = input("الهدف [1.1.1.1]: ") or "1.1.1.1"
    os.system(f"ping -c 4 {h}")

def dns_lookup():
    try: print(f"{G}{socket.gethostbyname(input('الدومين: '))}{N}")
    except: print(f"{R}[!] فشل{N}")

def reverse_dns():
    try: print(f"{G}{socket.gethostbyaddr(input('IP: '))[0]}{N}")
    except: print(f"{R}[!] لا rDNS{N}")

def whois_lookup():
    d = input("الدومين/IP: ")
    w = need("whois")
    if w: sh(f"{w} {d} | head -50")
    else: print(f"{R}[!] pkg install whois{N}")

def dns_full():
    d = input("الدومين: ")
    for rt in ['A','AAAA','MX','NS','TXT','CNAME','SOA']:
        out = subprocess.run(['dig','+short',rt,d],capture_output=True,text=True,timeout=10).stdout.strip()
        if out: print(f"{G}{rt:6}: {out}{N}")

def geo_ip():
    ip = input("IP (فارغ=عنوانك): ") or ""
    try:
        _,_,body = http_get(f"http://ip-api.com/json/{ip}?fields=66846719")
        d = json.loads(body)
        for k in ['query','country','regionName','city','zip','lat','lon','timezone','isp','org','as']:
            if k in d and d[k]: print(f"{G}{k:10}: {d[k]}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

# ============================================================
# 3) فحص الويب
# ============================================================

def site_status():
    u = input("URL: ")
    if not u.startswith("http"): u = "https://"+u
    try:
        t = time.time()
        s, h, _ = http_get(u, timeout=15)
        print(f"{G}Status : {s}{N}")
        print(f"{G}Time   : {int((time.time()-t)*1000)} ms{N}")
        for k in ['Server','Content-Type','Content-Length','X-Powered-By']:
            if k in h: print(f"{G}{k}: {h[k]}{N}")
    except urllib.error.HTTPError as e: print(f"{Y}HTTP {e.code}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def http_headers():
    u = input("URL: ")
    if not u.startswith("http"): u = "http://"+u
    try:
        _,h,_ = http_get(u)
        for k,v in h.items(): print(f"{G}{k}: {v}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def http_methods():
    u = input("URL: ")
    if not u.startswith("http"): u = "http://"+u
    for m in ["GET","POST","PUT","DELETE","OPTIONS","HEAD","PATCH","TRACE"]:
        try:
            req = urllib.request.Request(u, method=m, headers={'User-Agent':ua()})
            with urllib.request.urlopen(req, timeout=5) as r:
                print(f"{G}[{r.status}] {m}{N}")
        except urllib.error.HTTPError as e: print(f"{Y}[{e.code}] {m}{N}")
        except: print(f"{R}[ERR] {m}{N}")

def ssl_cert():
    h = input("Host: ")
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((h,443),timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=h) as ss:
                cert = ss.getpeercert()
        for k,v in cert.items(): print(f"{G}{k}: {v}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def sec_headers():
    u = input("URL: ")
    if not u.startswith("http"): u = "https://"+u
    checks = ['Strict-Transport-Security','Content-Security-Policy','X-Frame-Options',
              'X-Content-Type-Options','Referrer-Policy','Permissions-Policy',
              'X-XSS-Protection','Cross-Origin-Opener-Policy']
    try:
        _,h,_ = http_get(u)
        hl = {k.lower():v for k,v in h.items()}
        for c in checks:
            print(f"{G if c.lower() in hl else R}[{'OK' if c.lower() in hl else 'MISSING'}] {c}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def extract_links():
    u = input("URL: ")
    if not u.startswith("http"): u = "https://"+u
    try:
        _,_,html = http_get(u)
        links = set(re.findall(r'href=["\']([^"\']+)["\']', html))
        for l in sorted(links): print(f"{G}{l}{N}")
        if links: save_out("links", "\n".join(links))
    except Exception as e: print(f"{R}[!] {e}{N}")

def extract_emails():
    u = input("URL: ")
    if not u.startswith("http"): u = "https://"+u
    try:
        _,_,html = http_get(u)
        emails = set(re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', html))
        for e in emails: print(f"{G}{e}{N}")
        if emails: save_out("emails", "\n".join(emails))
    except Exception as e: print(f"{R}[!] {e}{N}")

def robots():
    d = input("الدومين: ")
    if not d.startswith("http"): d = "https://"+d
    try:
        _,_,body = http_get(d.rstrip('/')+"/robots.txt")
        print(f"{G}{body[:3000]}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def sitemap():
    d = input("الدومين: ")
    if not d.startswith("http"): d = "https://"+d
    try:
        _,_,body = http_get(d.rstrip('/')+"/sitemap.xml")
        print(f"{G}{body[:3000]}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def pwn_check():
    pwd = input("كلمة المرور (يُرسل أول 5 حروف): ")
    sha = hashlib.sha1(pwd.encode()).hexdigest().upper()
    try:
        _,_,body = http_get(f"https://api.pwnedpasswords.com/range/{sha[:5]}")
        hits = [l for l in body.splitlines() if l.startswith(sha[5:])]
        if hits: print(f"{R}[!] مسربة — {hits[0].split(':')[1]} مرة{N}")
        else: print(f"{G}[+] غير مسربة{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

# ============================================================
# 4) OSINT موسّع
# ============================================================

def username_enum():
    u = input("Username: ").strip()
    sites = {
        "GitHub": f"https://github.com/{u}",
        "Twitter/X": f"https://x.com/{u}",
        "Instagram": f"https://instagram.com/{u}",
        "Reddit": f"https://reddit.com/user/{u}",
        "TikTok": f"https://tiktok.com/@{u}",
        "Telegram": f"https://t.me/{u}",
        "Medium": f"https://medium.com/@{u}",
        "Pinterest": f"https://pinterest.com/{u}",
        "Twitch": f"https://twitch.tv/{u}",
        "YouTube": f"https://youtube.com/@{u}",
        "Facebook": f"https://facebook.com/{u}",
        "Snapchat": f"https://snapchat.com/add/{u}",
    }
    print(f"{Y}[*] فحص {len(sites)} منصة...{N}")
    def check(item):
        name, url = item
        try:
            s,_,_ = http_get(url, timeout=6)
            return (name, url, s)
        except urllib.error.HTTPError as e: return (name, url, e.code)
        except: return (name, url, 0)
    with ThreadPoolExecutor(max_workers=10) as ex:
        for name, url, code in ex.map(check, sites.items()):
            c = G if code==200 else Y if code in (301,302) else R
            print(f"{c}[{code}] {name}: {url}{N}")

def email_intel():
    e = input("الإيميل: ").strip().lower()
    h = hashlib.md5(e.encode()).hexdigest()
    print(f"{G}MD5      : {h}{N}")
    print(f"{G}Gravatar : https://www.gravatar.com/avatar/{h}{N}")
    print(f"{G}HIBP     : https://haveibeenpwned.com/account/{e}{N}")

def reverse_ip():
    ip = input("IP: ")
    try:
        _,_,body = http_get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
        print(f"{G}{body[:2000]}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def wayback():
    d = input("الدومين: ")
    try:
        _,_,body = http_get(f"http://web.archive.org/cdx/search/cdx?url={d}/*&output=text&limit=100&collapse=urlkey")
        print(f"{G}{body[:3000]}{N}")
        if body: save_out("wayback", body)
    except Exception as e: print(f"{R}[!] {e}{N}")

def subdomain_passive():                                    # crt.sh (passive)
    d = input("الدومين: ")
    try:
        _,_,body = http_get(f"https://crt.sh/?q=%25.{d}&output=json")
        subs = set()
        for item in json.loads(body):
            for n in item.get('name_value','').split('\n'):
                subs.add(n.strip())
        for s in sorted(subs): print(f"{G}{s}{N}")
        if subs: save_out("crtsh_subs", "\n".join(subs))
    except Exception as e: print(f"{R}[!] {e}{N}")

def mac_lookup():
    m = input("MAC: ").upper().replace(':','').replace('-','')[:6]
    try:
        _,_,body = http_get(f"https://api.macvendors.com/{m}")
        print(f"{G}{body}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def expand_url():
    try:
        req = urllib.request.Request(input("URL مختصر: "), headers={'User-Agent':ua()})
        with urllib.request.urlopen(req, timeout=15) as r:
            print(f"{G}Final: {r.url}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

def tor_check():
    try:
        _,_,body = http_get("https://check.torproject.org/api/ip")
        print(f"{G}{json.loads(body)}{N}")
    except Exception as e: print(f"{R}[!] {e}{N}")

# ============================================================
# 5) أدوات ProjectDiscovery (Pro Max core)
# ============================================================

def pro_subfinder():
    d = input("الدومين: ")
    t = need("subfinder")
    if not t: print(f"{R}[!] شغّل install.sh{N}"); return
    print(f"{Y}[*] subfinder على {d}...{N}")
    out = sh(f"{t} -d {d} -silent -all", timeout=600)
    if out: save_out("subfinder", out)

def pro_httpx():
    print(f"{Y}[*] الصق hosts (سطر فارغ للإنهاء):{N}")
    hs = []
    while True:
        h = input().strip()
        if not h: break
        hs.append(h)
    if not hs: return
    tmp = f"/tmp/_hosts_{now()}.txt"
    with open(tmp,"w") as f: f.write("\n".join(hs))
    t = need("httpx")
    if not t: print(f"{R}[!] شغّل install.sh{N}"); return
    out = sh(f"{t} -l {tmp} -silent -title -tech-detect -status-code -follow-redirects", timeout=900)
    if out: save_out("httpx", out)

def pro_nuclei():
    u = input("URL: ")
    tag = input("tags [cves,misconfig,exposures,takeovers]: ") or "cves,misconfig,exposures,takeovers"
    sev = input("severity [low,medium,high,critical]: ") or "low,medium,high,critical"
    t = need("nuclei")
    if not t: print(f"{R}[!] شغّل install.sh{N}"); return
    print(f"{Y}[*] nuclei على {u}...{N}")
    out = sh(f"{t} -u {u} -tags {tag} -severity {sev} -silent -stats", timeout=1800)
    if out: save_out("nuclei", out)

def pro_katana():
    u = input("URL: ")
    depth = input("depth [3]: ") or "3"
    t = need("katana")
    if not t: print(f"{R}[!] شغّل install.sh{N}"); return
    out = sh(f"{t} -u {u} -silent -d {depth} -jc -kf all", timeout=900)
    if out: save_out("katana", out)

def pro_ffuf():
    u = input("URL (ضع FUZZ مكان الكلمة): ") or "http://target/FUZZ"
    wl = input(f"Wordlist [{WORDLISTS}/common.txt]: ") or f"{WORDLISTS}/common.txt"
    t = need("ffuf")
    if not t: print(f"{R}[!] شغّل install.sh{N}"); return
    out = sh(f"{t} -u {u} -w {wl} -mc 200,204,301,302,307,401,403,405 -t 50 -s", timeout=1800)
    if out: save_out("ffuf", out)

def pro_dnsx():
    print(f"{Y}[*] الصق subdomains (سطر فارغ للإنهاء):{N}")
    subs = []
    while True:
        s = input().strip()
        if not s: break
        subs.append(s)
    if not subs: return
    tmp = f"/tmp/_subs_{now()}.txt"
    with open(tmp,"w") as f: f.write("\n".join(subs))
    t = need("dnsx")
    if not t: print(f"{R}[!] شغّل install.sh{N}"); return
    out = sh(f"{t} -l {tmp} -silent -a -resp", timeout=600)
    if out: save_out("dnsx", out)

# ============================================================
# 6) Pipeline — full recon على دومين
# ============================================================

def pipeline_full():
    print(f"{C}=== PIPELINE كامل: subfinder → httpx → nuclei ==={N}")
    d = input("الدومين: ")
    sf = need("subfinder"); hx = need("httpx"); nc = need("nuclei")
    if not sf or not hx:
        print(f"{R}[!] شغّل install.sh أولاً{N}"); return
    ts = now()
    print(f"{Y}[1/3] subfinder...{N}")
    subs = sh(f"{sf} -d {d} -silent", timeout=600)
    subs_file = f"{OUTDIR}/pipeline_subs_{ts}.txt"
    with open(subs_file,"w") as f: f.write(subs)
    print(f"{G}[+] {len(subs.splitlines())} subdomain → {subs_file}{N}")

    print(f"{Y}[2/3] httpx — probing...{N}")
    live = sh(f"{hx} -l {subs_file} -silent -title -tech-detect -status-code", timeout=900)
    live_file = f"{OUTDIR}/pipeline_live_{ts}.txt"
    with open(live_file,"w") as f: f.write(live)
    print(f"{G}[+] {len(live.splitlines())} host حي → {live_file}{N}")

    if nc:
        print(f"{Y}[3/3] nuclei — فحص ثغرات (قد يأخذ وقت)...{N}")
        urls = [l.split()[0] for l in live.splitlines() if l.strip()]
        if urls:
            tmp = f"{OUTDIR}/_urls_{ts}.txt"
            with open(tmp,"w") as f: f.write("\n".join(urls))
            out = sh(f"{nc} -l {tmp} -silent -severity medium,high,critical", timeout=2400)
            if out: save_out("nuclei_pipeline", out)

# ============================================================
# 7) Wordlist manager
# ============================================================

def gen_wordlist():
    print(f"{Y}[*] يولّد wordlist مخصص{N}")
    base = input("كلمات (فاصلة): ").split(',')
    years = [str(y) for y in range(1990, 2026)]
    syms = ['', '!', '@', '#', '123', '1234', '2024', '2025']
    out = f"{OUTDIR}/wordlist_custom_{now()}.txt"
    n = 0
    with open(out, "w") as f:
        for b in base:
            b = b.strip()
            if not b: continue
            for y in years: f.write(f"{b}{y}\n"); n += 1
            for s in syms: f.write(f"{b}{s}\n"); n += 1
            f.write(f"{b.capitalize()}\n"); n += 1
            f.write(f"{b.upper()}\n"); n += 1
    print(f"{G}[+] {n} كلمة → {out}{N}")

# ============================================================
# القائمة — 6 أقسام
# ============================================================

def _simple(fn):
    return fn

SECTIONS = [
    ("التشفير والترميز", [
        ("1",  "GEN",  "توليد كلمة مرور",         gen_pass),
        ("2",  "STR",  "فحص قوة كلمة مرور",       pass_strength),
        ("3",  "B64",  "Base64",                  b64_op),
        ("4",  "B32",  "Base32",                  b32_op),
        ("5",  "URL",  "URL encode/decode",       url_op),
        ("6",  "MOR",  "Morse",                   morse_op),
        ("7",  "HID",  "تجزئة نص",                text_hashes),
        ("8",  "FH",   "تجزئة ملف",               file_hashes),
        ("9",  "JWT",  "فك JWT",                  jwt_decode),
        ("10", "HT",   "معرّف نوع Hash",          hash_id),
        ("11", "CKI",  "فك Cookie",               cookie_decode),
        ("12", "IPC",  "حاسبة CIDR",              ip_calc),
        ("13", "BIN",  "نص → bin/hex",            text_to_bin),
    ]),
    ("الشبكة", [
        ("14", "SCAN", "منافذ (متوازي)",           scan_ports_fast),
        ("15", "SCF",  "Top 1000 (nmap)",          scan_top1000),
        ("16", "PING", "TCP ping",                 tcp_ping),
        ("17", "IPNG", "ICMP ping",                ping_icmp),
        ("18", "DNS",  "DNS lookup",               dns_lookup),
        ("19", "RDNS", "Reverse DNS",              reverse_dns),
        ("20", "DNSR", "سجلات DNS كاملة",          dns_full),
        ("21", "WHO",  "Whois",                    whois_lookup),
        ("22", "GEO",  "GeoIP (ip-api)",           geo_ip),
    ]),
    ("فحص الويب", [
        ("23", "SITE", "حالة الموقع",              site_status),
        ("24", "HDR",  "ترويسات HTTP",             http_headers),
        ("25", "METH", "طرق HTTP",                 http_methods),
        ("26", "SSL",  "شهادة SSL",                ssl_cert),
        ("27", "SECH", "ترويسات الأمان",           sec_headers),
        ("28", "LINK", "استخراج روابط",            extract_links),
        ("29", "EML",  "استخراج إيميلات",          extract_emails),
        ("30", "ROB",  "robots.txt",               robots),
        ("31", "MAP",  "sitemap.xml",              sitemap),
        ("32", "PWN",  "HIBP تسريب",               pwn_check),
    ]),
    ("OSINT", [
        ("33", "USR",  "username على منصات",       username_enum),
        ("34", "EMI",  "إيميل intel",              email_intel),
        ("35", "REV",  "reverse IP → domains",     reverse_ip),
        ("36", "WAY",  "Wayback Machine",          wayback),
        ("37", "CRT",  "subdomains (crt.sh)",      subdomain_passive),
        ("38", "MAC",  "مصنع MAC",                 mac_lookup),
        ("39", "EXP",  "توسيع رابط مختصر",         expand_url),
        ("40", "TOR",  "كشف Tor",                  tor_check),
    ]),
    ("ProjectDiscovery (Pro)", [
        ("41", "SUBF", "subfinder",                pro_subfinder),
        ("42", "HTX",  "httpx probing",            pro_httpx),
        ("43", "NUC",  "nuclei vuln scan",         pro_nuclei),
        ("44", "KAT",  "katana crawler",           pro_katana),
        ("45", "FFU",  "ffuf fuzzing",             pro_ffuf),
        ("46", "DNX",  "dnsx mass resolve",        pro_dnsx),
        ("47", "PIPE", "Pipeline كامل",            pipeline_full),
    ]),
    ("Wordlists", [
        ("48", "WGN",  "توليد wordlist مخصص",      gen_wordlist),
    ]),
]

ALL = [(int(c), s, d, f) for _, tools in SECTIONS for c, s, d, f in tools]

def show_menu():
    banner()
    print(f"{W}  ZEDK-ALPHA ULTRA PRO MAX — {len(ALL)} أداة في 6 أقسام{N}\n")
    for name, tools in SECTIONS:
        print(f"{C}┌─ {name} ─────────────────────────────────{N}")
        for c, s, d, _ in tools:
            print(f"{C}│{N} {Y}{c:>2}){N} {W}{s:<5}{N} {d}")
        print(f"{C}└──────────────────────────────────────────{N}")
    print(f"\n  {Y} 0){N} خروج")
    print(f"  {Y}h){N} سجل النتائج ({OUTDIR})")

def main():
    while True:
        show_menu()
        c = input(f"\n{Y}>>> {N}").strip().lower()
        if c == "0":
            print(f"{G}caw. roost stays warm.{N}"); break
        if c == "h":
            print(f"{G}{OUTDIR}:{N}")
            os.system(f"ls -la {OUTDIR}")
            pause(); continue
        try:
            i = int(c)
            for num, short, desc, fn in ALL:
                if num == i:
                    banner()
                    print(f"{W}=== [{num}] {short} — {desc} ==={N}\n")
                    try: fn()
                    except KeyboardInterrupt: print(f"\n{Y}[*] أُلغي{N}")
                    except Exception as e: print(f"{R}[!] {e}{N}")
                    pause(); break
        except ValueError:
            pass

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print(f"\n{G}caw.{N}")