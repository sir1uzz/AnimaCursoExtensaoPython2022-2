nome = input("Oi, aluno! \nInforme seu nome: ")
nota = float (input ("Digite sua nota de 0 a 10, " + nome + ": "))

if (nota == 10):
  print(nome + ", você é bichão mesmo hein doido")
elif (nota >= 6 and nota < 10):
  print(nome + ", você é mais ou menos")
else:
  print("Animal.")