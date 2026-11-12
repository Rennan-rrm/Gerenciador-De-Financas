from datetime import date
import gspread

# 1. Autenticar com o Google
cliente = gspread.service_account(
    filename="credenciais.json"
)

# 2. Abrir a planilha pelo nome
planilha = cliente.open("Financeiro Rennan")

def registrar_gastos(id, valor, descricao):
    # 3. Selecionar a primeira aba
    aba = planilha.sheet1

    # 4. Enviar os dados
    valor= valor
    descricao = descricao
    dia_compra = date.today()
    data = dia_compra.strftime("%d/%m/%Y")

    dados = [
        data,
        descricao,
        valor
    ]
    aba.append_row(dados)
    return "Dados enviados com sucesso!"


def resumo():

    aba = planilha.sheet1
    dados = aba.get_all_records()

    




