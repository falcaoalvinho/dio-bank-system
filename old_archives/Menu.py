# Imports do arquivo
from Caixa import sistema
from Conta import conta
from Cliente import cliente

# Função que exibe o menu inicial (1º loop)
def iniciar() -> None:
    print('Bem-Vindo'.center(60, '='))
    print('''
        1) Entrar
        2) Cadastrar
        3) Sair
    ''')
    print('=' * 60)

# Função que exibe tela de entrada do cpf no login (1º loop)
def login() -> None:
    print('Login'.center(60, '='))
    print('''
        Por favor, digite seu CPF para efetuar o login
          ou aperte enter para sair
    ''')
    print('=' * 60)

# Função que exibe formulário de entrada dos dados do cliente (1º loop)
def cadastro(sistema: sistema) -> None:
    print('Cadasto'.center(60, '='))

    nome: str = input('Nome: ')
    data_nascimento: str = input('Data nascimento: ') 
    cpf: str = input('CPF: ')
    endereco: str = input('Endereço: ')

    print('=' * 60)

    sistema.cadastrarCliente(cliente(nome= nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco))

# Função que exibe lista de contas do usuário que efetuar login (2º loop)
def contas(cliente: cliente, sistema: sistema) -> int:
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
        sistema.cadastrarConta(cliente)
        print('=' * 60)
        return contas(cliente=cliente, sistema=sistema)
    
# Função que exibe o menu de operações (3º loop)
def operacoes(conta: conta) -> None:
    print(f'Conta Nº: {conta.numero_conta}'.center(60, "="))
    print('''
        1) Depositar
        2) Sacar
        3) Gerar extrato
    ''')
    print('=' * 60)