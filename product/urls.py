from django.urls import path, include
from rest_framework import routers
from . import views as product_views

router = routers.DefaultRouter()
router.register(r'', product_views.ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]