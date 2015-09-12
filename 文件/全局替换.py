import fileinput

for line in fileinput.input('contect_list.txt',inplace=1):
    line = line.replace('##','00')
    print line,
