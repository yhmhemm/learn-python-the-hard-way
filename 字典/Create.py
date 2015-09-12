produce = []
prices = []
shop_list = {}
f = open('shop_list.txt')
for line in f.readlines():
    produce.append(line.split()[0])
    prices.append(line.split()[1])

for i in range(0,len(produce)):
    shop_list[produce[i]] = prices[i]

print shop_list['Cake']
shop_list["abc"] = 123444
print shop_list
print shop_list.keys()
print shop_list.values()
