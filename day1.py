def func1():
    total = 0
    inputs = [line.rstrip('\n') for line in open("d1.input")]
    for line in inputs:
        if line[0] == '+':
            total += int(line[1:])
        else:
            total -= int(line[1:])
    print(total)

def func2():
    total = 0
    dic = {}
    dic[total] = True
    inputs = [line.rstrip('\n') for line in open("d1.input")]
    while True:
        for line in inputs:
            if line[0] == '+':
                total += int(line[1:])
            else:
                total -= int(line[1:])
            if total in dic:
                return total
            dic[total] = True
            
func1()
print(func2())