"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

# swagger
# from rest_framework_swagger.views import get_swagger_view

# schemas
from rest_framework.documentation import include_docs_urls

# app
from dushanbe.urls import dushanbe_router


# swagger
# API_TITLE = 'Dushanbe APIs'
# API_DESCRIPTION = 'Dushanbe API List'
# schema_view = get_swagger_view(title=API_TITLE)


urlpatterns = [

    path('admin/', admin.site.urls),

    # home
    # path('', TemplateView.as_view(template_name="home.html")),

    # swagger (home)
    # path('', schema_view),

    # schemas (home)
    path('', include_docs_urls(title='Dushanbe APIs')),

    # DRF url
    path('api-auth/', include('rest_framework.urls')),

    # DRF authtoken model url
    path('api-token-auth/', obtain_auth_token),

    # app routers
    path('api/', include(dushanbe_router.urls)),

    # app urls
    path('api/', include('dushanbe.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


