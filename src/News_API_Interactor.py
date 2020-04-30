from configparser import ConfigParser
from newsapi import NewsApiClient
from datetime import datetime


class News:
    def __init__(self, api_key):
        self.newsapi = NewsApiClient(api_key=api_key)

    def top_headlines(self, country='in', query='', category='', page_size=5):
        top_headlines = self.newsapi.get_top_headlines(q=query, country=country, page_size=page_size)
        headlines = list()
        for article in top_headlines['articles']:
            headlines.append(article['title'] + '|' + article['url'])
        return f"1. {headlines[0].split('|')[0]} - {headlines[0].split('|')[1]} \n" \
               f"2. {headlines[1].split('|')[0]} - {headlines[1].split('|')[1]} \n" \
               f"3. {headlines[2].split('|')[0]} - {headlines[2].split('|')[1]} \n" \
               f"4. {headlines[3].split('|')[0]} - {headlines[3].split('|')[1]} \n" \
               f"5. {headlines[4].split('|')[0]} - {headlines[4].split('|')[1]} \n"


    def all_headlines(self, query='generic', page_size=5,
                      start_date=datetime.now().date(), end_date=datetime.now().date()):
        top_headlines = self.newsapi.get_everything(q=query, page_size=page_size, from_param=start_date, to=end_date)
        print(top_headlines)


if __name__ == '__main__':
    config_obj = ConfigParser()
    config_obj.read('config.ini')
    api_key = config_obj.get("News_Credentials", "API_Key")
    obj = News(api_key)
    print(obj.top_headlines())
    obj.all_headlines()

