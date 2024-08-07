
from django.urls import path

from apps.products.views.user_views import ProductsAPIView

app_name = 'products_user'

urlpatterns = [
    path(
        '',
        ProductsAPIView.as_view(),
    ),
    path(
        '<int:pk>/',
        ProductsAPIView.as_view(),
    ),
]
