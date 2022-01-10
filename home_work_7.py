

def capitalize(data):
    result = ''
    for i in data.split():
        result += i[0].upper() + i[1::] + ' '
    print(result)



def exponentiation(a,n):
    print(a ** n)



def distance(x1, y1, x2, y2):
    print(((x2-x1)**2 + (y2-y1)**2) ** 0.5)

