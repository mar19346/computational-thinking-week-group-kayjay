def solution_station_4(num):
    if num == 0 or num == 1:
        return False
    elif num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                return True
                # break out of loop
                break
            else:
                return False