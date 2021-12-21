"""djangotask URL Configuration

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
from ninja import NinjaAPI

from account.controllers import account_controller
from commerce.controllers import commerce_controller, order_controller

api = NinjaAPI()
api.add_router('auth', account_controller)
api.add_router('', commerce_controller)
api.add_router('order', order_controller)

urlpatterns = [
    path('api/', api.urls),
    path('admin/', admin.site.urls),
]
