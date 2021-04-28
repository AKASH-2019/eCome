from django.urls import path

from .views import ProductAPIView, CategoryAPIView

urlpatterns = [
    path('category/',CategoryAPIView.as_view()),
    path('product/',ProductAPIView.as_view()),
]
