from collections import Counter
def func1():
    twos = 0
    threes = 0
    inputs = []
    while True:
        line = input()
        if line == "end":
            break
        inputs.append(line)
    
    for line in inputs:
        line = Counter(line)
        for key,val in line.items():
            if val == 2:
                twos+=1
                break
        for key,val in line.items():
            if val == 3:
                threes+=1
                break
    print(twos*threes)

def func2():
    inputs = []
    while True:
        line = input()
        if line == "end":
            break
        inputs.append(line)
    
    for line in inputs:
        for line2 in inputs:
            differences = 0
            for i in range(len(line)):
                if line[i]!=line2[i]:
                    differences+=1
            if differences == 1:
                return line+"  "+line2

print(func2())