from django.views.generic import ListView, DetailView

from .models import Striker


class StrikerListView(ListView):
    model = Striker


class StrikerDetailView(DetailView):
    model = Striker

