
#Lista de Exercícios 1 - Linguagens de Programação
#UFRJ
#ECA 2023.2
#Natã dos Santos Carvalho

#Exercício 11
def exercicio11():
  print("----------------Exercicio 11-------------------")
  print("Digite o primeiro número inteiro: ")
  n_inteiro1 = input()
  print("Digite o segundo número inteiro: ")
  n_inteiro2 = input()
  print("Digite o número real: ")
  n_real = input()

  print("Resultados: ")
#a)
  resultado_a = (2 * int(n_inteiro1)) * (int(n_inteiro2) / 2)
  print("(2 *", n_inteiro1, ") * (", n_inteiro2, "/ 2) = ", resultado_a)

#b)
  resultado_b = (3 * int(n_inteiro1)) + float(n_real)
  print("(3 *", n_inteiro1, ") + (", n_real, ") = ", resultado_b)

#c)
  resultado_c = (float(n_real))**3
  print("(",n_real, "^ 3) = ", resultado_c, "\n")

def exercicio12():
  print("----------------Exercicio 12--------------------")
  print("Digite sua altura: ")
  altura = input()

  peso_ideal = (72.7 * float(altura)) - 58
  print("Seu peso ideal é: ", peso_ideal, "kg\n")

def exercicio13():
  print("----------------Exercicio 13--------------------")
  print("Digite sua altura: ")
  altura = input()

  print("Responda a ou b.\n")
  print("Qual seu genero ? \na)Mulher \nb)Homem")
  genero = input()

  if genero == "a":
    peso_ideal = (62.1 * float(altura)) - 44.7
    print("Seu peso ideal é: ", peso_ideal, "kg\n")

  if genero == "b":
      peso_ideal = (72.7 * float(altura)) - 58
      print("Seu peso ideal é: ", peso_ideal, "kg\n")

def exercicio14():
  peso_max = 50
  valor_multa_kg = 4.00

  print("Peso total de peixes obtidos: ")
  peso_peixes = float(input())

  excesso = peso_peixes - peso_max
  
  if (excesso > 0):
    multa = excesso * valor_multa_kg
    print("Quilos excedidos: ",excesso,"\n")
    print("Valor da multa a pagar em R$:",multa,"\n")

  else:
    print("Não houve excesso de peso em relação a esta pesca. O total ficou", excesso * (-1), "kg abaixo do limite.")

exercicio11()
exercicio12()
exercicio13()
exercicio14()