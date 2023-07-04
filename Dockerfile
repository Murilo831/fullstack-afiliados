# Use uma imagem base com suporte ao Python e ao Django
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código-fonte da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta do servidor web (geralmente a porta 8000) para acessar a aplicação
EXPOSE 8000

# Defina o comando para iniciar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]