import pandas as pd

products = [
    {"product_id": "PI_Laptop", "name": "Laptop", "price": 45000.0, "units": 10},
    {"product_id": "PI_Smartphone", "name": "Smartphone", "price": 18000.0, "units": 15},
    {"product_id": "PI_Headphones", "name": "Headphones", "price": 1500.0, "units": 30},
    {"product_id": "PI_Mouse", "name": "Mouse", "price": 750.0, "units": 50},
    {"product_id": "PI_Keyboard", "name": "Keyboard", "price": 1250.0, "units": 20},
]



def add_product(name:str, price:float, units:int)->str:
    # Function to add new product in inventory
    try:
        
        new_product= {"product_id": 'PI_'+name, "name":name, "price":price, "units": units}
    
        if new_product in products:
            return 'This product in already in inventory. Check the details.'
    
        products.append(new_product)
        return f'Product added into inventroy. \nProduct id: - {new_product["product_id"]}'
    except Exception as e:
        return e

def remove_product(product_id):
    # Function to remove a product form inventory
    try:
        for i, product in enumerate(products):
            if product['product_id'] == product_id:
                return products.pop(i)
    except Exception as e:
        return e
    


def product_list():
    try:
        inventory=pd.DataFrame(data=products)
        return inventory
    except Exception as e:
        return e

