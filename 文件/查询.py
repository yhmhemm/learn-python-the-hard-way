staff_list = 'contect_list.txt'

f = file(staff_list)
c = f.readlines()

while True:
    user_input = raw_input('plz input something to serch:')
    for line in c:
        if user_input in line:
            print line
            break
    else:
            print "not a keyword!"