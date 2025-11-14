from behave import given, when, then
from pages.home_page import HomePage
from pages.elements_page import ElementsPage
from pages.webtables_page import WebTablesPage
import time


@given("que estou na página Web Tables do DemoQA")
def step_go_to_web_tables_page(context):
    context.home_page = HomePage(context.driver)
    context.elements_page = ElementsPage(context.driver)
    context.webtables_page = WebTablesPage(context.driver)

    context.home_page.go_to_home()
    context.home_page.click_elements()
    context.elements_page.click_web_tables()


# ============================================================
#   CENÁRIO PADRÃO – CRIAR / EDITAR / DELETAR 1 REGISTRO
# ============================================================

@when("eu crio um novo registro")
def step_create_single_record(context):
    data = {
        "first_name": "Ana",
        "last_name": "Silva",
        "email": "ana.silva@example.com",
        "age": "30",
        "salary": "4500",
        "department": "QA"
    }
    context.webtables_page.create_record(**data)
    context.created_record = data


@then("o registro deve aparecer na tabela")
def step_verify_record_created(context):
    assert context.webtables_page.is_record_present(context.created_record["email"]) is True


@when("eu edito o registro criado")
def step_edit_record(context):
    new_data = {
        "first_name": "Ana Paula",
        "last_name": "Silva",
        "email": context.created_record["email"],
        "age": "31",
        "salary": "5500",
        "department": "Qualidade"
    }
    context.webtables_page.edit_record(context.created_record["email"], **new_data)
    context.created_record = new_data


@then("o registro deve ser atualizado na tabela")
def step_verify_record_edited(context):
    assert context.webtables_page.is_record_present(context.created_record["email"]) is True


@when("eu deleto o registro criado")
def step_delete_record(context):
    context.webtables_page.delete_record(context.created_record["email"])


@then("o registro não deve mais aparecer na tabela")
def step_verify_record_deleted(context):
    assert context.webtables_page.is_record_present(context.created_record["email"]) is False


# ============================================================
#   CENÁRIO BÔNUS – CRIAR 12 REGISTROS DINAMICAMENTE
# ============================================================

@when("eu crio {total:d} registros dinamicamente")
def step_create_multiple_records(context, total):
    context.created_records = []

    for i in range(total):
        data = {
            "first_name": f"User{i}",
            "last_name": "Test",
            "email": f"user{i}@example.com",
            "age": str(20 + i),
            "salary": str(3000 + i * 100),
            "department": "QA"
        }

        context.webtables_page.create_record(**data)
        context.created_records.append(data)

        time.sleep(0.3)   # Apenas para visualização no GIF (opcional)


@then("todos os registros criados devem aparecer na tabela")
def step_verify_multiple_records_created(context):
    for record in context.created_records:
        assert context.webtables_page.is_record_present(record["email"]) is True


# ============================================================
#   CENÁRIO BÔNUS – DELETAR TODOS OS REGISTROS CRIADOS
# ============================================================

@when("eu deleto todos os registros criados")
def step_delete_all_records(context):
    for record in context.created_records:
        context.webtables_page.delete_record(record["email"])
        time.sleep(0.2)  # Apenas para visualização


@then("nenhum dos registros criados deve permanecer na tabela")
def step_verify_all_records_deleted(context):
    for record in context.created_records:
        assert context.webtables_page.is_record_present(record["email"]) is False
