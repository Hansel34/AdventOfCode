from collections import defaultdict
def func1():
    inputs = []
    dic = defaultdict(int)
    inputs = [line.rstrip('\n') for line in open("d4.input")]
    inputs.sort()

    for i in range(len(inputs)):
        line = inputs[i]
        line = line.split()
        time = int(line[1][3:-1])
        type = line[2]
        id = line[3] 
        if type == "Guard":
            currentGuard = id[1:]
        elif type == "falls":
            sleepTime = time
        elif type == "wakes":
            dic[currentGuard]+=time-sleepTime

    totalGuards = list(dic.items())
    totalGuards.sort(key = lambda x:x[1], reverse = True)
    guardID = totalGuards[0][0]

    minutes = [0]*60
    for i in range(len(inputs)):
        line = inputs[i]
        line = line.split()
        time = int(line[1][3:-1])
        type = line[2]
        id = line[3] 
        if type == "Guard":
            currentGuard = id[1:]
        elif type == "falls":
            sleepTime = time
        elif type == "wakes" and currentGuard == guardID:
            for i in range(sleepTime,time):
                minutes[i]+=1
    print(int(guardID)*minutes.index(max(minutes)))

def func2():
    inputs = []
    dic = defaultdict(int)
    inputs = [line.rstrip('\n') for line in open("d4.input")]
    inputs.sort()

    for i in range(len(inputs)):
        line = inputs[i]
        line = line.split()
        time = int(line[1][3:-1])
        type = line[2]
        id = line[3] 
        if type == "Guard":
            currentGuard = id[1:]
        elif type == "falls":
            sleepTime = time
        elif type == "wakes":
            dic[currentGuard]+=time-sleepTime

    totalGuards = list(dic.items())
    totalGuards.sort(key = lambda x:x[1], reverse = True)
    guardID = totalGuards[0][0]
    allGuards = []

    for guard in dic:
        minutes = [0]*60
        for i in range(len(inputs)):
            line = inputs[i]
            line = line.split()
            time = int(line[1][3:-1])
            type = line[2]
            id = line[3] 
            if type == "Guard":
                currentGuard = id[1:]
            elif type == "falls":
                sleepTime = time
            elif type == "wakes" and currentGuard == guard:
                for i in range(sleepTime,time):
                    minutes[i]+=1
        allGuards.append([max(minutes),minutes.index(max(minutes)),int(guard)])
    allGuards.sort(reverse=True)
    print(allGuards[0][1]*allGuards[0][2])

func1()
func2()