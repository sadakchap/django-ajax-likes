from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.post_list,name='list'),
    path('detail/<int:pk>/<slug:slug>/',views.post_detail,name='detail'),
    path('like/',views.post_like,name='like'),
]
