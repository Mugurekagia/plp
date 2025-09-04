def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))
    
final_price = calculate_discount(price, discount_percent)
    
if discount_percent >=20:
    print(f"Final price after {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
        