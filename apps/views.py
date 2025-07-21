from django.db.models import Count, Avg
from django.template.context_processors import request
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Book, Category, Order, OrderItem, User, Chat, DeleteUser, Network
from apps.serializers import BookModelSerializer, CategoryModelSerializer, OrderModelSerializer, \
    OrderItemModelSerializer, UserModelSerializer, ChatModelSerializer, DeleteUserModelSerializer, \
    NetworkModelSerializer, BookStatsSerializer, TrendingCategorySerializer, OrderStatsSerializer, BookAmountSerializer


@extend_schema(tags=['books'])
class BookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


@extend_schema(tags=['books'])
class BookCreateApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


@extend_schema(tags=['books'], parameters=[
    OpenApiParameter(name='book_id', description='Book id ni kiriting', required=False, type=int)
], )
class BookGetListApiView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        book_id = self.request.query_params.get('book_id')
        if book_id:
            queryset = queryset.filter(id=book_id)
        return queryset


@extend_schema(tags=['books'])
class BookUpdateApiView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


@extend_schema(tags=['books'])
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "Book o'chirildi"})


@extend_schema(tags=['books'], parameters=[
    OpenApiParameter(name='category_id', description='Category id ni kiriting', required=False, type=int)
],
               )
class BookCategoryListView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        queryset = Book.objects.all()
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            return queryset
        return queryset


@extend_schema(tags=['books'], parameters=[
    OpenApiParameter(name='money', description='Money Type Choice', required=False, type=str)
],
               )
class BookMoneyTypeSearchView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        money_type = self.request.query_params.get('money')
        if money_type:
            queryset = queryset.filter(money_type=money_type)
            return queryset
        return queryset


@extend_schema(tags=['books'])
class BookMoneyAmountListApiView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(amount__gt=0)
        return queryset


@extend_schema(tags=['categories'])
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['categories'])
class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['categories'], parameters=[
    OpenApiParameter(name='category_id', description='Category id ni kiriting', required=False, type=int)
],)
class CategorySearchListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(id=category_id)
            return queryset
        return queryset


@extend_schema(tags=['categories'])
class CategoryUpdateApiView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'id'


@extend_schema(tags=['categories'])
class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'id'


@extend_schema(tags=['orders'])
class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


@extend_schema(tags=['orders'])
class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


@extend_schema(tags=['orders'], parameters=[
    OpenApiParameter(name='order_id', description='Order id ni kiriting', required=False, type=int)
], )
class OrderSearchListAPIView(ListAPIView):
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        query = Order.objects.all()
        order_id = self.request.query_params.get('order_id')
        if order_id:
            queryset = query.filter(id=order_id)
            return queryset
        return query


@extend_schema(tags=['orders'])
class OrderUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'id'


@extend_schema(tags=['orders'], parameters=[
    OpenApiParameter(name='user_id', description='User id ni kiriting', required=False, type=int)
])
class OrderUsersListAPIView(ListAPIView):
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Order.objects.all()
        if user_id:
            queryset = queryset.filter(user_id=user_id)
            return queryset
        return queryset


@extend_schema(tags=['orders'], parameters=[
    OpenApiParameter(name='payment_status', description='Money type ni kiriting', required=False, type=str)
], )
class OrderStatuTypeListAPIView(ListAPIView):
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        query = Order.objects.all()
        payment_status = self.request.query_params.get('payment_status')
        if payment_status:
            query = query.filter(payment_status=payment_status)

        return query


@extend_schema(tags=['order-items'])
class OrderItemListAPIView(ListAPIView):
    serializer_class = OrderItemModelSerializer
    queryset = OrderItem.objects.all()


@extend_schema(tags=['order-items'])
class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemModelSerializer


@extend_schema(tags=['order-items'], parameters=[
    OpenApiParameter(name='order_id', description='Order id ni kiriting', required=False, type=str)
], )
class OrderItemOrderListAPIView(ListAPIView):
    serializer_class = OrderItemModelSerializer

    def get_queryset(self):
        query = OrderItem.objects.all()
        order_id = self.request.query_params.get('order_id')
        if order_id:
            query = query.filter(order_id=order_id)
        return query


@extend_schema(tags=['users'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['users'])
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['users'], parameters=[
    OpenApiParameter(name='user_id', description='User id ni kiriting', required=False, type=int)
], )
class UserSearchListAPIView(ListAPIView):
    serializer_class = UserModelSerializer

    def get_queryset(self):
        query = User.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            query = query.filter(id=user_id)
        return query


@extend_schema(tags=['users'])
class UserPartialUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['patch']
    lookup_field = 'id'


@extend_schema(tags=['users'])
class UserPartialDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'id'


@extend_schema(tags=['chats'])
class ChatListAPIView(ListAPIView):
    serializer_class = ChatModelSerializer
    queryset = Chat.objects.all()


@extend_schema(tags=['chats'])
class ChatCreateAPIView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatModelSerializer


@extend_schema(tags=['chats'], parameters=[
    OpenApiParameter(name='username', description='Username ni kiriting', required=False, type=str)
], )
class ChatSearchUsernameListAPIView(ListAPIView):
    serializer_class = ChatModelSerializer

    def get_queryset(self):
        query = Chat.objects.all()
        username = self.request.query_params.get('username')
        if username:
            query = query.filter(username=username)
        return query


@extend_schema(tags=['deleted_user'], parameters=[
    OpenApiParameter(name='user_id', description='Username ni kiriting', required=False, type=str)
])
class DeletedUserListAPIView(ListAPIView):
    serializer_class = DeleteUserModelSerializer

    def get_queryset(self):
        query = DeleteUser.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            query = query.filter(user_id=user_id)
        return query


@extend_schema(tags=['deleted_user'])
class DeletedUserGetListView(ListAPIView):
    serializer_class = DeleteUserModelSerializer
    queryset = DeleteUser.objects.all()


@extend_schema(tags=['network'])
class NetworkListAPIView(ListAPIView):
    serializer_class = NetworkModelSerializer
    queryset = Network


@extend_schema(tags=['network'])
class NetworkCreateAPIView(CreateAPIView):
    serializer_class = NetworkModelSerializer
    queryset = Network.objects.all()


@extend_schema(tags=['nested'], parameters=[
    OpenApiParameter(name='user_id', description='User id ni kiriting', required=False, type=str)
])
class UserOrderListAPIView(ListAPIView):
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        query = Order.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            query = query.filter(user_id=user_id)
        return query


@extend_schema(tags=['nested'], parameters=[
    OpenApiParameter(name='order_id', description='Order id ni kiriting', required=False, type=str)
])
class OrderOrderItemListAPIView(ListAPIView):
    serializer_class = OrderItemModelSerializer

    def get_queryset(self):
        query = OrderItem.objects.all()
        order_id = self.request.query_params.get('order_id')
        if order_id:
            query = query.filter(order_id=order_id)
        return query


@extend_schema(tags=['nested'], parameters=[
    OpenApiParameter(name='category_id', description='Category id ni kiriting', required=False, type=str)
])
class BookCategoryListAPIView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        query = Book.objects.all()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            query = query.filter(category_id=category_id)
        return query


@extend_schema(tags=['statistic'])
class BookStatusListAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        average_pages = Book.objects.aggregate(avg=Avg('pages'))['avg'] or 0
        total_books = Book.objects.count()
        # top category id
        top_category = (
            Book.objects.values('category__name')
            .annotate(count=Count('id'))
            .order_by('-count')
            .first()
        )
        most_common_category = top_category['category__name'] if top_category else None

        data = {
            'average_pages': average_pages,
            'total_books': total_books,
            'most_common_category': most_common_category
        }
        serializer = BookStatsSerializer(data)
        return Response(serializer.data)


@extend_schema(tags=['statistic'])
class TrendingCategoryListAPIView(ListAPIView):
    serializer_class = TrendingCategorySerializer

    def get_queryset(self):
        return (
            Category.objects.annotate(book_count=Count('book'))
            .order_by('-book_count')
        )


@extend_schema(tags=['statistic'])
class OrderStatsAPIView(APIView):
    def get(self, request):
        total_orders = Order.objects.count()
        paid_orders = Order.objects.filter(status='paid').count()
        pending_orders = Order.objects.filter(status='pending').count()

        data = {
            'total_orders': total_orders,
            'paid_orders': paid_orders,
            'pending_orders': pending_orders,
        }

        serializer = OrderStatsSerializer(data)
        return Response(serializer.data)


@extend_schema(tags=['users'],
               parameters=[OpenApiParameter(name='user_id',
                                            description='User id ni kiriting', required=False, type=int)])
class GetUserChatListAPIView(ListAPIView):
    serializer_class = ChatModelSerializer

    def get_queryset(self):
        query = Chat.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            query = query.filter(user_id=user_id)
        return query


@extend_schema(tags=['users'], parameters=[OpenApiParameter(name='user_id',
                                                            description='User id ni kiriting',
                                                            required=False, type=int)])
class GetUserOrderBook(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Book.objects.filter(order__user_id=user_id).distinct()


@extend_schema(tags=['search'], parameters=[
    OpenApiParameter(name='title', description='title ni kiriting', required=False, type=str)
])
class BookSearchTitleListAPIView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        query = Book.objects.all()
        title = self.request.query_params.get('title')
        if title:
            query = query.filter(title__icontains=title)
        return query


@extend_schema(tags=['search'], parameters=[
    OpenApiParameter(name='author', description='Author ni kiriting', required=False, type=str)
])
class BookSearchAuthorListAPIView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        query = Book.objects.all()
        author = self.request.query_params.get('author')
        if author:
            query = query.filter(author__icontains=author)
        return query


@extend_schema(tags=['search'], parameters=[
    OpenApiParameter(name='lang', description='lang ni kiriting', required=False, type=str)
])
class UserSearchLangListAPIView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        query = Book.objects.all()
        lang = self.request.get_query_params.get('lang')
        if lang:
            query = query.filter(lang=lang)
        return query



@extend_schema(tags=['admins'])
class AdminListAPIView(ListAPIView):
    serializer_class = UserModelSerializer

    def get_queryset(self):
        query = User.objects.all()
        admins = query.filter(is_staff=True)
        return admins


@extend_schema(tags=['admins'])
class BookAmountUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAmountSerializer
    http_method_names = ['patch']
    lookup_field = 'id'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
