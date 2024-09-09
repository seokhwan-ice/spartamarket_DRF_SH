from django.urls import path
from . import views

app_name="products"


urlpatterns = [
    path("",views.ProductListAPIView.as_view(), name="product_list"),
#    path("create/", views.product_create, name="product_create"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:pk>/comments/", views.comment_list , name="comment_list"),
    path("comments/<int:pk>/", views.comment_detail, name="comment_detail"),
]