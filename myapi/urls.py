from  django.urls import path
from  myapi.views.bank_views  import Banks, BankDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('bank/',Banks.as_view(), name = 'banks'),
    path('bank/<str:pk>/',BankDetail.as_view(), name = 'bank_detail')

]
