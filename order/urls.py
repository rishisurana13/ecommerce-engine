from django.urls import include, path
from rest_framework.routers import DefaultRouter
from order.views import OrderViewSet, LineItemViewSet
from django.urls import path



router = DefaultRouter()
router.register(r"orders", OrderViewSet)
router.register(r"cart", LineItemViewSet)
# router.register(r"admin-view/products", AdminProductViewSet)
# 


urlpatterns = [

    path("", include(router.urls)),
    
]
