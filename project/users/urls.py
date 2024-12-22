from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    OrderViewSet,
    RegisterView,
    UpdatePasswordView,
    LoginView,
)


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls), name="user-list"),
    path("", include(router.urls), name="order-list"),
    path("register/", RegisterView.as_view(), name="register"),
    path("update-password/", UpdatePasswordView.as_view(), name="update-password"),
    path("login/", LoginView.as_view(), name="login"),
]
