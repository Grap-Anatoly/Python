from django.urls import path
from django.views.generic import ListView, TemplateView

from . import views
from myapp.models import *

urlpatterns = [
    # params for path: 'url adress/ <type:parametrName>', views.viewName, name = 'html page'
    path('', views.hello, name = 'hello'),
    path('<str:articleName>,<int:articleId>', views.viewArticle, name = 'viewArticle'),
    path('redirect', views.redirectPage, name = 'redirectPage'),
    path('static', views.StaticView.as_view()),

    path('dreamreals', ListView.as_view(model = Dreamreal, template_name = "dreamreal_list.html")),

    path('connection', 'formView', 'loginForm'),
    path('login', views.login, name = 'login'),

    path('profile', TemplateView.as_view(template_name='profile.html')),
    path('saved', views.saveProfile, name = 'saved'),
]