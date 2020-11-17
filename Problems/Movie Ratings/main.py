from django.http import HttpResponse, Http404
from django.views import View

CINEMA_RATINGS = {
    "The Dark Knight": 8.2,
    "The Shawshank Redemption": 8.3,
    "Pulp Fiction": 8.1,
}


class CinemaRatingView(View):
    def get(self, request, film, *args, **kwargs):
        if film not in CINEMA_RATINGS.keys():
            raise Http404

        return HttpResponse(f'{CINEMA_RATINGS[film]}')
