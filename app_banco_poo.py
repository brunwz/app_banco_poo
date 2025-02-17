from datetime import datetime
from abc import ABC, abstractproperty, abstractclassmethod

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.criar_conta(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico) -> None:
        self._saldo = 0
        self._numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo 
    
    @property
    def numero(self):
        return self._numero 
    
    @property
    def agencia(self):
        return self._agencia 
    
    @property
    def cliente(self):
        return self._cliente 
    
    @property
    def historico(self):
        return self._historico  

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n### Operação falhou! Você não tem saldo suficiente. ###")

        elif valor > 0:
            self._saldo -= valor
            # extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            # numero_saques += 1
            print("\n*** Saque realizado com sucesso! ***")

            return True
            
        # elif excedeu_limite:
        #     print("\n### Operação falhou! O valor do saque excede o limite. ###")
        
        # elif excedeu_saques:
        #     print("\n### Operação falhou! Número máximo de saques excedido. ###")

        else:
            print("\n###  Operação falhou! O valor informado é inválido. ### ")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            # extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n*** Depósito realizado com sucesso! ***")
        else:
            print("\n### Operação falhou! O valor informado é inválido. ###")
            return False

        return True

class ContaCorrente:
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
            )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n### Operação falhou! O valor de saque excedeu o limite. ###")

        elif excedeu_saques:
            print("\n### Operação falhou! Número de saques excedido. ###")

        else:
            return super().sacar(valor)
        
        def __str__(self):
            return f"""\
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
            """

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes 

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().stfrtime
                ("%d-%m-%Y %H:%M: %s"),
            }
        )

class Deposito:
    def __init__(self, valor):
        self.valor = 0
        
class Saque:
    def __init__(self, valor):
        self.valor = 0
        
class Transacao(ABC):
    
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractproperty
    def registrar(self, conta):
        pass