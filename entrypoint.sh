#!/bin/bash

# Espera o banco de dados ficar pronto (ajuste conforme necessário)
echo "Aguardando o banco de dados ficar pronto..."
while ! nc -z db 3306; do   
  sleep 1
done
echo "Banco de dados pronto!"

# Cria o usuário e concede privilégios totais
echo "Criando usuário de banco de dados e concedendo privilégios..."
mysql -u root -p -h db -e "CREATE USER 'euvitorr'@'%' IDENTIFIED BY 'euvitorr'; GRANT ALL PRIVILEGES ON * . * TO 'euvitorr'@'%'; FLUSH PRIVILEGES;"


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

# Cria um superusuário automaticamente se ele ainda não existir
echo "Verificando a existência do superusuário..."
SUPERUSER_EXISTS=$(python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='root').exists())")
if [ "$SUPERUSER_EXISTS" = "False" ]; then
    echo "Criando superusuário..."
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'admin@example.com', '1')" | python manage.py shell
else
    echo "Superusuário já existe."
fi


# Inicia o servidor de aplicação
echo "Iniciando o servidor de aplicação..."
python manage.py runserver 0.0.0.0:8000
