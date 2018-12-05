from collections import Counter
def func1():
    twos = 0
    threes = 0
    inputs = [line.rstrip('\n') for line in open("d2.input")]

    for line in inputs:
        line = Counter(line)
        for _,val in line.items():
            if val == 2:
                twos+=1
                break
        for _,val in line.items():
            if val == 3:
                threes+=1
                break
    print(twos*threes)

def func2():
    inputs = [line.rstrip('\n') for line in open("d2.input")]
    for line1 in inputs:
        for line2 in inputs:
            differences = 0
            for i in range(len(line2)):
                if line1[i]!=line2[i]:
                    differences+=1
            if differences == 1:
                answer = []
                for i in range(len(line1)):
                    if line1[i] == line2[i]:
                        answer.append(line1[i])
                return "".join(answer)
func1()
print(func2())