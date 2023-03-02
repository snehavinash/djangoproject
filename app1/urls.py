from django.urls import path
from app1 import views
app_name='app1'
urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout',views.logout,name='logout'),
    path('gallery',views.gallery,name='gallery'),
    path('details',views.detail,name='detail'),

]