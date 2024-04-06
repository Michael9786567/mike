from django.urls import path
from . import views

urlpatterns = [
    path('about',views.about,name='about'),
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('create',views.create, name='create'),
    path('<int:pk>',NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update',NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delite',NewsDeliteView.as_view(), name='news-delite')
]
 