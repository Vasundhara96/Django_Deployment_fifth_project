from django.conf.urls import url,include
from usermodel_app import views

# TEMPLATE TAGGING
app_name = "usermodel_app"

urlpatterns = [
    url(r'^register/$',views.register,name="register"),
    url(r'^login/$',views.user_login,name="user_login"),
    ]
