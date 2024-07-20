"""Question 13. Implement a python package structure for  a project named ecommerece and module for product management and order processing."""


from product.management import add_product, remove_product, product_list

## use case

## adding new product in inventory
print('==============================================')
print('\n')
print(product_list())
print('\n')
print('==============================================')
print('\n')
print(f'Adding a new product in inventory:', add_product('Earbuds', 850, 65))## adding new product in inventory
print('==============================================')
print('\n')
print(product_list())
print('\n')
print('==============================================')
print('\n')