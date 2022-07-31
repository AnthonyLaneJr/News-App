from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleTotalListView
)

urlpatterns = [
    path('<int:section>/<int:status>/', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('', ArticleTotalListView.as_view(), name='article_total_list'),
]