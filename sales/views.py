from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .serializers import TransactionSerializer
from rest_framework import viewsets
from .models import Transaction
import re

def upload_transactions(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            try:
                handle_uploaded_file(file)
                messages.success(request, 'Transaction file imported successfully.')
                return redirect('transaction_list')
            except Exception as e:
                messages.error(request, f'An error occurred while processing the file: {str(e)}')
                return redirect('transaction_list')
        else:
            messages.error(request, 'No file uploaded.')
            return render(request, 'upload.html')
    else:
        messages.error(request, 'Invalid request method.')
        return render(request, 'upload.html')

def handle_uploaded_file(file):
    

    # Lê o conteúdo do arquivo
    file_content = file.read().decode('utf-8')
    lines = file_content.split('\n')

    # Padrão para fazer o parsing do conteúdo do arquivo
    pattern = r'(\d{5}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2})([A-Z\s]+)\s+(\d+)([A-Z\s]+)'
    # Percorre as linhas do arquivo
    for line in lines:
        if line.strip() != '':
                    
            match = re.match(pattern, line)
                    
            if match:
                parts = re.split(pattern, line)
                timestamp = datetime.strptime(match.group(1)[1:], '%Y-%m-%dT%H:%M:%S%z')
                product_name = parts[2].strip()
                        
                if parts[3]:
                    value = int(parts[3])/100
                else:
                    value = 0.0
                seller = parts[4].strip()

                # Cria uma nova transação e a salva no banco de dados
                transaction = Transaction(timestamp=timestamp, product_name=product_name, value=value, seller=seller)
                        
                transaction.save()
                print('salvou')
            else:
                print('deu erro', line)

    # Retorne uma resposta de sucesso caso tudo ocorra corretamente
    return render(request, 'transaction_list.html')
        

def transaction_list(request):
    transactions = Transaction.objects.all()

    # Dicionário para armazenar as transações por produtor/afiliado e totalizador do valor
    transaction_data = {}

    for transaction in transactions:
        seller = transaction.seller

        # Verifica se o produtor/afiliado já está presente no dicionário
        if seller in transaction_data:
            transaction_data[seller]['transactions'].append(transaction)
            transaction_data[seller]['total_value'] += transaction.value
        else:
            transaction_data[seller] = {
                'transactions': [transaction],
                'total_value': transaction.value
            }

    context = {
        'transaction_data': transaction_data
    }

    return render(request, 'transaction_list.html', context)

class MyViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer