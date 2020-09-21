from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OfferViewSet, OfferList, OfferListApiView


router = DefaultRouter(trailing_slash=False)
router.register('offers', OfferViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products/', OfferList.as_view()),
    path('products-filter/', OfferListApiView.as_view())
]
