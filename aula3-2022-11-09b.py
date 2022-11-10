# criação de funções

preco = 1999.90

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

# Aqui é o uso
preco = 299
imposto1 = calcular_imposto(preco)
print(imposto1)

# Explicação de variável local x global
print(preco)
preco_produto = 100
print (preco_produto)

valores = [1.99, 24.50, 78.27, 1515.5]

for valor in valores:
  print (f"O imposto de {valor} é {calcular_imposto(valor)}")

print("---------------")
# Declara um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utiliza 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

print("---------------")
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

print("---------------")
# E se o imposto for 10?
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")