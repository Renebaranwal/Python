def shopping_cart_total(prices):
    subtotal = sum(prices)
    tax = subtotal * 0.10
    total = subtotal + tax
    return round(total, 2)

items = [100, 200, 50]
print(shopping_cart_total(items))
