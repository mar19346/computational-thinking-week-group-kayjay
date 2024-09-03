def solution_station_1(n):
    n = n + 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[-1]

print(solution_station_1(7))
