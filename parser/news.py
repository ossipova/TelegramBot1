import requests
from bs4 import BeautifulSoup
from pprint import pprint


class ParserNews():
    __URL = "https://www.securitylab.ru/news/"
    __HEADERS = {
        'Accept': "ext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
    }

    @classmethod
    def __get_html(cls, url):
        req = requests.get(url, headers=cls.__HEADERS)
        return req

    @staticmethod
    def __get_data(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('a', class_='article-card inline-card')
        news = []
        for item in items:
            card = {
                'title': item.find('h2', class_='article-card-title').string,
                'dop': item.find('p').string,
                'link': "https://securitylab.ru" + item.get("href"),
                'time': item.find('time').string.split('/')[0],
                'date': item.find('time').string.split('/')[1],
            }
            news.append(card)
        return news

    @classmethod
    def parser(cls):
        html = cls.__get_html(cls.__URL)
        if html.status_code == 200:
            news = []
            for i in range(1, 2):
                html = cls.__get_html(cls.__URL + f"page1_{i}.php")
                current_page = cls.__get_data(html.text)
                news.extend(current_page)
            return news
        else:
            raise Exception('Bad request in parser!')


#pprint(parser())
# The end
