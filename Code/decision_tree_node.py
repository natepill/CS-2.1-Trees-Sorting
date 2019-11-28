def isHappy(n: int, check_dict={}):

    num_str = str(n)

    num_tot = 0

    for num in num_str:
        num_tot += int(num)**2

    if num_tot == 1:
        return True
    elif num_tot in check_dict:
        return False
    else:
        check_dict[num_tot] = 1
        return isHappy(num_tot, check_dict)





if __name__ == "__main__":

    print(isHappy(13))
