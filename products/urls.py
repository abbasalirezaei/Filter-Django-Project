from django.urls import path
from .views import HomeListView

app_name='products'
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
]
