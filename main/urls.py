from django.urls import path
from .views import *
app_name = 'main'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('create/customer',CreateCustomerView.as_view(),name='create_customer'),
    path('detail/month/<str:pk>',MonthDetailView.as_view(),name='month_detail'),
    path('refresh/customer',refresh,name='refresh'),
    path('update/payment/<int:pk>',UpdatePaymentView.as_view(),name='payment_update'),
    path('update/customer/summa/<int:pk>',UpdateCustomerSummaView.as_view(),name='customer_summa_update'),
]