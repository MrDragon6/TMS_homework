from django.urls import path

from . import views
from .views import HomeView, PostView, PostAddView, PostUpdateView, ProfileView, ProfileEditView, \
    PostDeleteView, CommentAddView, category_view, category_list_view, like_view, \
    user_edit, ProfilePageCreateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post_view'),
    path('post_add/', PostAddView.as_view(), name='post_add'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('like/<int:pk>', like_view, name='post_like'),

    path('category/<str:categories>/', category_view, name='category'),
    path('category-list', category_list_view, name='category_list'),

    path('post/<int:pk>/comment', CommentAddView.as_view(), name='comment_add'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='view_profile'),
    path('<int:pk>/edit_profile_page/', ProfileEditView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', ProfilePageCreateView.as_view(), name='create_profile_page'),
    path('edit_profile/<int:user_id>', user_edit, name='edit_settings'),
]
