from django.shortcuts import render
from newsapi import NewsApiClient
# from django.template import context
# Create your views here.

def index(request): 
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')
    headLines = newsApi.get_top_headlines(sources = 'bbc-news,the-verge')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])

    mylist = zip(news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

    # return render(request, 'blog/index.html',
    #          context={'all_articles': all_articles, 'message': 'Write something!'})