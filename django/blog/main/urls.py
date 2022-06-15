from django.urls import path

from . import views
from .views import HomeView, PostView, PostAddView, PostUpdateView, \
    PostDeleteView, CategoryAddView, category_view, category_list_view, like_view, user_edit


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post_view'),
    path('post_add/', PostAddView.as_view(), name='post_add'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('like/<int:pk>', like_view, name='post_like'),

    path('category_add/', CategoryAddView.as_view(), name='category_add'),
    path('category/<str:categories>/', category_view, name='category'),
    path('category-list', category_list_view, name='category_list'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('edit_profile/<int:user_id>', user_edit, name='edit_profile'),
]
