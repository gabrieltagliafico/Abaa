
from django.urls.conf import path

from login.views import *

urlpatterns = [
    path('',LoginFormView.as_view(),name='loginPath'),
    path('logout/',LogoutView.as_view(next_page = 'loginPath'),name='logoutPath'),
]