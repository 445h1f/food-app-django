"""
URL configuration for food_menu_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

app_name = 'food'

urlpatterns = [
    # path('items/', views.item, name="items"),
    path('items/', view=login_required(views.IndexClassView.as_view()), name='items'),
    path('items/detail/<int:itemId>', views.details, name="details"),
    path('items/update/<int:itemId>', views.updateItem, name="update"),
    path('items/add', views.addItem, name='add'),
    path('items/delete/<int:itemId>', views.deleteItem, name='delete'),
    path('items/add2/', views.add2, name='add2'),
    path('items/update2/<int:itemId>', views.update2, name='update2'),
    path('items/delete2/<int:itemId>', views.delete, name='delete2'),
]
