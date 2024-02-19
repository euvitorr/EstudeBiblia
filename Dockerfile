# Imagem oficial do Python como base
FROM python:3.8-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Evitar que Python escreva arquivos .pyc no disco (opcional)
ENV PYTHONDONTWRITEBYTECODE 1
# Buffering do Python desativado para permitir a log em tempo real dentro do contêiner
ENV PYTHONUNBUFFERED 1

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Atualizar pip
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Instalar as dependências do projeto Django
# Copia o script de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copiar o projeto para o diretório /app dentro do contêiner
COPY . /app/
