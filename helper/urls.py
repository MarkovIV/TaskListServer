from rest_framework import routers
from .api import HelperViewSet

router = routers.DefaultRouter()
router.register('api/helper', HelperViewSet, 'helper')

urlpatterns = router.urls
