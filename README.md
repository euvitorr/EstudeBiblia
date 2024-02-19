# EstudeBiblia

## Sobre o Projeto

O projeto `EstudeBiblia` é uma aplicação desenvolvida para facilitar o estudo da Bíblia, permitindo aos usuários acessar diferentes versões, fazer anotações, marcar versículos como favoritos e criar planos de estudo personalizados. Desenvolvido com Django e Docker, o projeto visa proporcionar uma experiência interativa e enriquecedora no estudo bíblico.

## Funcionalidades

- **Acesso a diferentes versões da Bíblia**: Os usuários podem escolher entre diversas versões da Bíblia para leitura e estudo.
- **Anotações**: Permite aos usuários fazer anotações personalizadas em versículos específicos.
- **Favoritos**: Os usuários podem marcar versículos como favoritos para fácil acesso no futuro.
- **Planos de Estudo**: Criação de planos de estudo personalizados para guiar o usuário em seu estudo bíblico.
- **Grupos de Estudo**: Os usuários podem criar ou participar de grupos de estudo, compartilhando insights e discussões sobre os textos bíblicos.

## Tecnologias Utilizadas

- **Backend**: Django
- **Frontend**: HTML, CSS (com frameworks como Tailwind CSS), e JavaScript
- **Banco de Dados**: MySQL
- **Contêinerização**: Docker

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

## Configuração do Projeto

1. **Clone o repositório**

```bash
git clone https://github.com/euvitorr/EstudeBiblia.git
cd EstudeBiblia
```

2. **Construa e execute os contêineres**

```bash
docker-compose up --build
```

## Acesso ao Projeto
Após a configuração, o projeto estará disponível em http://localhost:8000.

## Estrutura do Projeto
A estrutura do projeto inclui várias aplicações Django, cada uma responsável por uma funcionalidade específica:

**biblia**: Gerenciamento de versões, livros, capítulos e versículos da Bíblia.
**anotacoes**: Sistema para criação e gerenciamento de anotações.
**usuarios**: Gerenciamento de usuários, autenticação e autorização.
**favoritos_historico**: Gerenciamento de versículos favoritos e histórico de leitura.
**grupos**: Criação e gerenciamento de grupos de estudo.
**planos_estudo**: Ferramentas para criar e gerenciar planos de estudo personalizados.

## Contribuindo
Contribuições são bem-vindas! Para contribuir, por favor siga os passos:

## Fork o projeto
Crie sua Feature Branch (git checkout -b feature/NovaFeature)
Commit suas mudanças (git commit -m 'Adicionando alguma NovaFeature')
Push para a Branch (git push origin feature/NovaFeature)
Abra um Pull Request

## Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.

## Contato
Vitor Rios Rodrigues - @euvitorr
