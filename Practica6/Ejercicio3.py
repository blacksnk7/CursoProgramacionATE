products = {'Mayonesa':140.50, 'Cerveza': 130, 'Agua mineral': 110.15, 'Servilleta': 65.20}
prod = input("Ingrese el producto: ").capitalize()
total = 0
while (prod != "Fin"):
    if prod in products.keys():
        ammount = int(input("Ingrese la cantidad de productos: "))
        total = total + (products[prod] * ammount)
        print(f"Costo actual: {products[prod] * ammount}")
    else:
        print("Ese producto no existe")
    prod = input("Ingrese el producto: ").capitalize()
print(f"Costo total: {total}")