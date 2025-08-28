def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n Saldo insuficiente.")
    elif valor > limite:
        print("\n Valor excede o limite de saque.")
    elif numero_saques >= limite_saques:
        print("\n Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    else:
        print("\n Valor inválido para saque.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    if extrato:
        for item in extrato:
            print(item)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================")


def cadastrar_cliente(clientes, nome, cpf, endereco):
    if cpf in clientes:
        print("\n Já existe cliente com esse CPF.")
    else:
        clientes[cpf] = {"nome": nome, "endereco": endereco}
        print("\n Cliente cadastrado com sucesso!")
    return clientes



def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    limite_saques = 3
    clientes = {}

    while True:
        print("""
========= MENU =========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[0] Sair
========================
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Digite o valor para saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            endereco = input("Endereço do cliente: ")
            clientes = cadastrar_cliente(clientes, nome, cpf, endereco)

        elif opcao == "0":
            print("\n Saindo do sistema bancário")
            break

        else:
            print("\n Opção inválida! Tente novamente.")


main()
