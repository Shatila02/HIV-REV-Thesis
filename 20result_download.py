
from bs4 import BeautifulSoup as bs
import requests
Domain = 'https://biosig.lab.uq.edu.au'
URL = 'https://biosig.lab.uq.edu.au/dynamut/single_results/169068879768/T34A'
FILETYPE ='.pse'

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

for link in get_soup(URL).find_all('a'):
    pse_link = link.get('href')
    if FILETYPE in pse_link:
        print(pse_link)
        with open(link.text, 'wb') as file:
            response = requests.get(Domain + pse_link)
            file.write(response.content)