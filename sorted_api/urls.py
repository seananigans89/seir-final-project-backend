from django.urls import path

from .views.kits import KitsView, KitView
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.items import ItemView, ItemsView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('items/', ItemsView.as_view(), name='items'),
    path('kits/', KitsView.as_view(), name='kits'),
    path('items/<int:pk>', ItemView.as_view(), name='item'),
    path('kits/<int:pk>', KitView.as_view(), name='kit'),

]