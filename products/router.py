from libreria.viewsets import LibreriaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('libreria', LibreriaViewset)
