# AutoFlow Lili 🤖

## 📌 Descrição

O **AutoFlow Lili** é um chatbot desenvolvido em Python utilizando a API do **Google Gemini**.

A Lili é uma assistente virtual da plataforma fictícia **AutoFlow**, uma plataforma corporativa de gravação inteligente e automação de testes.

O projeto foi desenvolvido a partir do exemplo de chatbot apresentado pela **DeepLearning.AI**, adaptando a personalidade, o objetivo e o conhecimento do chatbot para o contexto da AutoFlow.

A Lili foi configurada para:

* Responder dúvidas sobre a plataforma AutoFlow;
* Explicar o funcionamento da gravação inteligente;
* Orientar sobre os ambientes de execução;
* Explicar o uso de Gherkin na plataforma;
* Informar sobre massas de teste e integração com Azure DevOps;
* Orientar sobre abertura de chamados;
* Evitar a criação de informações que não estejam presentes em seu conhecimento.

Ao final de três perguntas, o sistema também gera um **resumo do atendimento** realizado.

---

## 🛠️ Tecnologias utilizadas

* Python
* Google Gemini API
* Google Gen AI SDK
* python-dotenv

---

## 📂 Estrutura do projeto

```text
AutoFlow-Lili/
├── main.py
├── README.md
├── env.example
├── .gitignore
└── requirements.txt
```

### Arquivos

**`main.py`**
Contém o código principal do chatbot, incluindo a configuração do Gemini, o prompt da Lili, o fluxo de perguntas e a geração do resumo.

**`env.example`**
Arquivo de exemplo contendo o nome da variável de ambiente necessária para executar o projeto.

**`requirements.txt`**
Contém as dependências necessárias para executar a aplicação.

**`.gitignore`**
Impede que arquivos como `.env` e arquivos temporários sejam enviados para o repositório.

---

## 🚀 Como executar o projeto

### 1. Pré-requisitos

É necessário ter instalado:

* Python 3;
* Git;
* Uma chave de API do Google Gemini.

---

### 2. Clonar o repositório

```bash
git clone https://github.com/LeticiaSanttos/AutoFlow-Lili.git
```

Depois, acesse a pasta do projeto:

```bash
cd AutoFlow-Lili
```

---

### 3. Criar um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
.venv\Scripts\activate
```

---

### 4. Instalar as dependências

Execute:

```bash
pip install -r requirements.txt
```

---

### 5. Configurar a chave da API

Crie um arquivo chamado:

```text
.env
```

na raiz do projeto.

Utilize o arquivo `env.example` como referência e configure sua chave:

```env
GEMINI_API_KEY=sua_chave_aqui
```

> **Importante:** não compartilhe sua chave da API e não envie o arquivo `.env` para o GitHub.

---

### 6. Executar o chatbot

Com o ambiente virtual ativado, execute:

```bash
python main.py
```

O programa solicitará três perguntas ao usuário.

Exemplo:

```text
Você (1/3): Como funciona a gravação inteligente da AutoFlow?

Lili: [resposta da assistente]

Você (2/3): O Gherkin é utilizado para gerar automaticamente as automações?

Lili: [resposta da assistente]

Você (3/3): A AutoFlow possui integração com o Jira?

Lili: [resposta da assistente]
```

Após as três perguntas, a aplicação gera um resumo do atendimento.

---

## 🧪 Demonstração

Durante a execução, podem ser utilizadas perguntas para demonstrar diferentes comportamentos da Lili.

### Pergunta sobre uma funcionalidade conhecida

```text
Como funciona a gravação inteligente da AutoFlow?
```

A Lili deve responder utilizando as informações disponíveis sobre a plataforma.

### Pergunta sobre Gherkin

```text
O Gherkin é utilizado para gerar automaticamente as automações?
```

A Lili deve explicar que o Gherkin é utilizado para documentar e descrever os cenários, enquanto as automações são criadas a partir das interações capturadas durante a gravação.

### Teste de não alucinação

```text
A AutoFlow possui integração com o Jira?
```

Como essa informação não está presente no conhecimento fornecido à Lili, ela deve informar que não possui essa informação disponível, sem inventar uma resposta.

---

## 🔐 Segurança

A chave da API deve ser armazenada no arquivo `.env` e não deve ser publicada no repositório.

O arquivo `.env` está incluído no `.gitignore`.

Para configurar o projeto, utilize o `env.example`, que contém apenas o nome da variável necessária.

---

## 📹 Demonstração

Youtube: https://youtu.be/A4hswZs7EaU

---

## 📚 Referência

O desenvolvimento deste projeto teve como base o exemplo de chatbot apresentado no curso **ChatGPT Prompt Engineering for Developers**, da DeepLearning.AI.

https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/jtmdv/chatbot
