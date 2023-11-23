import shodan

# Setup API
api_key = 'API KEY'  # Gantilah dengan kunci API Shodan Anda sendiri.
api = shodan.Shodan(api_key)

# Melakukan QUery
query = input("Masukan Query : ")
result = api.search(query)

# Print Hasil
for service in result['matches']:
    ip = service['ip_str']
    domains = service.get('domain', [])
    version = service.get('versi', '')
    open_ports = service.get('port', [])

    print(f"IP: {ip}, Domain: {', '.join(domains)}, Versi: {version}, Open Ports: {len(open_ports)}")
