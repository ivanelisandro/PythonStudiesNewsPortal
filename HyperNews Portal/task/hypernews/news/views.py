from django.conf import settings
from django.http import Http404
from django.views import View
from django.shortcuts import render, redirect
from datetime import datetime
from collections import OrderedDict
import json
import random


class Journal:
    date_groups = {}
    articles = {}

    def include_in_groups(self, article):
        date = datetime.strptime(article["created"], '%Y-%m-%d %H:%M:%S').date()
        if str(date) not in self.date_groups.keys():
            self.date_groups[str(date)] = {}
        self.date_groups[str(date)]["date"] = date
        if "articles" not in self.date_groups[str(date)].keys():
            self.date_groups[str(date)]["articles"] = []
        self.date_groups[str(date)]["articles"].append(article)

    def include_article(self, article):
        self.articles[article["link"]] = article
        self.include_in_groups(article)

    def load_news(self):
        with open(settings.NEWS_JSON_PATH) as news_file:
            _news = json.load(news_file)
            for article in _news:
                self.include_article(article)

    def filtered_news(self, search):
        _filtered = {}
        for date, info in self.date_groups.items():
            for item in info["articles"]:
                if search in item["title"]:
                    if date not in _filtered.keys():
                        _filtered[date] = {}
                    _filtered[date]["date"] = info["date"]
                    if "articles" not in _filtered[date].keys():
                        _filtered[date]["articles"] = []
                    _filtered[date]["articles"].append(item)
        return _filtered

    def ordered_filtered_news(self, search):
        if search is None or search == "":
            return self.ordered_news()
        else:
            filtered = self.filtered_news(search)
            ordered = OrderedDict(sorted(
                filtered.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=True))
            return ordered.values()

    def ordered_news(self):
        ordered = OrderedDict(sorted(
            self.date_groups.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=True))
        return ordered.values()

    def generate_link(self):
        _link = random.randint(1, 999999)

        while _link in self.articles.keys():
            _link = random.randint(1, 999999)

        return _link

    def create_article(self, title, text):
        return {
            "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "text": text,
            "title": title,
            "link": self.generate_link()}

    def save(self, article):
        self.include_article(article)
        with open(settings.NEWS_JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(list(self.articles.values()), file)


journal = Journal()
journal.load_news()


class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        # Previous implementation
        # return HttpResponse("Coming soon")
        return redirect('/news/')


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class NewsView(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get('q')
        context = {"groups": journal.ordered_filtered_news(search)}
        return render(request, "news/index.html", context=context)


class ArticleView(View):
    def get(self, request, article_id, *args, **kwargs):
        link = int(article_id)

        if link not in journal.articles.keys():
            raise Http404

        context = {"article": journal.articles[link]}
        return render(request, "news/article.html", context=context)


class CreateArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "news/create_article.html")

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('text')
        new_article = journal.create_article(title, text)
        print(new_article)
        journal.save(new_article)
        return redirect('/news/')
