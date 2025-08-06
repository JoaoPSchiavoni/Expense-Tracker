'''O aplicativo deve ser executado a partir da linha de comando e deve ter os seguintes recursos:
Os usuários podem adicionar uma despesa com uma descrição e valor. /\/\\/\/\/\//\/\/\/\/\
Os usuários podem atualizar uma despesa.
Os usuários podem excluir uma despesa.
Os usuários podem visualizar todas as despesas.
Os usuários podem visualizar um resumo de todas as despesas.
Os usuários podem visualizar um resumo das despesas para um mês específico (do ano atual).'''
import json
from datetime import datetime
def despesas(description, value):

    try:
        expenses = {
            "Descrição": description,
            "Valor": value,
            "Data": datetime.now().strftime("%d/%m/%Y")
        }
        with open("expensesData.json", "w", encoding="utf-8") as file:
            json.dump(expenses, file, ensure_ascii=False, indent=4)
        print("Despesa cadastrada com sucesso!".center(40))
    except:
        print("Ocorreu um erro durante o registro.")

despesas("gasto", 230)
