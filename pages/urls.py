from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('media/', MediaPageView.as_view(), name='media'),
    path('repertoire/', RepertoirePageView.as_view(), name='repertoire'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('article/', BlogArticlePageView.as_view(), name='article'),
    path('', IndexPageView.as_view(), name='index'),
]
