from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('snippets/', views.SnippetList),
    path('snippets/<int:pk>/', views.SnippetDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)