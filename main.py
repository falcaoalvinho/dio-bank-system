# Pacotes importados para o projeto
import os
import Menu

# Constantes para Cores 
# VERMELHO = '\033[31m'
# AMARELO = '\033[33m'
# VERDE = '\033[32m'
# FIM_COR = '\033m'

def contarCedulas(cedulas: dict) -> int:
    valor = 0

    for i in cedulas:
        valor += int(i) * cedulas[i]

    return valor

def depositar(cedulas: dict, saldo: int) -> {str, int}:
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
                cedulas_depositadas[i] += int(input(f'Cédulas no valor de {i}: ')) 
                cedulas[i] += cedulas_depositadas[i]

    valor_deposito = contarCedulas(cedulas_depositadas)
    saldo += valor_deposito

    print(f'\n    Saldo total: {saldo}')
    print(f'    Valor total do deposito: {valor_deposito}')
    os.system('cls')

    return {'valor_deposito': f'\n    +{valor_deposito}', 'valor_saldo': saldo}

def sacar(cedulas: dict, saldo: int, LIMITE_SAQUE: float) -> {str, int}:
    cedulas_usadas = {'200': 0, '100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0 }

    print('SAQUE'.center(60, '='))
    print(f'   SAQUE MÁXIMO: {LIMITE_SAQUE}')
    print(f'   Saldo disponível: {saldo}')

    try:
        saque = int(input('\n   Digite o valor do saque: '))
        valor_saque = saque

    except ValueError:
        print('\n🚫[ERRO]Valor incorreto, por favor retorne um valor válido\n')
        print(f'\n{'='*60}')
        sacar(cedulas, saldo, LIMITE_SAQUE)

    else:
        if saque <= saldo and saque <= LIMITE_SAQUE:
            for i in cedulas:
                cedulas[i] -= saque // int(i)
                cedulas_usadas[i] += saque // int(i)
                saque -= int(i) * (saque // int(i))

        else:
            print('\n🚫[ERRO] Valor do saque excedeu o limite, por favor tente denovo')
            print(f'\n{'='*60}')
            sacar(cedulas, saldo, LIMITE_SAQUE)

    print(cedulas_usadas)
    saldo -= contarCedulas(cedulas_usadas)
    
    os.system('cls')
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

    # Começo da construção do extrato
    extrato = 'EXTRATO'.center(60, '=')
    extrato += f'\nSALDO INICIAL: {saldo}'
    
    while True:
        os.system('cls')
        Menu.printOpercoes()

        try:
            operacao_atual = int(input())

        except ValueError:
            print('🚫[ERRO] Valor incorreto, por favor retorne um valor válido')

        else:
            if operacao_atual == 1:
                os.system('cls') # Limpa o terminal
                resultado = depositar(cedulas, saldo)
                extrato += resultado['valor_deposito']
                saldo = resultado['valor_saldo']

            elif operacao_atual == 2 and saques_efetuados >= SAQUES_DIARIOS:
                print('\n🚫[ERRO] Limite de saques diários atingido\n')

            elif operacao_atual == 2:
                saques_efetuados += 1
                os.system('cls') # Limpa o terminal
                resultado = sacar(cedulas, saldo, LIMITE_SAQUE)
                extrato += resultado['valor_saque']
                saldo = resultado['valor_saldo']
                
            elif operacao_atual == 3:
                os.system('cls') # Limpa o terminal
                extrato += f'\nSALDO FINAL: {saldo}'
                extrato += f'\n{'='*60}'
                print(extrato)
                break
main()