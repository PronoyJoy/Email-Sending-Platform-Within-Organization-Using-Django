from django.urls import path
from emailapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('email/',views.send,name='send'),
    path('email/compose/',views.compose,name='compose'),
    path('email/inbox/',views.email_list,name='inbox'),
    path('email/<int:id>/',views.email_detail,name='detail')
     
]
