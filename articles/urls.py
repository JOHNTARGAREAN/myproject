from django.urls import path

from .views import (
    ArticleListView,      # новый
    ArticleDetailView,    # новый
    ArticleUpdateView,    # новый
    ArticleDeleteView,    # новый
    ArticleCreateView,
)
urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),      # новый
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),   # новый
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),# новый
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("", ArticleListView.as_view(), name="article_list"),
]