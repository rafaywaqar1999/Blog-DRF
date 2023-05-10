from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogPostListCreateApiView.as_view(), name = 'list-create-blog'),
    path('blog/<int:pk>/', BlogPostUpdateRetrieveDestroyApiView.as_view(), name = 'update-retrieve-destroy-blog')
]
