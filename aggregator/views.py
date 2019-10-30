from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from aggregator.Scraper import TerminalScraper, IMDBScraper, DevScraper


hnScraper = TerminalScraper('https://news.ycombinator.com/news?p=')
imdbScraper = IMDBScraper()
devScraper = DevScraper()

# Create your views here.
def terminal_home(request):
    context={
        'Movies': imdbScraper.articles[0],
        'HotNews': hnScraper.filter_webpage()[0]
    }
    return render(request, 'home.html', context=context)

def terminal_news(request):
    context = {
        'IMDBNews': imdbScraper.articles[:5],
        'HackerNews': hnScraper.filter_webpage()[:5],
        'DevNews': devScraper.scrape_news()[:5]
    }
    return render(request,'news.html',context=context)

def sign_in(request):
    return render(request,'sign-in.html')