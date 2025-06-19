# Pacotes importados para o projeto
import os
import Menu
import Caixa 

# Função principal
def main() -> None:
    caixa = Caixa.sistema()

    while True:
        Menu.printOpercoes()

        try:
            operacao_atual = int(input())

        except ValueError:
            print('🚫[ERRO] Valor incorreto, por favor retorne um valor válido')

        else:
            # Opção que gera um depósito no caixa
            if operacao_atual == 1:
                os.system('cls') # Limpa o terminal
                resultado = caixa.depositar()
                caixa.extrato += resultado['valor_deposito']
                caixa.saldo = resultado['valor_saldo']

            # Opção que derruba um saque caso o limite diário tenha sido atingido
            elif operacao_atual == 2 and caixa.saques_efetuados >= caixa.SAQUES_DIARIOS:
                print('\n🚫[ERRO] Limite de saques diários atingido\n')

            # Opção que gera um saque
            elif operacao_atual == 2:
                caixa.saques_efetuados += 1
                os.system('cls') # Limpa o terminal
                resultado = caixa.sacar()
                caixa.extrato += resultado['valor_saque']
                caixa.saldo = resultado['valor_saldo']

            # Opção que gera o extrato
            elif operacao_atual == 3:
                os.system('cls') # Limpa o terminal
                caixa.extrato += f'\nSALDO FINAL: {caixa.saldo}'
                caixa.extrato += f'\n{'='*60}'
                print(caixa.extrato)
                break
main()

# Ideias de melhoria:
#   Transformar o caixa em um objeto de arquivo próprio e mandar todos os metódos
#   de manipulação e contagem para dentro dele, junto com algumas variáveis e constantes do projeto.