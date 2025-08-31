from abc import ABC, abstractmethod
from datetime import date

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def __str__(self):
        extrato = "\n".join([str(t) for t in self.transacoes])
        return extrato if extrato else "Nenhuma movimentação registrada."


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f"Depósito: R$ {self.valor:.2f}"


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f"Saque: R$ {self.valor:.2f}"


class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3, agencia="0001"):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > self.limite:
            print("Saque acima do limite diário.")
            return False
        if self.numero_saques >= self.limite_saques:
            print("Número máximo de saques atingido.")
            return False
        if super().sacar(valor):
            self.numero_saques += 1
            return True
        return False


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


def menu():
    return """
========= MENU =========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[5] Criar Conta
[6] Listar Contas
[0] Sair
========================
"""


def main():
    clientes = []
    contas = []
    numero_conta = 1

    while True:
        print(menu())
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            valor = float(input("Digite o valor para depósito: R$ "))
            conta = cliente.contas[0]
            cliente.realizar_transacao(conta, Deposito(valor))

        elif opcao == "2":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            valor = float(input("Digite o valor para saque: R$ "))
            conta = cliente.contas[0]
            cliente.realizar_transacao(conta, Saque(valor))

        elif opcao == "3":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            conta = cliente.contas[0]
            print("\n========== EXTRATO ==========")
            print(conta.historico)
            print(f"\nSaldo atual: R$ {conta.saldo_atual():.2f}")
            print("=============================")

        elif opcao == "4":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            endereco = input("Endereço: ")
            cliente = PessoaFisica(nome, cpf, date.fromisoformat(nascimento), endereco)
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso.")

        elif opcao == "5":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            conta = ContaCorrente(cliente, numero_conta)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            numero_conta += 1
            print("Conta criada com sucesso.")

        elif opcao == "6":
            for conta in contas:
                print(f"Agência: {conta.agencia} | Número: {conta.numero} | Cliente: {conta.cliente.nome}")

        elif opcao == "0":
            print("Saindo do sistema bancário.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
