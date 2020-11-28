from django.conf import settings
from django.http import HttpResponse, Http404
from django.views import View
from django.shortcuts import render
import json


class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")


class ArticleView(View):
    def get(self, request, article_id, *args, **kwargs):
        _current_article = None
        with open(settings.NEWS_JSON_PATH) as news_file:
            news = json.load(news_file)
            for article in news:
                if article['link'] == int(article_id):
                    _current_article = article

        if _current_article is None:
            raise Http404

        context = {"article": _current_article}
        return render(request, "news/index.html", context=context)
