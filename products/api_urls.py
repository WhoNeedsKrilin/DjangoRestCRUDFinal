from django.urls import path, include
from rest_framework import routers
from products.views import *


router = routers.DefaultRouter()
router.register('', ProductViewSet )


urlpatterns=[
     path('products/', include(router.urls)),

]