# Usa a imagem base do Python Alpine, que é leve e adequada para produção
FROM python:3.8-alpine

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instala dependências necessárias, incluindo o Node.js, o Yarn e o Bash
RUN apk add --no-cache \
    bash \
    curl \
    build-base \
    libffi-dev \
    musl-dev \
    openssl-dev \
    libgcc \
    mysql-dev \
    nodejs \
    npm \
    && npm install -g yarn

# Copia o script de entrada e dá permissão de execução
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copia o arquivo de dependências do Python e instala as dependências
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia os arquivos de dependências do frontend e instala as dependências
COPY frontend/package*.json /app/frontend/
RUN cd frontend && yarn install

# Copia o restante dos arquivos do projeto para o contêiner
COPY . /app

# Define o script de entrada como ponto de entrada
ENTRYPOINT ["/entrypoint.sh"]
