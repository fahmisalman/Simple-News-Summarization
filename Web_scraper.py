from newspaper import Article


def get_article(url):

    article = Article(url, language='id')
    article.download()
    article.parse()

    return article.text
