def sqrt(num):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # set upper and lower limits
    upperbound = num
    lowerbound = 1

#special casses
    if num ==1 or num ==0:
        return num

    if num < 0:
        return False

    while True:
        # set a value in between limits, iterate and update limits until found
        estimate = (lowerbound + upperbound) // 2

        if estimate ** 2 == num:
            return estimate
        
        elif estimate ** 2 > num:
            upperbound = estimate

        elif estimate ** 2 < num:
            if (estimate+1) **2 > num:
                return estimate
            else:
                lowerbound = estimate


# TESTS

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (False == sqrt(-9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (12 == sqrt(150)) else "Fail")
print ("Pass" if  (1234567 == sqrt(1524155677498)) else "Fail")
print ("Pass" if (9876567456) == sqrt(97546584712918311979) else "Fail")