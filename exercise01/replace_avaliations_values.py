ratings = [6, 8, 5, 9, 10]

def replace_ratings(rating):
  ratings_replaced = []

  for rate in rating:
    ratings_replaced.append(rate * 10)

  return ratings_replaced

print(replace_ratings(ratings))