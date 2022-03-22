

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # Assume that shopping list will arrive into function as a series of skus followed by the item letter #
    
    totalSum = 0

    n = 0
    
    for c in skus:
        
        if c.isdigit():
            n *= 10
            n += int(c)
            # if there are two isdigits in a row we are dealing with a 2 digit number and the calculation is made accordingly
            
        elif c.isalpha():
            if c == "A":
                # carry out the special offer as many times as possible then the regular price for those items left over
                totalSum += (n // 3) * 130
                totalSum += (n % 3) * 50
            elif c == "B":
                totalSum += (n // 2) * 45
                totalSum += (n % 2) * 30
            elif c == "C":
                totalSum += n * 20
            elif c == "D":
                totalSum += n * 15
            # reset the value to calculate the next sku for the next item
            n = 0
        
    return totalSum

