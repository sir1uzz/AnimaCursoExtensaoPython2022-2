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
imposto = calcular_imposto(preco)
print(imposto)

# Explicação de variável local x global
print(preco)
preco_produto = 100
print (preco_produto)

valores = [1.99, 24.50, 78.27, 1515.5]

for valor in valores:
  print (f"O imposto de {valor} é {calcular_imposto(valor)}")