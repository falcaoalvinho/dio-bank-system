# Pacotes importados para o projeto
import os
import Menu
from Caixa import sistema
from Cliente import cliente
from Conta import conta

# Função principal
def main() -> int:
    caixa = sistema()
    entrada_cpf = ''
    entrada_conta = 0

    alan = cliente(nome='Alan', data_nascimento='01/01/2000', cpf='1010', endereco='Casa do Caralho')
    caixa.cadastrarCliente(alan)
    caixa.cadastrarConta(alan)

    while True:
        # os.system('cls')
        Menu.iniciar()

        try:
            entrada_iniciar = int(input())
        
        except ValueError:
            ('🚫[ERRO] Valor incorreto, por favor retorne um valor válido')

        else:
            if entrada_iniciar == 1:
                try:
                    # os.system('cls')
                    Menu.login()
                    entrada_cpf: str = input()

                except ValueError:
                    ('🚫[ERRO] Cadastro não encontrado')

                else:
                    if caixa.loginCliente(entrada_cpf):
                        break 

            elif entrada_iniciar == 2:
                # os.system('cls')
                Menu.cadastro(caixa)
            
            elif entrada_iniciar == 3:
                # os.system('cls')
                print('Operações finalizadas obrigado por usar o sistema')
                return 0

    while True:
        entrada_conta = Menu.contas(cliente=caixa.clientes[entrada_cpf], sistema=caixa)  
        break


    while True:
        Menu.operacoes(caixa.clientes[entrada_cpf].contas[entrada_conta - 1])

        try:
            operacao_atual = int(input())

        except ValueError:
            print('🚫[ERRO] Valor incorreto, por favor retorne um valor válido')

        else:
            # Opção que gera um depósito no caixa
            if operacao_atual == 1:
                # os.system('cls') # Limpa o terminal
                resultado = caixa.depositar(caixa.clientes[entrada_cpf].contas[entrada_conta - 1])
                caixa.extrato += resultado['valor_deposito']
                caixa.saldo = resultado['valor_saldo']

            # Opção que derruba um saque caso o limite diário tenha sido atingido
            elif operacao_atual == 2 and caixa.saques_efetuados >= caixa.SAQUES_DIARIOS:
                print('\n🚫[ERRO] Limite de saques diários atingido\n')

            # Opção que gera um saque
            elif operacao_atual == 2:
                caixa.saques_efetuados += 1
                # os.system('cls') # Limpa o terminal
                resultado = caixa.sacar(caixa.clientes[entrada_cpf].contas[entrada_conta - 1])
                caixa.extrato += resultado['valor_saque']
                caixa.saldo = resultado['valor_saldo']

            # Opção que gera o extrato
            elif operacao_atual == 3:
                # os.system('cls') # Limpa o terminal
                caixa.extrato += f'\nSALDO FINAL: {caixa.saldo}'
                caixa.extrato += f'\n{'='*60}'
                print(caixa.extrato)
                break
main()