from django.http import HttpResponse
from django.views import View


class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")
