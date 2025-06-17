# Pacotes importados para o projeto
import os

# Constantes para Cores 
# VERMELHO = '\033[31m'
# AMARELO = '\033[33m'
# VERDE = '\033[32m'
# FIM_COR = '\033m'

# Função que exibe o menu de operações
def printMenu() -> None:
    print('MENU'.center(60, "="))
    print(f'''
        1) Depositar
        2) Sacar
        3) Sair
    ''')
    print('=' * 60)

def contarCedulas(cedulas: dict) -> int:
    valor = 0
    for i in cedulas:
        valor += int(i) * cedulas[i]
    return valor

def deposito(cedulas: dict, saldo: int) -> str:
    cedulas_depositadas = {'200': 0, '100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0}

    print('DEPOSITO'.center(60, '='))
    
    for i in cedulas:
        while True:
            try:
                cedulas_depositadas[i] += int(input(f'Cédulas no valor de {i}: ')) 
                cedulas[i] += cedulas_depositadas[i]
                break
            except ValueError:
                print('\n   🚫[ERRO] Valor incorreto, por favor retorne um valor válido\n')

    valor_deposito = contarCedulas(cedulas_depositadas)
    saldo += valor_deposito

    print(f'\n    Saldo total: {saldo}')
    print(f'    Valor total do deposito: {valor_deposito}')

    return {'valor_deposito': f'\n    +{valor_deposito}', 'valor_saldo': saldo}

def saque(cedulas: dict, saldo: int) -> str:
    print('SAQUE'.center(60, '='))
    print(f'   Saldo disponível: {saldo}')

    while True:
        try:
            saque = int(input('\n   Digite o valor do saque: '))
            valor_saque = saque
        except ValueError:
            print('\n🚫[ERRO] Valor incorreto, por favor retorne um valor válido\n')
        else:
            if saque <= saldo:
                for i in cedulas:
                    cedulas[i] -= saque // int(i)
                    saque -= int(i) * (saque // int(i))
                    saldo -= int(i) * (saque // int(i))
                break
            else:
               print('\nValor indisponível para seu saldo') 

    return {'valor_saque': f'\n    -{valor_saque}', 'valor_saldo': saldo}

# Função principal
def main() -> None:
    # Constantes do caixa
    SAQUES_DIARIOS = 3
    LIMITE_SAQUE = 500

    # Variáveis do caixa
    cedulas = {'200': 10, '100': 10, '50': 10, '20': 10, '10': 10, '5': 10, '2': 10 }

    saldo = 1000
    saques_efetuados = 0

    extrato = 'EXTRATO'.center(60, '=')
    extrato += f'\nSALDO INICIAL: {saldo}'

    print(f'BANCO DIO'.center(60, '='), '\n')
    
    while True:
        printMenu()

        try:
            operacao_atual = int(input())
        except ValueError:
            print('🚫[ERRO] Valor incorreto, por favor retorne um valor válido')
        else:
            if operacao_atual == 1:
                os.system('cls') # Limpa o terminal
                resultado = deposito(cedulas, saldo)
                extrato += resultado['valor_deposito']
                saldo += resultado['valor_saldo']
            elif operacao_atual == 2 and saques_efetuados <= LIMITE_SAQUE:
                ++saques_efetuados
                os.system('cls') # Limpa o terminal
                resultado = saque(cedulas, saldo)
                extrato += resultado['valor_saque']
                saldo -= resultado['valor_saldo']
            elif operacao_atual == 3:
                os.system('cls') # Limpa o terminal
                extrato += f'\nSALDO FINAL: {saldo}'
                extrato += f'\n{'='*60}'
                print(extrato)
                break
main()