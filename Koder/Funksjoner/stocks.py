# Setter utforbi slik den blir global for alle funksjonene
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 
                43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 
                49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

#finner prisen på dag x
def price_at(x):
    return stock_prices[x]

print(price_at(0))

#finnner max pris fra dag a til b  
def max_price(a, b):
    return max(stock_prices[a:b])



print(max_price(19,20))



def min_price(a, b):
    return min(stock_prices[a:b])

print(min_price(0,4))


