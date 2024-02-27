#!/bin/bash

# Espera o banco de dados ficar pronto (ajuste conforme necessário)
echo "Aguardando o banco de dados ficar pronto..."
while ! nc -z db 3306; do   
  sleep 1
done
echo "Banco de dados pronto!"

# Aplica migrações
echo "Aplicando migrações..."
python manage.py migrate

# Carrega os dados iniciais
if [ $(python manage.py shell -c "from django.apps import apps; print(apps.get_model('biblia.Book').objects.count())") -eq 0 ]; then
    echo "Carregando dados iniciais..."
    python manage.py loaddata backup_myapp.json
else
    echo "Dados iniciais já carregados."
fi

# Inicia o servidor de aplicação
echo "Iniciando o servidor de aplicação..."
python manage.py runserver 0.0.0.0:8000
