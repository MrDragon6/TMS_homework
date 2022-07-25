from django.urls import path

from .views import login, logout, signup, HomeView, PostView, PostAddView, PostUpdateView, \
    ProfileView, ProfileEditView, PostDeleteView, CommentAddView, category_view, category_list_view, \
    subscriptions_list_view, like_view, subscribe_view, user_edit, password_edit, \
    ProfilePageCreateView, create_author


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post_view'),
    path('post_add/', PostAddView.as_view(), name='post_add'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('like/<int:pk>', like_view, name='post_like'),

    path('category/<str:categories>/', category_view, name='category'),
    path('category-list', category_list_view, name='category_list'),

    path('subscribe/<int:pk>', subscribe_view, name='author_subscribe'),
    path('subscriptions', subscriptions_list_view, name='subscriptions_list'),

    path('post/<int:pk>/comment', CommentAddView.as_view(), name='comment_add'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='view_profile'),
    path('<int:pk>/edit_profile_page/', ProfileEditView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', ProfilePageCreateView.as_view(), name='create_profile_page'),
    path('edit_profile/<int:user_id>', user_edit, name='edit_settings'),
    path('edit_password/<int:user_id>', password_edit, name='password_edit'),
    path('become_author/<int:user_id>', create_author, name='create_author'),
]
