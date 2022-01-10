

# def was_it_before():
#     new_str = "1 2 3 4 5 6 7 2 3 4"
#     set_str = set()
#     for number in new_str.split():
#         if number in set_str:
#             print("YES")
#         else:
#             print("NO")
#
# was_it_before()



numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)