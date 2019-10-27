from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from aggregator.Scraper import TerminalScraper, IMDBScraper


hnScraper = TerminalScraper('https://news.ycombinator.com/news?p=')
imbdScraper = IMDBScraper()

# Create your views here.
def meister_home(request):
    context = {
        'IMBDNews': imbdScraper.articles[:5],
        'HackerNews': hnScraper.filter_webpage()[:5]
    }
    return render(request, 'news.html',context=context)
