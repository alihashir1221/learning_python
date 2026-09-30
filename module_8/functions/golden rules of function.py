#BAD STYLE FUNCTION
# def DiscPrint(p,r):
#     print("Calculating discount")
#     p = p - (p * r / 100)
#     print(p)
# DiscPrint(120, 20)

#Cleaned
def calculate_discount(price: float, rate: float) -> float:
    """ Calculate the final after applying a discount
        Args: 
            price (float): Original product price 
            rate (float): Discount rate as numbers (20 for 20%)
        Returns: 
            final_price (float): Final Price after applying discount.
    """
    final_price = price - (price * rate / 100)
    return final_price

# print(calculate_discount(80, 20))
help(calculate_discount) 