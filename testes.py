from Cliente import cliente
from ContaCorrente import contaCorrente

from datetime import date

novo_cliente = cliente()

novo_cliente.set_cpf("000.000.000-00")
novo_cliente.set_nome("Álvaro Falcão")
novo_cliente.set_data_nascimento(date(2006, 5, 13))
novo_cliente.set_endereco("Travessa Clã do Jabuti Nº5")

conta = contaCorrente()
conta.nova_conta(1)
conta.set_limite(1000)
conta.set_limite_saques(5)

novo_cliente.adcionar_conta(conta=conta)

print(novo_cliente.get_contas()[0].get_saldo())
novo_cliente.get_contas()[0].depositar(1000)
print(novo_cliente.get_contas()[0].get_saldo())
novo_cliente.get_contas()[0].sacar(500)
print(novo_cliente.get_contas()[0].get_saldo())

print("\n\nA APLICAÇÃO CONSEGUI DE MANEIRA BEM SUCEDIDA RELACIONAR TODAS AS SUAS CLASSES E GERAR RELAÇÕES ENTRE ELAS")