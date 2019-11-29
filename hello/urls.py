from django.urls import path
from .views import IndexView, NameListView, NameDetailView

app_name = "hello"

urlpatterns = [
    path("", IndexView.as_view()),
    path("list", NameListView.as_view(), name = "NameList"),
    path("<int:pk>", NameDetailView.as_view(), name = "NameDetail"),
]
