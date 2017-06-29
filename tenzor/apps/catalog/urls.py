from django.conf.urls import url, include
from .views import CategoryViewSet, GoodsViewSet
from rest_framework.routers import DefaultRouter


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'goods', GoodsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
