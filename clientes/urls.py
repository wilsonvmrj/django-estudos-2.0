from django.urls import path
from .views import persons_list
from .views import persons_new



urlpatterns = [
    path('list/', persons_list, name='peson_list'),
    path('new/', persons_new, name='person_new'),
]