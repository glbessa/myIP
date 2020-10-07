import re
import requests
from bs4 import BeautifulSoup

custom_headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
}

r = requests.Session()

response = r.get('http://www.meuip.com.br/', headers=custom_headers)

soup = BeautifulSoup(response.content, 'html.parser')

ip = soup.find('h3', class_='m-0 font-weight-bold')
#reverse_ip = soup.find('div', class_='card-body text-center').get_text()
reverse_ip = soup.find(string=re.compile('IP Reverso'))

print(f'IP: {ip.get_text().strip()[9:]}')
print(f'Reverse IP: {reverse_ip.strip()[11:]}')
