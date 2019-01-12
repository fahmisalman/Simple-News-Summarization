from newspaper import Article


class NewsScraper(object):

    def __init__(self, url):
        self.article = Article(url, language='id')
        self.article.download()
        self.article.parse()

    def get_article(self):
        return self.article.text

    def get_author(self):
        return self.article.authors

    def get_title(self):
        return self.article.title

    def get_publish_date(self):
        return self.article.publish_date

    def get_top_image(self):
        return self.article.top_image


