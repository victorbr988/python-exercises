ratings = [6, 8, 5, 9, 10]

def replace_ratings(rating):
  for rate in rating:
    if rate % 3 == 0:
      print(f'{rate} Múltiplo de 3')

print(replace_ratings(ratings))