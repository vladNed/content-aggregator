import requests
from bs4 import BeautifulSoup

class TerminalScraper(object):

    def __init__(self, web_link=None):
        self.webpage = web_link    
        self.links, self.subtext = self.__scrape_webpage(self.webpage)
    
    def __scrape_webpage(self,default_link):
        exists_next_page = True
        counter = 1
        temp_links = []
        temp_subtext = []

        while exists_next_page:
            webpage = requests.get(default_link+str(counter))
            if counter == 5:
                exists_next_page = False
            else:
                soup = BeautifulSoup(webpage.text,'html.parser')
                for link,subtext in zip(soup.select('.storylink'),soup.select('.subtext')):
                    temp_links.append(link)
                    temp_subtext.append(subtext)
                
                counter += 1
        return (temp_links, temp_subtext)

    def filter_webpage(self):
        filtered_list = []
        for idx,item in enumerate(self.links):
            title = item.getText()
            href = item.get('href',None)
            vote = self.subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points','').strip())
                if points > 99:
                    filtered_list.append({
                        'title': title,
                        'link': href,
                        'votes': points
                    })
        return self.__sort_stories_by_votes(filtered_list)
    
    def __sort_stories_by_votes(self,hn_list):
        return sorted(hn_list, key = lambda k: k['votes'], reverse=True)


class IMDBScraper(object):

    def __init__(self):
        self.__imdb = 'https://www.imdb.com'
        self.__news_webpage = '/news/movie'
        self.webpager = requests.get('https://www.imdb.com/news/movie')
        self.__soup = BeautifulSoup(self.webpager.text,'html.parser')
        self.articles = self.__scrape_news()

    def __scrape_news(self):
        articles = []
        news = self.__soup.select('.news-article__title > a')
        date = self.__soup.select('.news-article__date')
        for idx, article in enumerate(news):
            articles.append({
                'title': article.getText(),
                'href': self.__imdb+article.get('href',None),
                'date': date[idx].getText()
            })
        return articles

    def refresh(self):
        self.articles = self.__scrape_news()