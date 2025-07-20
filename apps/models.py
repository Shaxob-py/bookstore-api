from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Model, CharField, IntegerField, TextField, DateTimeField, ForeignKey, ImageField, SET_NULL, \
    BooleanField, PositiveIntegerField
from django.db.models.enums import TextChoices
from django.contrib.auth import get_user_model


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user_object(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone_number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        return user

    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone_number, and password.
        """
        user = self._create_user_object(phone_number, password, **extra_fields)
        user.save(using=self._db)
        return user

    async def _acreate_user(self, phone_number, password, **extra_fields):
        """See _create_user()"""
        user = self._create_user_object(phone_number, password, **extra_fields)
        await user.asave(using=self._db)
        return user

    def create_user(self, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    create_user.alters_data = True

    async def acreate_user(self, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return await self._acreate_user(phone_number, password, **extra_fields)

    acreate_user.alters_data = True

    def create_superuser(self, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)

    create_superuser.alters_data = True

    async def acreate_superuser(
            self, phone_number=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return await self._acreate_user(phone_number, password, **extra_fields)

    acreate_superuser.alters_data = True


class User(AbstractUser):
    phone_number = CharField(max_length=20, unique=True)
    username = None
    email = None
    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    lang = CharField(max_length=10, null=True, blank=True, default='en')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Category(Model):
    name = CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(Model):
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    page = IntegerField()
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)
    amount = IntegerField()
    money_type = CharField(max_length=100)
    category = ForeignKey(Category, on_delete=models.CASCADE, related_name='books')


class Order(Model):
    class PaymentStatus(TextChoices):
        PENDING = 'Pending'
        APPROVED = 'Approved'

    user = ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payment_status = CharField(choices=PaymentStatus.choices, max_length=20, default=PaymentStatus.PENDING)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = ForeignKey(Book, on_delete=models.CASCADE, related_name='items')
    price = IntegerField()
    quantity = IntegerField()


class Chat(Model):
    username = CharField(max_length=120)
    full_name = CharField(max_length=120)
    language = CharField(max_length=120, default='en')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_admin = BooleanField(default=False)
    phone_number = CharField(max_length=120)
    user = ForeignKey("apps.User", on_delete=models.CASCADE)

class DeleteUser(Model):
    user_id = ForeignKey('apps.User', on_delete=models.CASCADE)
    deleted_at = DateTimeField(auto_now_add=True)


class Network(Model):
    title = CharField(max_length=120)
    link = CharField(max_length=120)


class BookStatus(Model):
    average_pages = PositiveIntegerField(default=1)
    total_pages = PositiveIntegerField(default=1)
    most_popular_books = PositiveIntegerField(default=0)
