

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # Assume that lower case are invalid #
    
    totalSum = 0
    
    a_sum = 0
    b_sum = 0
    c_sum = 0
    d_sum = 0

    valid = ["A","B","C","D"]
    
    for c in skus:
        if c in valid:
            if c == "A":
                a_sum += 1
            elif c == "B":
                b_sum += 1
            elif c == "C":
                c_sum += 1
            elif c == "D":
                d_sum += 1
        else:
            return -1
                
    # carry out the special offer as many times as possible then the regular price for those items left over

    #~A~#
    totalSum += (a_sum // 3) * 130
    totalSum += (a_sum % 3) * 50
    #~B~#
    totalSum += (b_sum // 2) * 45
    totalSum += (b_sum % 2) * 30
    #~C~#
    totalSum += c_sum * 20
    #~D~#
    totalSum += d_sum * 15

        
    return totalSum



