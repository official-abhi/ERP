from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='userhome' ),
    path('profile', views.profile, name='profile'),
    path('update', views.update, name='update'),
    path('orders', views.order , name='orders'),
    path('neworder',views.placeorder, name='placeorder'),
    path('orderupdate', views.orderupdate, name='orderupdate'),
    path('orderupdate/<int:id>', views.orderupdate2, name='orderupdate2'),
    path('trackorder', views.trackorder, name='trackorder'),
    path('d-order/<int:id>', views.orderdelete, name="deleteorder" ),




]
