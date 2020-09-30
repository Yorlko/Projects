def discounted (price,discount, max_discount=50):
    price = abs(float(price))
    discount = abs (float(discount))
    max_discount = abs(float(max_discount))
    if max_discount>99 :
        raise ValueError ('Максимальная скидка не может быть больше 99%')
    if discount >= max_discount :
        price_with_discount = price
    else : 
        price_with_discount=price - (price * discount / 100)
    return (price_with_discount)

p = discounted (-69000, -90, 100)
print (p)