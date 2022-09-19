from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    path('quiz/<int:pk>', views.QuizInfoView.as_view(), name='quiz_info'),
    path('like/<int:pk>', views.quiz_like, name='quiz_like'),

    path('quiz_list/', views.quiz_list, name='quiz_list'),
    path('quiz_questions/<int:quiz_id>', views.quiz_questions, name='quiz_questions'),
    path('submit_answer/<int:quiz_id>/<int:question_id>', views.submit_answer, name='submit_answer'),

    path('<int:pk>/profile/', views.ProfileView.as_view(), name='view_profile'),
    path('<int:pk>/edit_profile_page/', views.ProfileEditView.as_view(), name='edit_profile_page'),
    path('edit_profile/<int:user_id>', views.user_edit, name='edit_settings'),
    path('edit_password/<int:user_id>', views.password_edit, name='password_edit'),

    path('rules/', views.rules, name='rules'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    path('admin_panel/', views.AdminPanelView.as_view(), name='admin_panel'),
    path('quiz_switch_access/<int:pk>', views.quiz_switch_access, name='quiz_switch_access'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('quiz/edit/<int:pk>', views.QuizEditView.as_view(), name='edit_quiz'),
    path('question/edit/<int:pk>', views.QuestionEditView.as_view(), name='edit_question'),
    path('delete_quiz/<int:pk>', views.QuizDeleteView.as_view(), name='delete_quiz'),
    path('add_question/<int:quiz_id>', views.add_question, name='add_question'),
    path('list_questions/<int:quiz_id>', views.list_questions, name='list_questions'),
    path('delete_question/<int:pk>', views.QuestionDeleteView.as_view(), name='delete_question'),
]
