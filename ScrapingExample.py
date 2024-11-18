from pip._vendor import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

print(r)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='article-page_flex')

#print(s)

content = s.find_all('p')

print(content)