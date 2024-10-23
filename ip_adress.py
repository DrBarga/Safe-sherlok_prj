import requests


def get_ip_info(ip_address):
    try:
        # Запрос к ipinfo.io для получение информации об IP
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(f"IP address: {data.get('ip')}")
            print(f"City: {data.get('city')}")
            print(f"region: {data.get('region')}")
            print(f"Country: {data.get('country')}")
            print(f"provider: {data.get('org')}")
            print(f"Latitude Longitude: {data.get('loc')}")
        else:
            print("Failed to obtain information about IP.")
    except Exception as e:
        print("An error was occupted:", str(e))