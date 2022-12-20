import requests as rq
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.vedomosti.ru/ecology"
main_page = rq.get(url)
print(main_page)

soup = BeautifulSoup(main_page.text, features="html.parser")
print(soup.prettify())

urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))

new_urls = []
for link in soup.find_all('a'):
  if 'release' in link.get('href') and link.get('href') not in new_urls:
    new_urls.append(link.get('href'))

full_urls = []
for i in new_urls:
  full_urls.append(f'https://www.vedomosti.ru{i}')

for link in full_urls:
  url0 = full_urls[0]
  page0 = rq.get(url0)
  soup0 = BeautifulSoup(page0.text, features="html.parser")

for link in full_urls:
  url1 = full_urls[1]
  page1 = rq.get(url1)
  soup1 = BeautifulSoup(page1.text, features="html.parser")

for link in full_urls:
  url2 = full_urls[2]
  page2 = rq.get(url2)
  soup2 = BeautifulSoup(page2.text, features="html.parser")

for link in full_urls:
  url3 = full_urls[3]
  page3 = rq.get(url3)
  soup3 = BeautifulSoup(page3.text, features="html.parser")

articles0 = []
for link in soup0.find_all('a', href=True):
  if 'articles' in link.get('href') or 'columns' in link.get('href') and link.get('href') not in articles0:
      articles0.append(link.get('href'))

articles1 = []
for link in soup1.find_all('a', href=True):
  if 'articles' in link.get('href') or 'columns' in link.get('href') and link.get('href') not in articles1:
      articles1.append(link.get('href'))

articles2 = []
for link in soup2.find_all('a', href=True):
  if 'articles' in link.get('href') or 'columns' in link.get('href') and link.get('href') not in articles2:
      articles2.append(link.get('href'))

articles3 = []
for link in soup3.find_all('a', href=True):
  if 'articles' in link.get('href') or 'columns' in link.get('href') and link.get('href') not in articles3:
      articles3.append(link.get('href'))

all_articles = []
all_articles.extend(articles0)
all_articles.extend(articles1)
all_articles.extend(articles2)
all_articles.extend(articles3)

full_artricles = []
for i in all_articles:
  full_artricles.append(f'https://www.vedomosti.ru{i}')

for link in full_artricles:
  url_0 = full_artricles[0]
  page_0 = rq.get(url_0)
  soup_0 = BeautifulSoup(page_0.text, features="html.parser")

script = soup_0.find_all('script')[1]
data = json.loads(script.get_text())
title = data["name"]
date = data["datePublished"][:10]

text_list = soup_0.find_all('p', {'class' : 'box-paragraph__text'})
text = []
for i in text_list:
  text.append(i.text)
final_text = ' '.join(text)

def News(url_0):
  page_0 = rq.get(url_0)
  soup_0 = BeautifulSoup(page_0.text, features="html.parser")
  script = soup_0.find_all('script')[1]
  data = json.loads(script.get_text())
  title = data["name"]
  date = data["datePublished"][:10]
  text_list = soup_0.find_all('p', {'class' : 'box-paragraph__text'})
  text = []
  for i in text_list:
    text.append(i.text)
  final_text = ' '.join(text)
  return url_0, title, date, final_text

all_news = []
for link in full_artricles:
  new = News(link)
  all_news.append(new)

df = pd.DataFrame(all_news)
df.columns = ['link', 'title', 'date', 'text']
df.to_excel('ecology_news.xlsx')