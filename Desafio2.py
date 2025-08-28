clientes = []
contas = []

def cadastrar_cliente(nome, cpf, endereco):
    cliente = {"nome": nome, "cpf": cpf, "endereco": endereco}
    clientes.append(cliente)
    return cliente

def criar_conta(cliente):
    conta = {"agencia": "0001", "numero": len(contas) + 1, "cliente": cliente, "saldo": 0, "extrato": []}
    contas.append(conta)
    return conta

def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        return True
    return False

def sacar(conta, valor, limite=500, limite_saques=3):
    saques_realizados = sum(1 for op in conta["extrato"] if "Saque" in op)
    if valor > conta["saldo"] or valor > limite or saques_realizados >= limite_saques or valor <= 0:
        return False
    conta["saldo"] -= valor
    conta["extrato"].append(f"Saque: R$ {valor:.2f}")
    return True

def exibir_extrato(conta):
    for op in conta["extrato"]:
        print(op)
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")

cliente1 = cadastrar_cliente("João Silva", "12345678900", "Rua A, 123")
conta1 = criar_conta(cliente1)

depositar(conta1, 1000)
sacar(conta1, 200)
exibir_extrato(conta1)
