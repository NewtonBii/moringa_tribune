from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Article, NewsLetterRecipients
from .forms import NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/accounts/login')
def article(request, article_id):
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
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(request, 'all_news/today_news.html', {'date':date,"news":news, 'letterForm':form})
