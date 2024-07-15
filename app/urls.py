from django.contrib import admin
from django.urls import path
from .views import match_product, add_part, part_list, generate_barcode
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('match_product/', match_product, name='match_product'), #match_product url
    path('generate_barcode/', generate_barcode, name='generate_barcode'),
    path('', part_list, name='part_list'),
    path('add_part/', add_part, name='add_part'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

