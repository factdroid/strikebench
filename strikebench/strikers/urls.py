from django.urls import path

from . import views

app_name = "strikers"


urlpatterns = [
    path('', views.StrikerListView.as_view(), name='list'),
    path('<slug:slug>/', views.StrikerDetailView.as_view(), name='detail'),
]