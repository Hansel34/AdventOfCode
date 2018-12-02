def func1():
    total = 0
    while True:
        line = input()
        if line == 'end':
            break
        if line[0] == '+':
            total += int(line[1:])
        else:
            total -= int(line[1:])
    print(total)

def func2():
    total = 0
    dic = {}
    dic[total] = True
    inputs = []
    while True:
        line = input()
        if line == "end":
            break
        inputs.append(line)

    while True:
        for line in inputs:
            if line[0] == '+':
                total += int(line[1:])
            else:
                total -= int(line[1:])
            if total in dic:
                return total
            dic[total] = True