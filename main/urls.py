from django.urls import path 
from main import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.TodoTask.as_view(),name='tasks'),
    path('detail/<int:pk>',views.TodoTask_detail.as_view(),name='task'),
    path('create/',views.CreateTask.as_view(),name='createtask'),
    path('update/<int:pk>/',views.UpdateTask.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeleteTask.as_view(),name='delete'),
    path('login/',views.Login_user.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',views.UserRegister.as_view(),name='register'),
]
