from django.urls import path
from snippets import views
from snippets.views import snippet_detail


urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail)
]