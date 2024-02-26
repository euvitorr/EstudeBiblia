# Usa a imagem base do Python Alpine, que é leve e adequada para produção
FROM python:3.8-alpine

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instala dependências do sistema necessárias para o Django e as dependências do projeto
RUN apk add --no-cache \
    bash \
    curl \
    build-base \
    libffi-dev \
    musl-dev \
    openssl-dev \
    libgcc \
    mysql-dev

# Copia o arquivo de dependências do Python e instala as dependências
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante dos arquivos do projeto para o contêiner
COPY . /app

# Expõe a porta 8000 para comunicação com o Django
EXPOSE 8000

# Copia e dá permissão de execução para o script de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Define o script de entrada como ponto de entrada
ENTRYPOINT ["/entrypoint.sh"]
