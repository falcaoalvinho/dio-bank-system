import Cliente
import Caixa
import Conta
import os

# Função que exibe o menu de operações
def operacoes(conta: Conta.conta) -> None:
    print(f'{conta.numero_conta}'.center(60, "="))
    print('''
        1) Depositar
        2) Sacar
        3) Gerar extrato
    ''')
    print('=' * 60)

def iniciar() -> None:
    print('Bem-Vindo'.center(60, '='))
    print('''
        1) Entrar
        2) Cadastrar
        3) Sair
    ''')
    print('=' * 60)

def login() -> None:
    print('Login'.center(60, '='))
    print('''
        Por favor, digite seu CPF para efetuar o login
          ou aperte enter para sair
    ''')
    print('=' * 60)
    
def cadastro(sistema: Caixa.sistema) -> None:
    print('Cadasto'.center(60, '='))
    nome: str = input('Nome: ')
    data_nascimento: str = input('Data nascimento: ') 
    cpf: str = input('CPF: ')
    endereco: str = input('Endereço: ')
    print('=' * 60)
    sistema.cadastrarCliente(Cliente.cliente(nome= nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco))
    
def contas(cliente: Cliente.cliente, sistema: Caixa.sistema) -> int:
    # os.system('cls')
    print(f'Contas de {cliente.nome}'.center(60, '='))

    print()
    for conta in cliente.contas:
        print(f'Conta: {conta.numero_conta}')

    print('\nAperte [ENTER] para cadastrar uma conta')
    entrada_contas = input('Selecione uma conta: ')

    if entrada_contas != '':
        print('=' * 60)
        return int(entrada_contas)
    
    else: 
        # os.system('cls')
        sistema.cadastrarConta(cliente)
        print('=' * 60)
        return contas(cliente=cliente, sistema=sistema)
    