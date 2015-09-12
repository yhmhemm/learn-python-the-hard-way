produce = []
prices = []
f = open('shop_list.txt')
for line in f.readlines():
    produce.append(line.split()[0])
    prices.append(line.split()[1])

print produce,prices