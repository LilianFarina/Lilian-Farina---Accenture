Feature: DemoQA Automation

  Scenario: Preencher form com sucesso
    Given que o usuário está na Home do DemoQA
    When acessa Forms e Practice Form
    And preenche o formulário com dados válidos
    And envia o formulário
    Then o popup de confirmação deve aparecer

  Scenario: Abrir e validar nova janela
    Given que o usuário está no DemoQA
    When acessa Alerts, Frame & Windows e Browser Windows
    And clica em New Window
    Then uma nova janela deve abrir com a mensagem "This is a sample page"

  Scenario: Criar editar e deletar registro na WebTable
    Given que o usuário está no DemoQA
    When acessa Elements e WebTables
    And cria um novo registro
    And edita o registro criado
    And exclui o registro criado
    Then o registro deve ser removido da lista

  Scenario: Controlar Progress Bar
    Given que o usuário está no DemoQA
    When acessa Widgets e ProgressBar
    And inicia o progresso
    Then deve parar antes dos 25%
    When iniciar novamente
    Then deve chegar ao 100% e resetar

  Scenario: Ordenar lista Sortable
    Given que o usuário está no DemoQA
    When acessa Interactions e Sortable
    Then deve ordenar os itens em ordem crescente


