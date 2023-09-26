from collections import OrderedDict

sales = OrderedDict()

N = int(input())

for _ in range(N):
    *item_name, price = input().split()
    item_name = ' '.join(item_name)
    if item_name in sales:
        sales[item_name] += int(price)
    else:
        sales[item_name] = int(price)

for item_name, net_price in sales.items():
    print(f'{item_name} {net_price}')
