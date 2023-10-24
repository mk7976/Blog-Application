from django.urls import path
from . import views

urlpatterns = [
    path("", views.Bloghome, name="bloghome"),
    path("app/", views.Bloghome, name="bloghome"),
    path('<str:slug>', views.Blogpost, name="blogpost"),
    path('search/<str:slug>', views.Blogpost, name="blogpost"),
    path('search/', views.search, name="search"),
    path('signof/', views.Signof, name="signof"),
    path('login/', views.login, name="login"),
    path('logout/login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # path('search/postcomment', views.postComment, name="comments"),
    # path('postcomment', views.postComment, name="postComment"),
]
