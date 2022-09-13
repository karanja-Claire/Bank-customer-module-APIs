from  django.urls import path
from  myapi.views.bank_views  import Banks, BankDetail,BranchView,BranchDetailView,BankAccountView,AccountDetailView, Categories, CategoryDetail
from myapi.views.customer_views import CustomerDetail, CustomerView, MoneyTransferView, MoneytransferDetail, RoleDetail, RoleView, SettlementDetail, SettlementView
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

    path('category/',Categories.as_view(),name = 'category'),
    path('category/<str:pk>/',CategoryDetail.as_view(), name = 'category_detail'),

    path('role/',RoleView.as_view(), name = 'roles'),
    path('role/<str:pk>/',RoleDetail.as_view(), name = 'role_detail'),

    path('bank_accounts/',BankAccountView.as_view(), name = 'accounts'),
    path('bank_accounts/<str:pk>/',AccountDetailView.as_view(), name = 'account_detail'),

    path('customer/',CustomerView.as_view(), name = 'customers'),
    path('customer/<str:pk>/',CustomerDetail.as_view(), name = 'customer_detail'),

    path('money_transfer/',MoneyTransferView.as_view(), name ='money_transfer'),
    path('money_transfer/<str:pk>/',MoneytransferDetail.as_view(), name = 'transfer_detail'),
    
    path('withdraw',SettlementView.as_view(),name ='settlement'),
    path('withdraw/<str:pk>/',SettlementDetail.as_view(), name = 'settlement_detail')
]
