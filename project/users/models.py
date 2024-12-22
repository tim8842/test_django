from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from products.models import Product


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и возвращает пользователя с email.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и возвращает суперпользователя с email.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["last_name", "first_name"]

    objects = UserManager()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
