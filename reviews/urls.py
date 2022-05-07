from django.contrib import admin
from django.urls import path
from reviews.views import home
from reviews.views import GameListView, GameDetailViews
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home),
    path('', GameListView.as_view(), name='home'),
    path('<slug:slug>/',GameDetailViews.as_view(),name='game_detail')

]