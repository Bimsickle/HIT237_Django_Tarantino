from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from quentin_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^movies/?$', views.movies, name = "movies"),
    url(r'^model/?$', views.model, name = "model"),
    url(r'^credits/?$', views.credits, name = "credits"),
    url(r'^film/(\d{1,4})/?$', views.details, name = "film"),
    url(r'^search/?$', views.search, name = "search"),
]
