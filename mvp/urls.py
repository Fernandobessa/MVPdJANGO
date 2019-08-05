from django.contrib import admin
from django.urls import path,include
from core.views import DemandaViewSet,EnderecoViewSet,ContatoViewSet,AnuncianteViewSet,PecaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'demanda', DemandaViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'contato', ContatoViewSet)
router.register(r'anunciante', AnuncianteViewSet)
router.register(r'pecas', PecaViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
