
#https://pythontutor.ru/lessons/for_loop/problems/factorial/

def factorial(num):
    count = 1
    result = 1
    while count != num + 1:
        result *= count
        count += 1


#https://pythontutor.ru/lessons/for_loop/problems/sum_of_n_numbers/

def sum_of_N():
    N = int(input())
    count = 0
    result = 0
    while count != N:
        number = int(input())
        result += number
        count += 1


#https://pythontutor.ru/lessons/for_loop/problems/how_many_zeroes/

def sum_of_zeros():
    N = int(input())
    count = 0
    result = 0
    while count != N:
        number = int(input())
        if number == 0:
            result += 1
        count += 1

#https://pythontutor.ru/lessons/int_and_float/problems/raznost_vremen/

#Variant 1
def difference_in_time():
    first_time = 0
    first_time_hour = int(input())
    first_time_hour *= 3600
    first_time += first_time_hour

    first_time_min = int(input())
    first_time_min *= 60
    first_time += first_time_min

    first_time_sec = int(input())
    first_time += first_time_sec

    second_time = 0
    second_time_hour = int(input())
    second_time_hour *= 3600
    second_time += second_time_hour

    second_time_min = int(input())
    second_time_min *= 60
    second_time += second_time_min

    second_time_sec = int(input())
    second_time += second_time_sec

    print(second_time - first_time)


#Variant 2

def difference_in_time(first_time, second_time):
    print((second_time[0] * 3600 + second_time[1] * 60 + second_time[2]) - (first_time[0] * 3600 + first_time[1] * 60 + first_time[2]))

#Variant 3

def difference_in_time():
    times = []
    for _ in range(6):
        time = int(input())
        times.append(time)

    print((times[3] * 3600 + times[4] * 60 + times[5]) - (times[0] * 3600 + times[1] * 60 + times[2]))



