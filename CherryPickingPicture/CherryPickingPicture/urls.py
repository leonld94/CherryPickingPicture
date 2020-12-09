from django.urls import path
from . import views

app_name = "CherryPickingPicture"

urlpatterns = [
    path('', views.main, name='main'),
    path('Login/', views.login, name='login'),
    path('Signup/', views.signup, name='signup'),
    path('Upload/', views.upload_page, name='upload_page'),
    path('User/<int:user_id>', views.user_page, name='user_page'),
    path('Image/<int:image_id>', views.image_page, name='image_page'),
    path('UploadImage/', views.upload_image, name='upload_image'),
]

