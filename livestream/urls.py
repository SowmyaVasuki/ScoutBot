from django.urls import path

from . import views

app_name = 'livestream'

urlpatterns = [
    path('', views.index, name='index'),
    path('forward', views.forward, name='forward'),
    path('reverse', views.reverse, name='reverse'),
    path('right', views.right, name='right'),
    path('left', views.left, name='left'),
    path('forward1', views.forward1, name='forward1'),
    path('reverse1', views.reverse1, name='reverse1'),
    path('right1', views.right1, name='right1'),
    path('left1', views.left1, name='left1'),
    path('stop', views.stop, name='stop'),
    path('checkfor', views.checkfor, name='checkfor'),
    path('checkback', views.checkback, name='checkback'),
]