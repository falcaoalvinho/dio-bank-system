# Imports do arquivo
from Conta import conta
from Cliente import cliente


# Classe Caixa
# Armazena constantes e algumas variáveis do projeto
# Permite manipulação dos valores em depositos e saques
class sistema:
    def __init__(self):
        # Constantes do caixa
        self.SAQUES_DIARIOS: int = 3
        self.LIMITE_SAQUE: float = 500

        # Variáveis do caixa
        self.cedulas: dict = {
            "200": 10,
            "100": 10,
            "50": 10,
            "20": 10,
            "10": 10,
            "5": 10,
            "2": 10,
        }
        self.saldo: int = 0
        self.saques_efetuados: int = 0

        self.clientes: dict = {}  # Armazenameto dos Clientes ('cpf' : obj.cliente)

        # Armazenamento das Contas
        # self.contas: dict = {} #('cpf' : [conta1, conta2, ...])
        self.id_conta: int = 1

        # Começo da construção do extrato
        self.extrato: str = "EXTRATO".center(60, "=")
        self.extrato += f"\nSALDO INICIAL: {self.saldo}"

    def contarCedulas(self, cedulas: dict) -> int:
        # Essa função calcula o valor de uma quantia de cédulas recebidas em um dicionário de formato
        # {'<valor cédula>': <quantidade>, ...}
        # retorna o valor calculado

        valor = 0
        for i in cedulas:
            valor += int(i) * cedulas[i]
        return valor

    def loginCliente(self, cpf: str) -> None:
        # Essa função determina se o login foi bem sucedido verificando
        # se o cpf de fato foi cadastrado na lista de clientes do caixa
        # retornando verdadeiro ou falso

        if cpf in self.clientes:
            return True
        else:
            print("🚫[ERRO] Cliente não cadastrado!")
            return False

    def cadastrarCliente(self, cliente: cliente) -> None:
        # Este metódo cadastra os dados dos clientes caso já não exista um cpf
        # igual registrado na lista, senão retorna uma mensagem de erro

        if cliente.cpf not in self.clientes:
            self.clientes[cliente.cpf] = cliente
            print("Cliente cadastrado com suscesso!")

        else:
            print("🚫[ERRO] Cliente já cadastrado!")

    def cadastrarConta(self, cliente: cliente) -> None:
        # Este metódo vincula os dados do cliente que está realizando as operações com uma
        # nova conta e a registra nas listas do sistema

        self.clientes[cliente.cpf].contas.append(conta(self.id_conta, cliente.cpf))
        self.id_conta += 1
        print(f"Conta cadastrada no nome de {cliente.nome} com sucesso!")

    def depositar(self, conta: conta) -> {str, int}:
        # Função responsável pelos depositos no caixa
        # Capaz de computar quantas cédulas de cada estão sendo inseridas no programa
        # Calcula o valor usando a quantidade de cédulas e seus respectivos valores
        # Retorna o valor novo do saldo e o registro para ser adicionado no extrato

        # Armazena as células que vão entrar no caixa (usado para calcular o valor do depósito)
        cedulas_depositadas = {
            "200": 0,
            "100": 0,
            "50": 0,
            "20": 0,
            "10": 0,
            "5": 0,
            "2": 0,
        }

        print("DEPOSITO".center(60, "="))

        for i in self.cedulas:
            while True:
                try:
                    cedulas_depositadas[i] += int(input(f"Cédulas no valor de {i}: "))

                    if cedulas_depositadas[i] < 0:
                        raise ValueError("🚫[ERRO] O valor não pode ser negativo")

                    self.cedulas[i] += cedulas_depositadas[i]
                    break

                except ValueError:
                    print(
                        "\n   🚫[ERRO] Valor incorreto, por favor retorne um valor válido\n"
                    )
                    cedulas_depositadas[i] += int(input(f"Cédulas no valor de {i}: "))
                    self.cedulas[i] += cedulas_depositadas[i]

        valor_deposito = self.contarCedulas(cedulas_depositadas)
        conta.saldo += valor_deposito

        print(f"\n    Saldo total: {conta.saldo}")
        print(f"    Valor total do deposito: {valor_deposito}")
        print("=" * 60)

        return {
            "valor_deposito": f"\n    +{valor_deposito}",
            "valor_saldo": conta.saldo,
        }

    def sacar(self, conta: conta) -> {str, int}:
        # Função responsável pelos saques no caixa
        # Capaz de computar quantas cédulas de cada estão sendo retiradas no programa calculando os valores corretos de acordo com o saque
        # Retorna o valor novo do saldo e o registro para ser adicionado no extrato

        # Armazena cedulas usadas no saque para calcular seu valor
        cedulas_usadas = {"200": 0, "100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0}

        print("SAQUE".center(60, "="))
        print(f"   SAQUE MÁXIMO: {self.LIMITE_SAQUE}")
        print(f"   Saldo disponível: {conta.saldo}")

        try:
            saque = int(input("\n   Digite o valor do saque: "))
            valor_saque = saque

        except ValueError:
            print("\n🚫[ERRO]Valor incorreto, por favor retorne um valor válido\n")
            print(f"\n{'='*60}")
            self.sacar()

        else:
            if saque <= conta.saldo and saque <= self.LIMITE_SAQUE:
                for i in self.cedulas:
                    self.cedulas[i] -= saque // int(i)
                    cedulas_usadas[i] += saque // int(i)
                    saque -= int(i) * (saque // int(i))

            else:
                print(
                    "\n🚫[ERRO] Valor do saque excedeu o limite, por favor tente denovo"
                )
                print(f"\n{'='*60}")
                return self.sacar(conta=conta)

            conta.saldo -= self.contarCedulas(cedulas_usadas)

            print("    O valor foi sacado da sua conta")
            print(f"    Saldo atual: {conta.saldo}")
            print("=" * 60)

            return {"valor_saque": f"\n    -{valor_saque}", "valor_saldo": conta.saldo}
