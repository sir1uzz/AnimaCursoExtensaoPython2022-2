# comando input (): quero permitir que o usuário digite algo
nome = input("Informe seu nome: ")
# Variável idade
idade = int (input ("Legal! Digite sua idade, " + nome + ": "))
genero = input ("Qual o seu gênero? \n M - Masculino \n F - Feminino \n")
dobroidade = idade * 2

# comando de saída
print ("Seu nome é " + nome + " e sua idade é " + str(idade) + " anos")
print ("O dobro da sua idade é " + str(dobroidade))

# Estrutura condicional (if)
# Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir (e ser preso)"

if (idade >= 18):
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir (e ser preso)")
else:
  print("Você é menor de idade :0")

if (idade >= 18 and genero == "M"):
  print("Você está apto ao alistamento")


