Saldo_Atual = 0
opcao = -1
Soma_Saque = 0
Limite_De_Saques = 0
Numero_de_saques = 3
Historico = []

while opcao != 0:
    print(""" 
          =================MENU====================
                    DIGITE[1] SAQUE
                    DIGITE[2] DEPOSITO
                    DIGITE[3] EXTRATO
                    DIGITE[0] SAIR
          ==========================================
""")
    opcao = int(input("Digite o numero de acordo com a transação bancaria que voce deseja fazer: "))

    if opcao == 1:
        if Limite_De_Saques >= Numero_de_saques:
            print("o numero limite de saques foi atingido")
        else:
            print(f"o seu saldo atual é de R$: {Saldo_Atual: .2f}")
            Saque = float(input("Digite o valor que voce deseja sacar: "))
        if Saldo_Atual >= Saque and Saque <= 500:
         Saldo_Atual = Saldo_Atual - Saque
         print(f"Retire o dinheiro no caixa, seu saldo atual é {Saldo_Atual}")
        elif Saldo_Atual < Saque:
             print("Operação bloqueada! Seu saque ultrapassa o valor do saldo disponivel na conta")
        elif Saque > 500:
            print("saque acima do seu limite diario(500)")

        Soma_Saque = Soma_Saque + Saque
        Limite_De_Saques += 1
        print(f"o saque total eh {Soma_Saque:.2f}")
        Historico.append(f"Saque de R$ {Saque:.2f}")

    elif opcao == 2:
        Deposito = float(input("Digite o valor que voce deseja depositar na sua conta: "))
        if Deposito > 0:
            Saldo_Atual = Saldo_Atual + Deposito
            Historico.append(f"Depósito de R$ {Deposito:.2f}")
            print (f"Voce depositou R$: {Deposito:.2f} e agora seu saldo atual é R$: {Saldo_Atual:.2f}")
        elif Deposito < 0:
            print("operação bloquada")        

    elif opcao == 3:
        print("""
    ==========EXTRATO BANCARIO========""")
        if not Historico:
            print("Nenhuma movimentação registrada.")
        else:
            for transação in Historico:
                print(transação)
        print(f"\nSaldo final: R$ {Saldo_Atual:.2f}")
        print("====================================\n")

    elif opcao == 0:
        print("Saindo do sistema... Obrigado por usar nosso banco!")
    else:
        print("Opção inválida, tente novamente.")

        
