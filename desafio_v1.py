def exibir_menu():
    menu = """
================ BANCO PYTHON ================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    return input(menu).lower()


def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n✅ Depósito realizado com sucesso!")

        else:
            print("\n❌ O valor do depósito deve ser maior que zero.")

    except ValueError:
        print("\n❌ Digite um valor numérico válido.")

    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\n❌ Saldo insuficiente.")

        elif excedeu_limite:
            print(f"\n❌ O limite por saque é de R$ {limite:.2f}.")

        elif excedeu_saques:
            print("\n❌ Número máximo de saques atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            print("\n✅ Saque realizado com sucesso!")

        else:
            print("\n❌ O valor informado é inválido.")

    except ValueError:
        print("\n❌ Digite um valor numérico válido.")

    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")

    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print(extrato)

    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=========================================")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo,
                extrato,
                numero_saques,
                limite,
                LIMITE_SAQUES
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "q":
            print("\n👋 Obrigada por usar o Banco Python!")
            break

        else:
            print("\n❌ Operação inválida. Escolha uma opção do menu.")