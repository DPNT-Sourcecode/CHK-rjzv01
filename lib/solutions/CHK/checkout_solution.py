import string

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # Assume that lower case are invalid #
    
    totalSum = 0

    valid = string.ascii_uppercase # a list of all valid inputs

    sums = {"A":0}

    for i in range(1,26):
        sums.update({valid[i]:0}) # Create a list of sums for each indiviudal item
    
    
    for c in skus:
        if c in valid:
            sums[c] += 1
        else:
            return -1


    # Each time at least 3 Fs appear in the basket the third is removed for the deal
    sums["F"] -= sums["F"] // 3
    
    # E special offer before B is calculated
    sums["B"] = max(0,(sums["B"] - (sums["E"] // 2)))
                
    # carry out the special offer as many times as possible then the regular price for those items left over
    
    #~A~#
    totalSum += (sums["A"] // 5) * 200
    sums["A"] = sums["A"] % 5 
    totalSum += (sums["A"] // 3) * 130
    totalSum += (sums["A"]% 3) * 50
    #~B~#
    totalSum += (sums["B"] // 2) * 45
    totalSum += (sums["B"] % 2) * 30
    #~C~#
    totalSum += sums["C"] * 20
    #~D~#
    totalSum += sums["D"] * 15
    #~E~#
    totalSum += sums["E"] * 40
    #~F~#
    totalSum += sums["F"] * 10
    #~G~#
    totalSum += sums["G"] * 20
    #~H~#
    totalSum += (sums["H"] // 10) * 80
    sums["A"] = sums["H"] % 10 
    totalSum += (sums["H"] // 5) * 45
    totalSum += (sums["H"]% 5) * 10
    #~I~#
    totalSum += sums["I"] * 35
    #~J~#
    totalSum += sums["J"] * 60
    #~K~#
    totalSum += (sums["K"] // 2) * 150
    totalSum += (sums["K"] % 2) * 80
    #~L~#
    totalSum += sums["L"] * 90
    #~M~#
    totalSum += sums["M"] * 15
        
    return totalSum





