from django.urls import path
from . import views
from .views import menuView, bookingView, secret
# from . views import bookingView
from .views import secret
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns= [
 path('home/', views.home),
 path('menu/', menuView),
 path('booking/', bookingView),
 path('secret/', secret),
 path('api-auth-token/', obtain_auth_token)
]
