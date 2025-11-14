# Lilian-Farina---Accenture

# DemoQA Selenium Automation (Python + Page Objects)

Projeto completo automatizando 5 fluxos do site https://demoqa.com utilizando:

- Selenium WebDriver
- Page Object Pattern
- Pytest
- GitHub Actions CI
- Faker para dados aleatórios

## 📁 Estrutura do Projeto
```
selenium-demoqa-automation/
├── data/
│   └── upload_example.txt
├── pages/
├── tests/
├── utils/
├── requirements.txt
└── README.md
```

## ▶️ Executar o Projeto

### 1. Instalar dependências
```
pip install -r requirements.txt
```

### 2. Executar todos os testes
```
pytest -v
```

## 🚀 CI/CD – GitHub Actions
O workflow executa automaticamente os testes a cada push ou pull request.

---

## 🧪 Cenários Automatizados

### 1 — Forms → Practice Form
- Preencher formulário
- Upload de arquivo `.txt`
- Submeter formulário
- Validar popup

### 2 — Browser Windows
- Abrir nova janela
- Validar mensagem
- Fechar janela

### 3 — Web Tables
- Criar registro
- Editar registro
- Deletar registro

### 4 — Progress Bar
- Iniciar
- Parar antes de 25%
- Resetar ao final

### 5 — Sortable
- Ordenar lista por drag & drop

---

## 🥒 BDD (Cucumber Gherkin)

Os cenários completos estão na pasta `bdd/features`.


