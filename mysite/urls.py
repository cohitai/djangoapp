"""mysite URL Configuration

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
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from django.views.generic.base import TemplateView

from django.conf.urls.static import static
from django.conf import settings
from blog_view import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainview.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('blog1/', TemplateView.as_view(template_name="index.html")),
    path('ckeditor', include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

