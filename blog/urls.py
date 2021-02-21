from django.urls import path

from .views import BlogListViews, BlogDetailPost


urlpatterns = [
    path('post/<int:pk>/',BlogDetailPost.as_view(), name = 'detail_post'),
    path('', BlogListViews.as_view(), name = 'home')

]