from django.urls import path
from rest_framework import routers
from dushanbe_auth.views.user_views import Login, Logout
from dushanbe_auth.views.token_views import TokenReadOnlyModelViewSet
from dushanbe_auth.views.permission_views import PermissionReadOnlyModelViewSet


# ModelViewSet router
dushanbe_auth_router = routers.DefaultRouter()


""" Token Routers """
# List (GET): http://127.0.0.1:8000/api/tokens/
dushanbe_auth_router.register('tokens', TokenReadOnlyModelViewSet)


""" Permission Routers """
# List (GET): http://127.0.0.1:8000/api/permissions/
dushanbe_auth_router.register('permissions', PermissionReadOnlyModelViewSet)


# APIView
urlpatterns = [

    # -------------------- Auth --------------------

    # Login (POST) (No Token): http://127.0.0.1:8000/api/login/
    path('login/', Login.as_view()),

    # Logout (GET): http://127.0.0.1:8000/api/logout/
    path('logout/', Logout.as_view()),

]



