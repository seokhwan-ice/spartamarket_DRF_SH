from django.urls import path
from . import views

app_name="products"


urlpatterns = [
    path("",views.product_list, name="product_list"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:pk>/comments/", views.comment_list , name="comment_list"),
    path("comments/<int:pk>/", views.comment_detail, name="comment_detail"),
]