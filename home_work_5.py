#################################


my_index = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[my_index]:
        my_index = i
print(a[my_index], my_index)



#################################


a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])


#################################


a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()

