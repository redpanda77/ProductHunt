from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('create_info', views.create_info, name='create_info'),
    path('create_detail', views.create_detail, name='create_detail'),
    path('<int:product_id>/upvote', views.vote_up, name='vote_up'),
    path('<int:product_id>/', views.detail, name='detail'),
]
