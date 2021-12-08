

def greeting():
    print('Please, enter your name: ')
    name = str(input())
    print(f"Hello, {name}")


def show_next_previous_number():
    print('Please, enter your number: ')
    number = int(input())
    print(f'The next number for the number {number} is {number + 1}')
    print(f'The previous number for the number {number} is {number - 1}')


def is_leap_year():
    print('Please enter the year: ')
    year = int(input())
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(True)
    else:
        print(False)


def digit_after_dot():
    digit = float(input())
    print(int(digit * 10) % 10)


def is_fizz_or_buzz():
    number = int(input())
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')



def what_is_length_of_laces():
    print("Enter a: ")
    a = int(input())
    print("Enter b: ")
    b = int(input())
    print("Enter l: ")
    l = int(input())
    print("Enter N: ")
    N = int(input())

    if N < 2:
        length_of_laces = a + l * 2
    else:
        length_of_laces = (2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
    print(length_of_laces)


    #for standart laces
    # length_of_laces = 2 * l + a + (0.5 * (a * b) * (N - 1))


# if __name__ == '__main__':
#     greeting()
#     show_next_previous_number()
#     is_leap_year()
#     digit_after_dot()
#     is_fizz_or_buzz
#     what_is_length_of_laces()
