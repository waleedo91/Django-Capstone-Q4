"""capstone_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from capstone_app import views

from capstone_app.views import index
# Added the Player and Index urls
from capstone_app.views import PlayerView, ReviewsView

urlpatterns = [
    path('', views.homeview, name='home'),
    path('game/<int:game_id>/', views.gameview, name='gameview'),
    path('search/', views.searchview, name='search_result'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    path('player/<int:user_id>/', PlayerView.as_view(), name="playerview"),
    path('reviews/', ReviewsView.as_view(), name='review')
]
