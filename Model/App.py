from Model import Summarizer
from Model.Web_scraper import NewsScraper


def fit(url):

    news = NewsScraper(url)
    result = {'author': news.get_author(), 'title': news.get_title(), 'article': news.get_article(),
              'publish date': news.get_publish_date(), 'summarizer': Summarizer.fit(news.get_article())}

    return result
