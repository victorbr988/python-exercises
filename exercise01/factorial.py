def factorial(number):
  factorial = 1
  
  # Iterar por cada número  #
  for value in range(number):

    # a variável factorial recebe a multiplicação do índice com o valor anterior dela mesma #
    factorial = (value + 1) * factorial

  return factorial

print(factorial(8))
