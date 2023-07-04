from django.urls import path
from .views import upload_transactions, transaction_list

urlpatterns = [
    path('upload/', upload_transactions, name='upload_trasactions'),
    path('transactions/', transaction_list, name='transaction_list'),
    
    #path('transactions/', transactions_list, name='transactions_list'),
]
