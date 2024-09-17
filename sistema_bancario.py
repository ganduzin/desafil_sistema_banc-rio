import datetime


menu_acesso = """
[u] Cadastrar Usuário
[n] Nova conta
[c] Selecionar Conta
[q] Sair

=> """

menu_conta = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

dict_usuarios = {}
dict_contas = {}
numero_conta = 1
limite = 500
extrato = ""
LIMITE_SAQUES = 3

def criar_usuario(nome, data_nascimento, cpf, endereco):
    if cpf in dict_usuarios:
        print("Usuário já existe")
    else:
        usuario = {}
        usuario["nome"] = nome
        usuario["data_nascimento"] = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        usuario["endereco"] = endereco
        usuario["contas"] = []
        dict_usuarios[cpf] = usuario
        print("Usuário criado com sucesso\n")

def criar_conta(numero_conta, cpf, valor_inicial):
    if not dict_usuarios.keys:
        print("Você precisa se cadastrar antes")
    else:
        conta = {}
        conta["saldo"] = float(valor_inicial)
        conta["usuario"] = cpf
        conta["numero_saques"] = 0
        conta["extrato"] = extrato
        dict_usuarios[cpf]["contas"] += f"{numero_conta}"
        dict_contas[str(numero_conta)] = conta
        print(f"Conta {numero_conta} criada com sucesso.")
        numero_conta += 1
    

def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > dict_contas[conta]["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = dict_contas[conta]["numero_saques"] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        dict_contas[conta]["saldo"] -= valor
        dict_contas[conta]["extrato"]  += f"Saque: R$ {valor:.2f}\n"
        dict_contas[conta]["numero_saques"] += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        dict_contas[conta]["saldo"] += valor
        dict_contas[conta]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
def tirar_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not dict_contas[conta]["extrato"] else dict_contas[conta]["extrato"])
    print(f"\nSaldo: R$ {dict_contas[conta]['saldo']:.2f}")
    print("==========================================")



while True:

    
    opcao_acesso = input(menu_acesso)
    if opcao_acesso == "u":
        cpf = input("Digite seu CPF: ")
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Enderaço: ")
        criar_usuario(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
        valor_inicial = input("Digite o valor inicial de sua conta: ")
        criar_conta(numero_conta=numero_conta, cpf=cpf, valor_inicial=valor_inicial)
    elif opcao_acesso == "n":
        valor_inicial = "Digite o valor inicial de sua conta: "
        criar_conta(numero_conta=numero_conta, cpf=cpf, valor_inicial=valor_inicial)
    elif opcao_acesso == "c":
        if dict_usuarios[cpf]["contas"]:
            print(f"Você possui as seguintes contas: {dict_usuarios[cpf]['contas']}")
            conta_ativa = input("Digite a conta que deseja utilizar: ")
            if conta_ativa in dict_usuarios[cpf]['contas']:
                while True:
                    opcao_conta = input(menu_conta)
                    if opcao_conta == "d":
                        depositar(conta_ativa)
                    elif opcao_conta == "s":
                        sacar(conta_ativa)
                    elif opcao_conta == "e":
                        tirar_extrato(conta_ativa)
                    elif opcao_conta == "q":
                        break
                    else:
                        print("Operação inválida, por favor selecione novamente a operação desejada.") 
        else:
            print("Você ainda não possui contas")
    elif opcao_conta == "q":
                    break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")