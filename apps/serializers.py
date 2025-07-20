from django.db.models import ForeignKey
from drf_spectacular import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Book, Category, Order, OrderItem, User, Chat, DeleteUser, Network, BookStatus


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_money_type(self , value):
        if value != '':
            raise ValidationError('Book money type can not be empty')
        return value



class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        write_only_fields = 'name',


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = 'user_id','user'


class OrderItemModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = 'id','created_at','updated_at'

class ChatModelSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        read_only_fields = 'id','created_at','updated_at'

class DeleteUserModelSerializer(ModelSerializer):
    class Meta:
        model = DeleteUser
        fields = '__all__'

class NetworkModelSerializer(ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'

class BookStatsSerializer(ModelSerializer):
    class Meta:
        model = BookStatus
        fields = '__all__'
        read_only_fields = '__all__'

class TrendingCategorySerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(read_only=True)
    book_count = IntegerField(read_only=True)


class OrderStatsSerializer(Serializer):
    total_orders = IntegerField(read_only=True)
    paid_orders = IntegerField(read_only=True)
    pending_orders = IntegerField(read_only=True)


class BookAmountSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['amount']