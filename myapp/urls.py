from django.urls import path
from . import views
from . import tests
from django.conf import settings
from django.conf.urls.static import static


app_name = 'myapp'
urlpatterns = [
    # path('', tests.test, name='test'),
    path('',views.Login, name='index'), 
    path('register/', views.AccountRegistration.as_view(), name='register'),
    # path('signup/', views.AccountRegistration.as_view(), name='signup'),
    path("home/",views.home,name="home"),
    # path('home/',views.Home.as_view(),name='home'),
    path('artist/',views.Artist.as_view(),name='artist'),
    path('friend/',views.Friend.as_view(),name='friend'),
    path('recommend/',views.Recommend.as_view(),name='recommend'),
    path('post2/',views.CreatePost.as_view(),name='post2'),
    path('discover/',views.Discover.as_view(),name='discover'),
    path('myaccount/',views.Myaccount.as_view(),name='myaccount'),
    path('favorite/',views.Favorite.as_view(),name='favorite'),
    path('create/', views.CreatePost.as_view(), name='create'), 
    path('list/',views.MyPost.as_view(),name='list'),
    path('post/',views.appload.as_view(),name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# クラスを用いるときは.as_view()が必要
#<int:pk>はmodels.pyのDBテーブルそれぞれにIDをつけて動的なURLにする