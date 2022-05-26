"""djangoProjectDiagnostics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from app.views import LoginUser, TableViewSetAi1, TableViewSetAi2

router = DefaultRouter()

router.register(r'tables-1', TableViewSetAi1, basename='tables-1')
router.register(r'tables-2', TableViewSetAi2, basename='tables-2')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginUser.as_view(), name='login'),
    path('home/', TemplateView.as_view(template_name='app/index.html'), name='home'),
    path('graph/', TemplateView.as_view(template_name='app/graph/all/graph_page.html'), name='graph'),
    path('details/<int:pk>', TemplateView.as_view(template_name='app/graph/details/details_graph_page.html'), name='details'),
    path('table/', TemplateView.as_view(template_name='app/table/table_page.html'), name='table'),
    path('api/', include(router.urls)),
    #path('dashboardkit/', TemplateView.as_view(template_name='dashboardkit/dashboardkit/index.html'), name='dashboardkit'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
