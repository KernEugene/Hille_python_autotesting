
#Task1
def voting():
    num_votes = {}
    for _ in range(int(input())):
        candidate, votes = input().split()
        num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

    for candidate, votes in sorted(num_votes.items()):
        print(candidate, votes)


#Task2

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))


#Task3

numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
