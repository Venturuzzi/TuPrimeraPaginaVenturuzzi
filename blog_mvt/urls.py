from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('blogpages.urls', namespace='blogpages')),
    path('inbox/', include('messagesapp.urls', namespace='messagesapp')),
    path('accounts/', include('useraccounts.urls', namespace='useraccounts')),
    path('', RedirectView.as_view(url='/pages/')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
