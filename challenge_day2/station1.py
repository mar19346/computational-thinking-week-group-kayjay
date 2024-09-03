def solution_station_1(a):

    if a == 1 or a == 2:
        return 1

    else:
        return solution_station_1(a-1) + solution_station_1(a-2)
    

