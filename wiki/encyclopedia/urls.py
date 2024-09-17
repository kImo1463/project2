from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("wiki/create/", views.create_page, name="create_page"),
    path('wiki/edit/<str:title>', views.edit_page, name='edit_page'),
    path("random", views.random_page, name="random_page"),
]