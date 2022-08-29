from  django.urls import path
from  myapi.views.bank_views  import Banks, BankDetail,BranchView,BranchDetailView,BankAccountView,AccountDetailView
from  myapi.views import auth_views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('api/token/', auth_views.LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register',auth_views.RegisterView.as_view(), name = 'register'),

    path('bank/',Banks.as_view(), name = 'banks'),
    path('bank/<str:pk>/',BankDetail.as_view(), name = 'bank_detail'),

    path('branch/',BranchView.as_view(), name = 'branch'),
    path('branch/<str:pk>/',BranchDetailView.as_view(), name = 'branch_detail'),

    path('bank_accounts/',BankAccountView.as_view(), name = 'accounts'),
    path('bank_accounts/<str:pk>/',AccountDetailView.as_view(), name = 'account_detail')
]
