import json

#Task 1
class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def __str__(self):
    return f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

def product_serializer(product):
  if isinstance(product, Product):
    return {'name': product.name, 'price': product.price, 'quantity': product.quantity}
  raise TypeError('Cannot serialize object')

def product_deserializer(json_data):
  return Product(json_data['name'], json_data['price'], json_data['quantity'])

product1 = Product("Phone", 2300, 2)
product2 = Product("Laptop", 2500, 3)
product3 = Product("Mouse", 50, 5)

products_list = [product1, product2, product3]

with open('products.json', 'w') as json_file:
  json.dump(products_list, json_file, default=product_serializer, indent=4)

with open('products.json', 'r') as json_file:
  products = json.load(json_file, object_hook=product_deserializer)

for product in products:
  print(product)


#Task 2
from datetime import datetime

with open('lecture 19/movies.json', 'r') as file:
  data = json.load(file)

movies = data[0]['results']

updated_movies = []

for movie in movies:
  release_date = movie.get('release_date')
  movie_title = movie.get('title')
  genres = movie['genres']

  if release_date:
    release_year = datetime.strptime(release_date, '%Y-%m-%d').year

    if release_year > 2000 and 'Crime' in genres:
      movie['genres'] = ['New_Crime' if genre == 'Crime' else genre for genre in genres]
      updated_movies.append(movie)

    elif release_year < 2000 and 'Drama' in genres:
      movie['genres'] = ['Old_Drama' if genre == 'Drama' else genre for genre in genres]
      updated_movies.append(movie)

    elif release_year == 2000:
      movie['genres'].append('New_Century')
      updated_movies.append(movie)

with open('lecture 19/movies1.json', 'w') as json_file:
  json.dump({"results": updated_movies}, json_file, indent = 4)
