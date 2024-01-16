from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog import views as v


urlpatterns = [
    path('', v.index_page, name='homepage'),
    # path('home', v.index_page, name='homepage'),
    path('home/', v.index_page, name='homepage'),

    path('about/', v.about_page, name='about'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
