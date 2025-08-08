# Pacotes importados para o projeto
import Menu
from Caixa import sistema

# Função principal
# Dividada em loops diferentes para cada ciclo de operações
#   1º loop permite login e cadastro de novos clientes
#   2º loop coleta todas as contas do cliente que efetuou o login e permite escolha de 1 para operações bancárias, também permite adicionar novas contas para cliente
#   3º loop permite realização de operações bancárias e ao final saída da execução do programa exibindo extrato
def main() -> int:
    # Variáveis globais
    caixa = sistema()
    entrada_cpf = ''
    entrada_conta = 0

    # 1º loop
    while True:
        Menu.iniciar()

        try:
            entrada_iniciar = int(input())
        
        except ValueError:
            ('🚫[ERRO] Valor incorreto, por favor retorne um valor válido')

        else:
            # Caso para efetuar login do usuário usando o cpf cadastrado
            if entrada_iniciar == 1:
                try:
                    Menu.login()
                    entrada_cpf: str = input()

                except ValueError:
                    ('🚫[ERRO] Cadastro não encontrado')

                else:
                    if caixa.loginCliente(entrada_cpf):
                        break 
            
            # Caso para efetuar cadastro de um novo cliente
            elif entrada_iniciar == 2:
                Menu.cadastro(caixa)
            
            # Caso de saída 
            elif entrada_iniciar == 3:
                print('Operações finalizadas obrigado por usar o sistema')
                return 0 # Retorno para função main()

    # 2º loop
    while True:
        # Atribuição de valor para variável global que controla em qual conta as operações estão sendo realizadas
        entrada_conta = Menu.contas(cliente=caixa.clientes[entrada_cpf], sistema=caixa)  
        break

    # 3º loop
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