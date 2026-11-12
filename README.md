# 💰 Gerenciador de Finanças Pessoais

Aplicação em Python desenvolvida para ajudar no controle das finanças pessoais, permitindo registrar
e acompanhar receitas e despesas de forma simples e organizada, com integração a um bot do Telegram.

> ⚠️ **Projeto em desenvolvimento!**
> Este projeto ainda está sendo construído e **novas funcionalidades serão adicionadas** ao longo do tempo.
>  O que está descrito abaixo representa o estado atual e os planos para as próximas versões.

---

## 📌 Sobre o Projeto

Este projeto foi criado com o objetivo de praticar e consolidar conhecimentos de programação,
ao mesmo tempo em que resolve um problema do dia a dia: **organizar o dinheiro**.

Ele está sendo desenvolvido de forma incremental, com foco em:

- Organização de código em módulos (configuração, serviços e bot)
- Integração com serviços externos
- Boas práticas de estrutura de projeto
- Evolução contínua, funcionalidade por funcionalidade

---

## 🚧 Status do Projeto

🟡 **Em desenvolvimento** — a base do projeto já está estruturada e novas funções ainda serão implementadas.

---

## 🚀 Funcionalidades

### ✅ Em andamento / disponíveis
- 🤖 Bot do Telegram para interação com o sistema
- 💸 Registro de receitas e despesas
- 🗂️ Estrutura modular (config, services e telegram_bot)

### 🔜 Planejadas
- 📊 Relatórios e resumos mensais
- 🏷️ Categorias de gastos
- 🎯 Metas financeiras
- 📈 Gráficos e visualização de dados
- ➕ Outras melhorias que forem surgindo

---

## 🛠️ Tecnologias Utilizadas

- Python
- API do Telegram (bot)
- JSON (configuração e credenciais)

---

## 📂 Estrutura do Projeto

```
📁 GerenciadorDeFinançasPessoais
 ┣ 📁 config          → configurações do projeto
 ┣ 📁 services        → lógica e serviços da aplicação
 ┣ 📁 telegram_bot    → código do bot do Telegram
 ┣ 📄 main.py         → arquivo principal (ponto de entrada)
 ┗ 📄 README.md
```

---

## ⚙️ Como Executar o Projeto

### 🔹 Pré-requisitos

- Python 3.10 ou superior
- Uma conta no Telegram e um token de bot (criado pelo [@BotFather](https://t.me/BotFather))
- Arquivo de credenciais próprio (`credenciais.json`)

### 🔹 Passo a passo

```bash
# Clone o repositório
git clone https://github.com/Rennan-rrm/GerenciadorDeFinan-asPessoais.git

# Acesse a pasta
cd GerenciadorDeFinan-asPessoais

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
python main.py
```

> 💡 Como o projeto está em evolução, os passos de instalação e as dependências podem mudar nas próximas versões.

---

## 🔐 Credenciais e Segurança

O projeto utiliza um arquivo de credenciais (`credenciais.json`) e o token do bot do Telegram.

- **Nunca** compartilhe suas credenciais ou seu token publicamente.
- Adicione o arquivo ao `.gitignore` para que ele não seja enviado ao GitHub:

```
credenciais.json
```

---

## 🎯 Objetivo

Este projeto está sendo desenvolvido para:

- Praticar lógica de programação e organização de código em Python
- Construir uma ferramenta útil para o controle financeiro pessoal
- Aprender a integrar um bot do Telegram a uma aplicação
- Servir como projeto de portfólio, evoluindo a cada nova versão

---

## 🤝 Contribuições

Como o projeto ainda está em fase inicial, sugestões e ideias são bem-vindas! Sinta-se à vontade para abrir uma *issue*.

---

## 👨‍💻 Autor

**Rennan Rodrigues**
Desenvolvedor em formação, apaixonado por tecnologia.

🔗 [GitHub — Rennan-rrm](https://github.com/Rennan-rrm)

---

⭐ Se gostou do projeto, deixe uma estrela e acompanhe as próximas atualizações!
