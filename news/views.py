from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article


def article(request):
    article = Article.objects.get(id = article_id)
    return render(request, "all_news/article.html", {"article":article})

def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_article = Article.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'all_news/search.html', {"message":message, "articles":searched_article})
    else:
        message = 'You haven\'t searched for any article.'
        return render(request, 'all_news/search.html', {"message":message})


def past_days_news(request, past_date):
    try:
        """Converts data from the string url"""
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        """Raise 404 error when ValueError is thrown"""
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)
    news = Article.days_news(date)

    return render(request, 'all-news/past_news.html', {"date": date, "news":news})

def news_today(request):
    news = Article.todays_news()
    date = dt.date.today()
    return render(request, 'all_news/today_news.html', {'date':date,"news":news})
