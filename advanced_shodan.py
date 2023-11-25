import shodan
from colorama import Fore, Style
from termcolor import colored
import pyfiglet

shodan_api_key = ""  # Isi dengan kunci API Shodan Anda

# Fungsi untuk menampilkan banner program
def display_banner():
    banner = pyfiglet.figlet_format("RenaldY Project", font="slant")
    colored_banner = colored(banner, color="cyan")

    print(colored_banner)
    print(colored("Explore the world of connected devices and services with My Project", color="yellow"))
    print(colored("*" * 60, color="cyan"))
    print(colored("Create RenaldY(K1ngP1ng)", color="white"))
    print(colored("*" * 60, color="cyan"))
    print("\n")
    print(Fore.YELLOW + "1. Mencari Perusahaan ")
    print("2. Mencari IP ")
    print("3. Mencari Berdasarkan Kata Kunci")
    print("4. Mencari Berdasarkan Negara")
    print("5. Mencari Berdasarkan Port")
    print("6. Mencari Berdasarkan Hostname")
    print("7. Mencari Berdasarkan Kota")
    print("8. Mencari Berdasarkan Judul")
    print("9. Mencari Berdasarkan Nama Produk")
    print("\n")

# Fungsi untuk menampilkan detail host
def host_details(target):
    print(f"""
    IP: {target['ip_str']}
    Perusahaan: {target.get('org', 'n/a')}
    Sistem Operasi: {target.get('os', 'n/a')}
    """)

    for item in target['data']:
        print(f"""
        Port: {item['port']}
        Banner: {item['data']}
        """)

# Fungsi untuk menampilkan hasil pencarian
def display_search_result(index, host):
    ip_address = host['ip_str']
    port = host['port']
    hostname = host['hostnames']
    version = host.get('version', 'N/A')
    organization = host.get('org', 'N/A')
    info = host.get('info', 'N/A')
    os = host.get('os', 'N/A')
    product = host.get('product', 'N/A')
    tag = host.get("tag", "N/A")

    print(f"\n=== Result {index} ===")
    print(f"IP Address: {ip_address}")
    print(f"Port: {port}")
    print(f"Hostname: {hostname}")
    print(f"Version: {version}")
    print(f"Organization: {organization}")
    print(f"Info: {info}")
    print(f"Operating System: {os}")
    print(f"Produk: {product}")
    print(f"Tag: {tag}")

    print('-' * 50)

# Fungsi untuk melakukan pencarian menggunakan Shodan API
def shod():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        keyw = input("Masukan Kata Kunci : ")
        result = api.search(keyw)
        total_results = result['total']
        print(f"Result Found {total_results}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi untuk melakukan pencarian berdasarkan negara
def country_search():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        country_code = input("Masukan Kode Negara (Contoh: ID, US): ")
        result = api.search(f"country:{country_code}")
        total_results = result['total']
        print(f"Result Found {total_results}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi untuk melakukan pencarian berdasarkan nomor port
def port_search():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        port_num = input("Masukan Nomor Port: ")
        result = api.search(f"port:{port_num}")
        total_results = result['total']
        print(f"Result Found {total_results}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi untuk melakukan pencarian berdasarkan hostname
def hostname_search():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        hostname = input("Masukan Hostname: ")
        result = api.search(f"hostname:{hostname}")
        total_results = result['total']
        print(f"Result Found {total_results}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi untuk melakukan pencarian berdasarkan kota
def city_search():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        city_name = input("Masukan Nama Kota: ")
        result = api.search(f"city:{city_name}")
        total_results = result['total']
        print(f"Result Found {total_results}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi untuk melakukan pencarian berdasarkan judul
def title():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        print("Contoh masukan judul: 'hacked'/'donald trump'/'indonesia'/'login'")
        title_name = input("Masukan Title : ")
        result = api.search(f"title:{title_name}")
        total_result = result['total']
        print(f"Result Found {total_result}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi untuk melakukan pencarian berdasarkan nama perusahaan
def org():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        title_org = input("Masukan Nama Perusahaan: ")
        result = api.search(f"org:{title_org}")
        total_result = result['total']
        print(f"Result Found {total_result}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi untuk melakukan pencarian berdasarkan nama produk
def product():
    API_KEY = shodan_api_key
    api = shodan.Shodan(API_KEY)
    try:
        product = input("Masukan Nama Produk : ")
        result = api.search(f"product:{product}")
        total_result = result['total']
        print(f"Result Found {total_result}")

        for index, host in enumerate(result['matches'], start=1):
            display_search_result(index, host)

    except shodan.APIError as e:
        print(f"Fault {e}")

# Fungsi utama untuk menjalankan program
def main():
    display_banner()

    choices = input("Masukan Pilihanmu (1 - 9): ")
    choice = int(choices)

    if choice == 1:
        org()

    elif choice == 2:
        ip = input("Masukan IP : ")
        API_KEY = shodan_api_key
        api = shodan.Shodan(API_KEY)
        target = api.host(ip)
        host_details(target)

    elif choice == 3:
        shod()

    elif choice == 4:
        country_search()

    elif choice == 5:
        port_search()

    elif choice == 6:
        hostname_search()

    elif choice == 7:
        city_search()

    elif choice == 8:
        title()

    elif choice == 9:
        product()

    else:
        print("Pilihan tidak valid " + choices)


if __name__ == "__main__":
    main()
