

def string_factoring(string):
    print(string[2])
    print(string[-2])
    print(string[0:5])
    print(string[:-2])
    print(string[::2])
    print(string[1::2])
    print(string[::-1])
    print(string[::-2])
    print(len(string))



def string_slice(string):
    string = string[:string.find('h')] + string[string.rfind('h') + 1:]
    print(string)



def calculate_avarage_summ():
    summ = 0
    print("please enter how many times u want to print a number")
    how_many_times = int(input())

    for _ in range(how_many_times):
        number = int(input())
        summ += number

    avarage_summ = summ/int(how_many_times)



def find_counts_of_prev_elements():
    prev = int(input())
    answer = 0
    while prev != 0:
        next = int(input())
        if next != 0 and prev < next:
            answer += 1
        prev = next

