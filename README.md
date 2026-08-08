# 💜 Adote Um Desejo

Adote Um Desejo é uma plataforma web desenvolvida em Django que conecta pessoas que possuem desejos, necessidades ou sonhos com pessoas dispostas a ajudar.

Através de cartinhas publicadas pelos usuários, a comunidade pode interagir, comentar, curtir e adotar desejos, criando uma rede de solidariedade e esperança.

---

## ✨ Funcionalidades

### 👤 Usuários
- Cadastro e login
- Recuperação de senha
- Perfil personalizado
- Foto de perfil
- Biografia
- Endereço completo
- Perfil público

### 💌 Cartinhas
- Criar cartinhas
- Visualizar cartinhas da comunidade
- Página individual da cartinha
- Limite de uma cartinha por semana
- Edição automática de cidade e estado pelo perfil
- Marcar desejo como correspondido
- Apagar cartinhas próprias

### ❤️ Interações
- Curtir e descurtir cartinhas
- Contador de curtidas
- Comentários
- Adoção de desejos
- Cancelamento de adoção

### 🔔 Notificações
- Notificação quando um desejo é adotado
- Central de notificações integrada

### 🔎 Busca e Filtros
- Pesquisa inteligente sem acentos
- Filtro por cidade
- Filtro por estado
- Filtro por status de adoção

### 📱 Experiência do Usuário
- Layout responsivo
- Navbar dinâmica
- FAQ (Dúvidas Frequentes)
- Interface moderna e amigável

---

## 🛠️ Tecnologias Utilizadas

### Backend
- Python 3
- Django

### Frontend
- HTML5
- CSS3
- JavaScript

### Banco de Dados
- SQLite3

### Bibliotecas
- Pillow
- Unidecode

---

## 📂 Estrutura do Projeto

```text
site-adote_um_desejo/

├── config/
├── core/
├── usuarios/
├── cartas/
├── static/
├── media/
├── templates/
├── manage.py
└── requirements.txt
```

---

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/adote-um-desejo.git
```

Entre na pasta:

```bash
cd adote-um-desejo
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000
```

---

## 📸 Telas do Sistema

### Home
Página inicial da plataforma.

### Feed de Cartinhas
Listagem de desejos publicados.

### Detalhes da Cartinha
Visualização completa de uma cartinha.

### Perfil
Área pessoal do usuário.

### Perfil Público
Visualização pública dos usuários e suas cartinhas.

### FAQ
Perguntas frequentes da comunidade.

---

## 🔮 Melhorias Futuras

- Chat privado entre usuários
- Sistema de denúncias
- Categorias de desejos
- Upload de múltiplas imagens
- Sistema de conquistas
- Painel administrativo avançado
- Mapa de desejos por localização

---

## 👩‍💻 Desenvolvedora

**Mikaele Cavalcanti Martins**

Estudante de Análise e Desenvolvimento de Sistemas.

### Contato

- LinkedIn: www.linkedin.com/in/mikaele-cavalcanti-martins-351b22371
- E-mail: 2cavalcantimartins@gmail.com

---

## 📜 Licença

Este projeto foi desenvolvido para fins educacionais e de portfólio.
