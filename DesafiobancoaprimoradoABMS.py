AGENCIA = "0001"
LIMITE_SAQUES = 3

usuarios = []
contas = []

def sacar(*, saldo, valor, extrato, limite, numero_saques):
    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print("❌ Valor excede o limite por saque.")
    elif numero_saques >= LIMITE_SAQUES:
        print("❌ Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")
    else:
        print("⚠️ Valor inválido para saque.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("⚠️ Valor inválido para depósito.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("====================")

def cadastrar_usuario():
    cpf = input("Informe o CPF (somente números): ").strip()
    if any(u["cpf"] == cpf for u in usuarios):
        print("⚠️ Já existe usuário com esse CPF.")
        return

    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Endereço (logradouro, nro, bairro, cidade/UF): ").strip()

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("✅ Usuário cadastrado com sucesso!")

def encontrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cadastrar_conta():
    cpf = input("CPF do titular da conta: ").strip()
    usuario = encontrar_usuario(cpf)
    if not usuario:
        print("❌ Usuário não encontrado. Cadastre o usuário antes.")
        return

    numero_conta = len(contas) + 1
    conta = {"agencia": AGENCIA, "numero": numero_conta, "usuario": usuario}
    contas.append(conta)
    print(f"✅ Conta criada com sucesso! Agência: {AGENCIA}, Número: {numero_conta}")

def menu():
    print("""
===== BANCO ABMS =====
[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar usuário
[c] Criar conta
[q] Sair
""")

# Variáveis de conta corrente ativa (padrão)
saldo = 0
limite = 500
extrato = ""
numero_saques = 0

while True:
    menu()
    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        cadastrar_usuario()

    elif opcao == "c":
        cadastrar_conta()

    elif opcao == "q":
        print("👋 Obrigado por usar o Banco ABMS!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
