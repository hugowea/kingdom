"""kingdom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from app.views import index, kingall, subordinate, king, king_subordinates, answer, test_of_kingdom, results, king_subordinate_unaccept, king_subordinate_result, king_subordinate_accept

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('subordinate/', subordinate, name='subordinate'),
    path('king/', king, name='king'),
    path('king_subordinates/<str:king_name>/', king_subordinates, name='king_subordinates'),
    path('answer/', answer, name='answer'),
    path('results/', results, name='results'),
    path('test_of_kingdom/<int:kingdom_id>/<str:user_name>/', test_of_kingdom, name='test_of_kingdom'),
    path('king_subordinates/<str:king_name>/<str:subordinate_name>/', king_subordinate_result, name='king_subordinate_result'),
    path('king_subordinates/<str:king_name>/<str:subordinate_name>/accept/', king_subordinate_accept, name='king_subordinate_accept'), 
    path('king_subordinates/<str:king_name>/<str:subordinate_name>/unaccept/', king_subordinate_unaccept, name='king_subordinate_unaccept'), 
    path('king/all/', kingall, name='kingall')
]
