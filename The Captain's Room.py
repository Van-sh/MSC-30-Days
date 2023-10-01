from collections import Counter

K = int(input())

room_numbers = list(map(int, input().split()))

rooms = Counter(room_numbers)

for room, count in rooms.items():
    if count == 1:
        print(room)
