from django.urls import path
from django.views.generic import ListView

from . import views
from myapp.models import *

urlpatterns = [
    # params for path: 'url adress/ <type:parametrName>', views.viewName, name = 'ShortcutNameOfTheArticle'
    path('', views.hello, name = 'hello'),
    path('<str:articleName>,<int:articleId>', views.viewArticle, name = 'viewArticle'),
    path('redirect', views.redirectPage, name = 'redirectPage'),
    path('static', views.StaticView.as_view()),
    path('dreamreals', ListView.as_view(model = Dreamreal, template_name = "dreamreal_list.html")),

]