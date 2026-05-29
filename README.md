# Flask Piloto

Projeto piloto em Flask com SQLAlchemy, Flask-Migrate e banco de dados SQLite3.

## Visão geral

- Aplicação Flask simples com configuração de banco de dados em `app/__init__.py`
- Modelo de usuário em `app/models/usuario.py`
- Migrações gerenciadas por Flask-Migrate em `migrations/`
- Ponto de entrada em `run.py`
- Banco de dados local SQLite armazenado em `app/app.db`

## Estrutura do projeto

- `run.py` - inicializa a aplicação Flask
- `app/__init__.py` - cria a app, configura SQLAlchemy e Flask-Migrate e define rotas básicas
- `app/models/usuario.py` - modelo `Usuario` com campos `id`, `nome`, `email` e `senha`
- `app/routes/` - definem rotas e páginas do sistema
- `migrations/` - arquivos de migração do banco de dados

## Requisitos

- Python 3.11+ (ou versão compatível com Flask)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite3

## Instalação

1. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Banco de dados SQLite3

O projeto utiliza SQLite3 para o banco de dados local. O arquivo do banco é `app/app.db`.

Você pode inspecionar o banco diretamente com o cliente SQLite:

```bash
sqlite3 app/app.db
```

## Executando a aplicação

1. Ative o ambiente virtual:

```bash
source venv/bin/activate
```

2. Defina a variável de ambiente do Flask:

```bash
export FLASK_APP=run.py
```

3. Execute o aplicativo:

```bash
python run.py
```

4. Acesse no navegador:

- `http://127.0.0.1:5000/` - página inicial
- `http://127.0.0.1:5000/mostrar-dados` - página de demonstração
- `http://127.0.0.1:5000/cadastrar-usuario` - cadastro de usuário
- `http://127.0.0.1:5000/login` - página de login

## Migrações

Se precisar criar ou atualizar o banco de dados:

```bash
flask db init      # somente se ainda não houver migrations/
flask db migrate -m "mensagem"
flask db upgrade
```

> Observação: quando usar `flask`, certifique-se de ter ativado o ambiente virtual e definido `FLASK_APP=run.py`.

## Modelo `Usuario`

O modelo `Usuario` possui os seguintes campos:

- `id` - chave primária
- `nome` - nome do usuário
- `email` - e-mail único
- `senha` - senha do usuário

## Notas

- A chave secreta está definida em `app/__init__.py` como placeholder (`'sua_chave_secreta_aqui'`). Substitua por um valor seguro em produção.
- A aplicação atual é uma base para desenvolvimento e demonstração; as rotas atuais retornam texto ou templates.

# Melhorias

## Sistema de login e autenticação inicial  
- [ ] Uso de blueprints para organização das rotas, separando módulos por funcionalidade
- [ ] Validação e tratamento de formulários com Flask-WTF
- [ ] Implementar autenticação completa com `flask_login`
- [ ] Melhorar a segurança e o hash de senhas com `werkzeug.security` ou `bcrypt`
- [ ] Elaborar lógica de reset de senha

## Criação do formulário inicial e mapeamento das regras de negócio de cálculos
A fundação da aplicação (Arquitetura, Banco de Dados, Autenticação e Segurança) está concluída. A próxima fase foca na construção do motor do Simulador de Aposentadoria em si:

- [ ] **Integração da Base Cadastral (Dependência):** Importar a base de dados consolidada dos servidores (Responsável pela extração: Izabella).
- [ ] **Modelagem do Banco da Simulação:** Criar a tabela e as variáveis necessárias no banco de dados para salvar o progresso das simulações de cada usuário.
- [ ] **Interface de Simulação:** Construir o formulário de entrada das variáveis financeiras, previdenciárias e de tempo de serviço.
- [ ] **Preenchimento Inteligente (Auto-fill):** Desenvolver a lógica em Python para buscar e preencher automaticamente os dados cadastrais e o histórico do servidor no formulário (buscando na base consolidada da Izabella) para reduzir o trabalho manual.
- [ ] **Motor Matemático:** Implementar as funções que calculam e projetam a evolução da aposentadoria.