# Imagem oficial do Python como base
FROM python:3.8-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Evitar que Python escreva arquivos .pyc no disco (opcional)
ENV PYTHONDONTWRITEBYTECODE 1
# Buffering do Python desativado para permitir a log em tempo real dentro do contêiner
ENV PYTHONUNBUFFERED 1

# Copiar e instalar as dependências do projeto Django
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y \
        default-libmysqlclient-dev \
        pkg-config \
        gcc \
        netcat-openbsd \
        default-mysql-client && \
    pip install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copia o script de entrada e dá permissão de execução
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copiar o projeto para o diretório /app dentro do contêiner
COPY . /app/
