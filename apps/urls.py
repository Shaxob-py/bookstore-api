from django.urls import path
from apps.views import BookListApiView, BookCreateApiView, BookGetListApiView, BookUpdateApiView, BookDeleteView, \
    BookCategoryListView, BookMoneyTypeSearchView, BookMoneyAmountListApiView, CategoryListAPIView, \
    CategoryCreateApiView, CategorySearchListAPIView, CategoryUpdateApiView, CategoryDestroyAPIView, OrderListAPIView, \
    OrderCreateAPIView, OrderSearchListAPIView, OrderUpdateAPIView, OrderUsersListAPIView, OrderStatuTypeListAPIView, \
    OrderItemListAPIView, OrderItemOrderListAPIView, UserListAPIView, UserCreateAPIView, UserSearchListAPIView, \
    UserPartialUpdateAPIView, UserPartialDestroyAPIView, DeletedUserListAPIView, DeletedUserGetListView, \
    NetworkListAPIView, NetworkCreateAPIView, UserOrderListAPIView, OrderOrderItemListAPIView, BookCategoryListAPIView, \
    BookStatusListAPIView, TrendingCategoryListAPIView, OrderStatsAPIView, BookSearchTitleListAPIView, GetUserOrderBook, \
    GetUserChatListAPIView, BookSearchAuthorListAPIView, UserSearchLangListAPIView

urlpatterns = [
    path('book/list', BookListApiView.as_view(), name='book-list'),
    path('book/create', BookCreateApiView.as_view(), name='book-create'),
    path('id/book', BookGetListApiView.as_view(), name='book-get'),
    path('update/book<int:pk>', BookUpdateApiView.as_view(), name='book-update'),
    path('delete/book<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('category/book', BookCategoryListView.as_view(), name='book-category'),
    path('book/money', BookMoneyTypeSearchView.as_view(), name='book-money'),
    path('book/available', BookMoneyAmountListApiView.as_view(), name='book-available'),

    # ===========================Category=======================================
    path('category', CategoryListAPIView.as_view(), name='category'),
    path('category/create', CategoryCreateApiView.as_view(), name='category-create'),
    path('category/search_id', CategorySearchListAPIView.as_view(), name='category-search_id'),
    path('category/update<int:id>', CategoryUpdateApiView.as_view(), name='category-update'),
    path('category/delete<int:id>', CategoryDestroyAPIView.as_view(), name='category-delete'),

    # ==========================orders=====================================
    path('orders', OrderListAPIView.as_view(), name='orders'),
    path('orders/create', OrderCreateAPIView.as_view(), name='orders-create'),
    path('orders/search', OrderSearchListAPIView.as_view(), name='orders-search'),
    path('order/update<int:id>', OrderUpdateAPIView.as_view(), name='order-update'),
    path('order/users', OrderUsersListAPIView.as_view(), name='order-users'),
    path('order/money_type', OrderStatuTypeListAPIView.as_view(), name='order-money_type'),

    # =================================order-item ==================================

    path('order/item', OrderItemListAPIView.as_view(), name='order-item'),
    path('order/item/create', OrderItemListAPIView.as_view(), name='order-item'),
    path('order/item/orders', OrderItemOrderListAPIView.as_view(), name='order-item'),

    # ======================================== USERS ===============================================
    path('user/get', UserListAPIView.as_view(), name='users'),
    path('user/create', UserCreateAPIView.as_view(), name='users-create'),
    path('user/search', UserSearchListAPIView.as_view(), name='users-search'),
    path('user/update<int:id>', UserPartialUpdateAPIView.as_view(), name='users-update'),
    path('user/delete<int:id>', UserPartialDestroyAPIView.as_view(), name='users-delete'),
    path('user/chat', GetUserChatListAPIView.as_view(), name='users-chat'),
    path('user/chat', GetUserOrderBook.as_view(), name='users-order-book'),

    # =================================== DELETE USERS ==============================================
    path('deleted/users', DeletedUserListAPIView.as_view(), name='deleted-users'),
    path('deleted/users/get_all', DeletedUserGetListView.as_view(), name='deleted-users-get_all'),

    # ================================ NET-WORK ======================================================
    path('network/get', NetworkListAPIView.as_view(), name='network-get'),
    path('network/create', NetworkCreateAPIView.as_view(), name='network-create'),



    # ================================== Nested Serialize ================================

    path('user/orders', UserOrderListAPIView.as_view(), name='user-orders'),
    path('order/order-item', OrderOrderItemListAPIView.as_view(), name='order-order-item'),
    path('book/category', BookCategoryListAPIView.as_view(), name='book-category'),


    # ================================== Statistic ===============================================

    path('book/statistic', BookStatusListAPIView.as_view(), name='book-statistic'),
    path('trend/category/statu', TrendingCategoryListAPIView.as_view(), name='trend-category'),
    path('order/status', OrderStatsAPIView.as_view(), name='order-status'),




    # ================================== Search =====================================================
    path('search/title', BookSearchTitleListAPIView.as_view(), name='search-title'),
    path('search/authot', BookSearchAuthorListAPIView.as_view(), name='search-author'),
    path('search/lang/user', UserSearchLangListAPIView.as_view(), name='search-lang-user'),

    # ============================== Admins ======================================================

    path('get/admins', AdminListAPIView.as_view(), name='get-admins'),

]
