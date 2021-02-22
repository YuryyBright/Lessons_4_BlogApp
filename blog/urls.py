from django.urls import path

from .views import BlogListViews, BlogDetailPost, BlogAddPost, BlogUpdatePost, BlogDeletePost

urlpatterns = [
    path('post/<int:pk>/',BlogDetailPost.as_view(), name = 'detail_post'),
    path('', BlogListViews.as_view(), name = 'home'),
    path('post/new/', BlogAddPost.as_view(),name = 'add_post' ),
    path('post/<int:pk>/edit/', BlogUpdatePost.as_view(),name = 'edit_post' ),
    path('post/<int:pk>/detete/', BlogDeletePost.as_view(),name = 'delete_post' ),
]