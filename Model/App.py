from Model import Summarizer
from Model.Web_scraper import NewsScraper


def fit(url):

    news = NewsScraper(url)
    result = {}

    result['author'] = news.get_author()
    result['title'] = news.get_title()
    result['article'] = news.get_article()
    result['publish date'] = news.get_publish_date()
    result['summarizer'] = Summarizer.fit(news.get_article())

    return result
