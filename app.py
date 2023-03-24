from time import sleep
import psycopg2
import psycopg2.extras
import funcoes as fn
import pyinputplus as inp

fn.limpa_tela()

ls = "-" * 60

data: str = ""
plano_conta: str = ""
complemento = ""
valor = ""
codigo_forma_pagamento = ""  # 1=Dinheiro   2=Nubank   3=Inter   4=Bradesco

print("Forma de utilizar:")
print(ls)
print("A = 55 = ALIMENTACAO")
print("F = 49 = FILHAS")
print("T = 51 = TRANSPORTE")
print("R = 54 = REMEDIOS")
print("N = 50 = ANA")
print("O = 52 = OUTRAS")
print("C = 48 = CASA")
print("U = 43 = CASA MATERIAL DE CONSTRUÇÃO")
print(ls)
print("Data: três de dezembro de dois mil e vinte dois")
print("Plano de conta: alimentação")
print("Complemento: frutas")
print("Valor: vinte e dois vírgula cinquenta e três")
print("Código da forma de pagamento: dois")
print(ls)

while True:
    data = inp.inputDate(prompt="Data: ", blank=True, applyFunc=fn.converte_float)
    plano_conta = inp.inputStr(prompt="Plano de conta: ", blank=True)
    complemento = inp.inputStr(prompt="Complemento: ", blank=True)
    valor = inp.inputFloat(prompt="Valor: ", blank=True, applyFunc=fn.converte_float)
    codigo_forma_pagamento = inp.inputInt(prompt="Código da forma de pagamento: ", blank=True)

    if data == "" and plano_conta == "" and complemento == "" and \
            valor == "" and codigo_forma_pagamento == "":
        fn.mensagem("Fim do aplicativo.", 0)
        break
    else:
        print(ls)

        print("Data:", fn.converte_data_sql(data))
        print("Plano de conta:", plano_conta)
        print("Complemento:", complemento)
        print("Valor:", valor)
        print("Código da forma de pagamento:", codigo_forma_pagamento)

        print(ls)

        if data == "" or plano_conta == "" or complemento == "" or \
            valor == "" or codigo_forma_pagamento == "":
            fn.mensagem("Dados inválidos.", 3)
            continue

        conexao = psycopg2.connect(host="127.0.0.1", port="5436", database="simplesvarejo", user="postgres", password="Mpvpr@8@8282@1@RCPNMGPOVP")
        cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql01 = ""
        consulta01 = None

        # 1 = Marcio
        codigo_usuario = 1

        sql01 = "SELECT codigo FROM plano_conta_tesouraria WHERE upper(to_ascii(descricao)) LIKE upper(to_ascii('" + plano_conta + "%')) ORDER BY descricao LIMIT 1;"
        cursor.execute(sql01)
        consulta01 = cursor.fetchone()
        if not consulta01:
            fn.mensagem("Plano de conta não encontrado. Tente novamente.", 5)
            continue
        codigo_plano_conta = consulta01["codigo"]

        sql01 = """
            INSERT INTO
                lancamento_tesouraria
            (
                data, codigo_plano_conta_tesouraria, codigo_historico,
                complemento, valor, codigo_usuario
            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s
            );
        """
        cursor.execute(sql01, (fn.converte_data_sql(data), codigo_plano_conta, 1, complemento, valor, codigo_usuario))

        sql01 = "SELECT max(numero_controle) as ultimo FROM lancamento_tesouraria;"
        cursor.execute(sql01)
        consulta01 = cursor.fetchone()
        numero_controle = consulta01["ultimo"]

        sql01 = """
            INSERT INTO
                lancamento_tesouraria_composicao
            (
                numero_controle, numero_ordem_composicao, codigo_forma_pagamento,
                valor, codigo_usuario
            )
            VALUES
            (
                %s, %s, %s, %s, %s
            );
        """
        cursor.execute(sql01, (numero_controle, 1, codigo_forma_pagamento, valor, codigo_usuario))

        conexao.commit()

        cursor.close()
        conexao.close()
