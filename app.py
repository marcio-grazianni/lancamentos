# import psycopg2
# import psycopg2.extras
import funcoes as fn
import pyinputplus as inp

fn.limpa_tela()

ls = "-" * 60

data: str = ""
plano_conta: str = ""
complemento = ""
valor = ""
codigo_forma_pagamento = ""  # 1=Dinheiro   2=Nubank   3=Inter   4=Bradesco
# Forma de utilizar:
# três de dezembro de dois mil e vinte dois
# alimentação
# frutas
# dois
data = inp.inputDate(prompt="Data: ", blank=True)
plano_conta = inp.inputStr(prompt="Plano de conta: ", blank=True)
complemento = inp.inputStr(prompt="Complemento: ", blank=True)
valor = inp.inputFloat(prompt="Valor: ", blank=True, applyFunc=fn.converte_float)
codigo_forma_pagamento = inp.inputInt(prompt="Código da forma de pagamento: ", blank=True)

if data == "" or plano_conta == "" or complemento == "" or \
        valor == "" or codigo_forma_pagamento == "":
    print(ls)
    print("Dados inválidos.")
    print(ls)
else:
    print(ls)

    print("Data:", data)
    print("Plano de conta:", plano_conta)
    print("Complemento:", complemento)
    print("Valor:", valor)
    print("Código da forma de pagamento:", codigo_forma_pagamento)

    print(ls)

# else:
#     ls = "-" * 60
#     sql01 = ""
#     consulta01 = None

#     # 1 = Marcio
#     codigo_usuario = 1
#     # 2 = nubank   3 = inter
#     planilha = pd.read_excel(caminho_planilha).to_dict(orient="records")
#     conexao = psycopg2.connect(host="127.0.0.1", port="5436", database="simplesvarejo", user="postgres", password="Mpvpr@8@8282@1@RCPNMGPOVP")
#     cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

#     for linha in planilha:
#         if (linha["Tipo"] != "P" or len(linha["Tipo"]) != 1):
#             sql01 = """
#                 INSERT INTO
#                     lancamento_tesouraria
#                 (
#                     data, codigo_plano_conta_tesouraria, codigo_historico,
#                     complemento, valor, codigo_usuario
#                 )
#                 VALUES
#                 (
#                     %s, %s, %s, %s, %s, %s
#                 );
#             """
#             cursor.execute(sql01, (fn.converte_data_sql(linha["Data"]), fn.retorna_plano_conta(linha["Tipo"]), 1, linha["Descrição"], linha["Valor"], codigo_usuario))

#             sql01 = "SELECT max(numero_controle) as ultimo FROM lancamento_tesouraria;"
#             cursor.execute(sql01)
#             consulta01 = cursor.fetchone()
#             numero_controle = consulta01["ultimo"]

#             sql01 = """
#                 INSERT INTO
#                     lancamento_tesouraria_composicao
#                 (
#                     numero_controle, numero_ordem_composicao, codigo_forma_pagamento,
#                     valor, codigo_usuario
#                 )
#                 VALUES
#                 (
#                     %s, %s, %s, %s, %s
#                 );
#             """
#             cursor.execute(sql01, (numero_controle, 1, codigo_forma_pagamento, linha["Valor"], codigo_usuario))

#     conexao.commit()

#     cursor.close()
#     conexao.close()
