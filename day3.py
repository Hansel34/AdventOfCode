def func1():
    inputs = []
    matrix = []

    for i in range(1000):
        matrix.append([0]*1000)
    
    while True:
        line = input()
        if line == "end":
            break
        inputs.append(line)

    for line in inputs:
        line = line.split('@')

        xVal = int(line[1].split(',')[0])

        line = line[1].split(',')[1]
        yVal = int(line.split(':')[0])

        line = line.split(':')[1]

        width = int(line.split('x')[0])
        height = int(line.split('x')[1])

        for x in range(xVal,xVal+width):
            for y in range(yVal, yVal+height):
                matrix[x][y]+=1
    total = 0
    for line in matrix:
        for val in line:
            if val > 1:
                total+=1
    print(total)

def func2():
    inputs = []
    matrix = []

    for i in range(1000):
        matrix.append([0]*1000)
    
    while True:
        line = input()
        if line == "end":
            break
        inputs.append(line)

    for line in inputs:
        line = line.split('@')

        xVal = int(line[1].split(',')[0])

        line = line[1].split(',')[1]
        yVal = int(line.split(':')[0])

        line = line.split(':')[1]

        width = int(line.split('x')[0])
        height = int(line.split('x')[1])

        for x in range(xVal,xVal+width):
            for y in range(yVal, yVal+height):
                matrix[x][y]+=1

    for line in inputs:
        line = line.split('@')
        id = line[0]
        xVal = int(line[1].split(',')[0])

        line = line[1].split(',')[1]
        yVal = int(line.split(':')[0])

        line = line.split(':')[1]

        width = int(line.split('x')[0])
        height = int(line.split('x')[1])

        isEmpty = True
        for x in range(xVal,xVal+width):
            for y in range(yVal, yVal+height):
                if matrix[x][y]!=1:
                    isEmpty = False
        if isEmpty == True:
            return id
