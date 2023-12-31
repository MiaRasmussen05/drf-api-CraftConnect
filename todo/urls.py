from django.urls import path
from todo import views

urlpatterns = [
    path('ideas/', views.IdeaList.as_view()),
    path('ideas/<int:pk>/', views.IdeaDetail.as_view()),

    path('categories/', views.TaskCategoryList.as_view()),
    path('categories/<int:pk>/', views.TaskCategoryDetail.as_view()),

    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('tasks/<int:task_id>/contents/', views.TaskContentView.as_view(), name='task-content-create'),
    path('tasks/<int:task_id>/contents/<int:pk>/', views.TaskContentDetail.as_view(), name='task-content-detail'),

    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
]
