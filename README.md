# Flask Piloto

Projeto piloto em Flask com SQLAlchemy e Flask-Migrate, usando SQLite como banco de dados local.

## Visão geral

- Aplicação Flask simples com configuração de banco de dados em `app/__init__.py`
- Modelo de usuário em `app/models/usuario.py`
- Migrações gerenciadas por Flask-Migrate em `migrations/`
- Ponto de entrada em `run.py`

## Estrutura do projeto

- `run.py` - inicializa a aplicação Flask
- `app/__init__.py` - cria a app, configura SQLAlchemy e Flask-Migrate, e define rotas básicas
- `app/models/usuario.py` - modelo `Usuario` com campos `id`, `nome`, `email` e `senha`
- `migrations/` - arquivos de migração do banco de dados
- `app/app.db` - banco de dados SQLite local

## Requisitos

- Python 3.11+ (ou versão compatível com Flask)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

## Instalação

1. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install flask flask_sqlalchemy flask_migrate
```

## Executando a aplicação

1. Ative o ambiente virtual:

```bash
source venv/bin/activate
```

2. Execute o aplicativo:

```bash
python run.py
```

3. Acesse no navegador:

- `http://127.0.0.1:5000/` para a página inicial
- `http://127.0.0.1:5000/mostrar_dados` para a rota de demonstração

## Banco de dados e migrações

O projeto usa SQLite e mantém o arquivo local em `app/app.db`.

Para criar ou aplicar migrações:

```bash
flask db init      # somente se ainda não houver migrations/
flask db migrate -m "mensagem"
flask db upgrade
```

> Observação: Se estiver usando `flask` via ambiente virtual, defina a variável `FLASK_APP=run.py` antes de executar os comandos de migração.

## Modelo `Usuario`

O modelo `Usuario` possui os seguintes campos:

- `id` - chave primária
- `nome` - nome do usuário
- `email` - e-mail único
- `senha` - senha do usuário

## Notas

- A chave secreta está definida em `app/__init__.py` como placeholder (`'sua_chave_secreta_aqui'`). Substitua por um valor seguro em produção.
- A aplicação atual é uma base para desenvolvimento e demonstração; as rotas atuais retornam apenas texto simples.
