import bs4
import requests
from bs4 import BeautifulSoup

url ="https://www.baidu.com/"
head = {
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
}
response = requests.get(url, headers=head)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
hotSearch = soup.find_all('span', class_='title-content-title')
#print(hotSearch.text)

for i in hotSearch:
    print(i.text)