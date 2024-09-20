# Classe base Empregado
class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

# Subclasse Gerente
class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    # Gerente tem um bônus fixo
    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo

# Subclasse Vendedor
class Vendedor(Empregado):
    def __init__(self, nome, salario_base, comissao, vendas):
        super().__init__(nome, salario_base)
        self.comissao = comissao
        self.vendas = vendas

    # Vendedor recebe com base na comissão por vendas
    def calcular_salario(self):
        return self.salario_base + (self.comissao * self.vendas)

# Exemplo de uso
gerente = Gerente("João", 5000, 1000)  # Salário base de 5000 e bônus fixo de 1000
vendedor = Vendedor("Maria", 3000, 0.05, 20000)  # Salário base de 3000, comissão de 5% sobre 20000 em vendas

print(f"Salário do Gerente {gerente.nome}: R${gerente.calcular_salario():.2f}")
print(f"Salário do Vendedor {vendedor.nome}: R${vendedor.calcular_salario():.2f}")