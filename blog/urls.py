from django.urls import path
from .views import PostByCategory, PostByTags, PostList, PostDetail


app_name = 'blog'


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<slug:slug>', PostDetail.as_view(), name='post_detail'),

    path('category/<slug:slug>', PostByCategory.as_view(), name='post_by_category'),
    path('tags/<slug:slug>', PostByTags.as_view(), name='post_by_tags'),
]
