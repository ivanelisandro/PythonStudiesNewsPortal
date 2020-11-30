from django.conf import settings
from django.http import HttpResponse, Http404
from django.views import View
from django.shortcuts import render
from datetime import datetime
from collections import OrderedDict
import json

_date_groups = {}
_articles = {}

with open(settings.NEWS_JSON_PATH) as news_file:
    _news = json.load(news_file)
    for article in _news:
        _articles[article["link"]] = article
        date = datetime.strptime(article["created"], '%Y-%m-%d %H:%M:%S').date()
        if str(date) not in _date_groups.keys():
            _date_groups[str(date)] = {}
        _date_groups[str(date)]["date"] = date
        if "articles" not in _date_groups[str(date)].keys():
            _date_groups[str(date)]["articles"] = []
        _date_groups[str(date)]["articles"].append(article)


class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")


class NewsView(View):
    def get(self, request, *args, **kwargs):
        ordered = OrderedDict(sorted(
            _date_groups.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=True))

        context = {"groups": ordered.values()}
        return render(request, "news/index.html", context=context)


class ArticleView(View):
    def get(self, request, article_id, *args, **kwargs):
        link = int(article_id)

        if link not in _articles.keys():
            raise Http404

        context = {"article": _articles[link]}
        return render(request, "news/article.html", context=context)
