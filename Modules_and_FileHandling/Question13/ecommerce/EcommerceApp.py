from product import management
from order import processing

# Adding a product
management.add_product("Laptop", 1200)

# Placing an order
cart = [...]  # assume this is a list of products
customer_info = {...}  # customer information
processing.place_order(cart, customer_info)
