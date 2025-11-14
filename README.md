 Desafio 2 - Accenture

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

✅ Seção para adicionar no README – Cenário Bônus (Dinâmico)
⭐ Cenário Bônus – Criação e Exclusão Dinâmica de 12 Registros

Além do fluxo principal, este projeto também inclui um cenário bônus, onde testamos a capacidade do sistema de lidar com múltiplos registros sendo criados e removidos de forma dinâmica.

Esse cenário foi implementado utilizando Selenium + Python + Behave (Cucumber BDD) e funciona como um excelente teste de estresse para a tabela dinâmica do DemoQA.

🎯 Objetivo do Cenário Bônus

Criar 12 registros automaticamente, cada um com dados únicos.

Validar que todos aparecem corretamente na tabela.

Deletar todos os registros criados.

Confirmar que nenhum registro resta na tabela.

🧪 Cenário Bônus (Gherkin)
Scenario: Criar e deletar 12 registros dinamicamente
    Given que estou na página Web Tables do DemoQA
    When eu crio 12 registros dinamicamente
    Then todos os registros criados devem aparecer na tabela
    When eu deleto todos os registros criados
    Then nenhum dos registros criados deve permanecer na tabela

🧩 Onde está implementado?
✔ Steps:

steps/webtables_steps.py

step_create_multiple_records()

step_delete_all_records()

Validadores correspondentes.

✔ Page Object:

pages/webtables_page.py

create_record()

is_record_present()

delete_record()

▶ Demonstração (GIF ou Imagens)

📌 Opcional, mas recomendado:
Adicione GIFs ou capturas de tela mostrando a criação dos 12 registros em sequência.
Coloque algo assim:

## 🎬 Demonstração do Cenário Bônus

📌 Criação automática dos 12 registros:

![Criação dos registros](docs/gif/create_12_records.gif)

📌 Exclusão automática dos registros:

![Exclusão dos registros](docs/gif/delete_12_records.gif)


Se quiser, eu posso até gerar um GIF fake ilustrativo pra você usar.

🧠 Por que esse cenário é importante?

Testa resiliência da interface em operações repetidas.

Garante que o sistema mantém funcionamento mesmo com alto volume de dados.

Ajuda a validar que a tabela não quebra com múltiplas inserções e exclusões.

Demonstrando domínio de cenários dinâmicos no Cucumber (Behave).
