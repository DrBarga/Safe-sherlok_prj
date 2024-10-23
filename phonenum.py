import phonenumbers
from phonenumbers import timezone
import requests
from bs4 import BeautifulSoup
import re

def phonenum(number):
    x = phonenumbers.parse(number)
    timeZone = timezone.time_zones_for_number(x)
    return (''.join(timeZone))

def lookup_phone_number(phone_number):
    # Поисковой запрос
    search_queries = [
        f"https://www.truecaller.com/search/in/{phone_number}",
        f"https://www.whitepages.com/phone/{phone_number}",
        f"https://www.anywho.com/phone/{phone_number}",
        f"https://www.whocallsme.com/Phone-Number/{phone_number}",
        f"https://www.spydialer.com/{phone_number}",
        f"https://www.zlookup.com/{phone_number}",
        f"https://www.numlookup.com/{phone_number}"
    ]

    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in search_queries:
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Попытка извлечение информации
            if "truecaller" in url:
                name = soup.find('span', class_='name')
                if name:
                    print(f"Truecaller: {name.text.strip()}")
                else:
                    print(f"Truecaller: Name doesn`t find.")

            elif "whitepages" in url:
                name = soup.find('h1', class_='name')
                if name:
                    print(f"Whitepages: {name.text.strip()}")
                else:
                    print(f"Whitepages: Name doesn`t find.")

            elif "anywho" in url:
                name = soup.find('div', class_='result-name')
                if name:
                    print(f"Anywho: {name.text.strip()}")
                else:
                    print(f"Anywho: Name doesn`t find.")

            elif "whocallsme" in url:
                name = soup.find('div', class_='user-name')
                if name:
                    print(f"WhoCallsMe: {name.text.strip()}")
                else:
                    print(f"WhoCallsMe: Name doesn`t find.")

            elif "spydialer" in url:
                name = soup.find('h1', class_='person-name')
                if name:
                    print(f"Spy Dialer: {name.text.strip()}")
                else:
                    print(f"Spy Dialer: Name doesn`t find")

            elif "zlookup" in url:
                name = soup.find('div', class_='name')
                if name:
                    print(f"ZLOOKUP: {name.text.strip()}")
                else:
                    print(f"ZLOOKUP: Name doesn`t find.")

            elif "numlookup" in url:
                name = soup.find('h2', class_='user-name')
                if name:
                    print(f"NumLookup: {name.text.strip()}")
                else:
                    print(f"NumLookup: Name doesn`t find.")

        except Exception as e:
            print(f"An error occurred with {url}: {str(e)}")