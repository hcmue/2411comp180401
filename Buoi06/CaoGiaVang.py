import requests
from bs4 import BeautifulSoup

url = "https://giavang.pnj.com.vn/"


result = requests.get(url)
if result.status_code == 200:
    # print(result.content)
    soup = BeautifulSoup(result.content, 'html.parser')
    for m_cell in soup.find_all('td'):
        print(m_cell)
