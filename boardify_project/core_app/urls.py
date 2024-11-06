from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all-boards/', views.all_boards_page, name='all_boards_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('category/<slug:slug>/', views.boards_by_category_page, name='boards_by_category_page'),
    path('location/<slug:slug>/', views.boards_by_location_page, name='boards_by_location_page'),
    path('search/', views.search_results, name='search_results'),
    path('board/<int:pk>/', views.board_detail_page, name='board_detail_page'),
    path('login/', views.login_page, name='login_page'),
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('logout/', views.logout_action, name='logout_action'),
    path('profile/', views.profile_page, name='profile_page'),
    path('user-boards/', views.user_boards_page, name='user_boards_page'),
    path('create-board/', views.create_board_page, name='create_board_page'),
    path('success/', views.success_page, name='success_page'),
    path('update-board/<int:pk>/', views.update_board_page, name='update_board_page'),
    path('delete-board/<int:pk>/', views.delete_board_page, name='delete_board_page'),
    path('create-or-update-profile/', views.create_or_update_profile_page, name='create_or_update_profile_page'),
]
