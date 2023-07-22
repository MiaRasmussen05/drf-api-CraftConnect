from django.urls import path
from todo import views

urlpatterns = [
    path('ideas/', views.IdeaList.as_view()),
    path('ideas/<int:pk>/', views.IdeaDetail.as_view()),
    
    path('categories/', views.TaskCategoryList.as_view()),
    path('categories/<int:pk>/', views.TaskCategoryDetail.as_view()),
    
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]