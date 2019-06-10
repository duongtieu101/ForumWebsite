from django.urls import path
from . import views
from .models import Board, Thread, User, Post
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index, name="index" ),
    path('board<int:id>/',views.index_board, name="index_board" ),
    path('thread<int:id>/',views.index_thread, name="index_thread" ),
    path('user<str:username>/',views.index_user, name="index_user" ),
    path('danhsachbaidang/',views.index_danhsachbaidang, name="index_danhsachbaidang" ),
    path('danhsachthanhvien/',views.index_danhsachthanhvien, name="index_danhsachthanhvien" ),
    path('dieukhoan_quydinh/',views.dieukhoan_quydinh, name="dieukhoan_quydinh" ),
    path('register/',views.register, name="register" ),
    path( 'login/',auth_views.LoginView.as_view(template_name="Home/login.html",
        extra_context={'Threads':Thread.objects.all().order_by("Time_Created")[:10]}),
        name="login"),
    path( 'logout/',auth_views.LogoutView.as_view(next_page='/',
        extra_context={'Threads':Thread.objects.all().order_by("Time_Created")[:10]}),
        name="logout"),
    path('search/',views.index_danhsachbaidang, name="search" ),
]
