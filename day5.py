def func1():
    inputLine = input()
    stack = []

    for c in inputLine:
        if stack:
            if stack[-1].lower() == c.lower():
                if (stack[-1].islower() and c.isupper()) or (stack[-1].isupper() and c.islower()):
                    stack.pop()
                    continue
        stack.append(c)

    print(len(stack))

def func2():

    inputLine = input()
    minSize = float("inf")

    for i in range(26):
        smallCase = chr(ord('a')+i)
        upperCase = chr(ord('A')+i)
        stack = []
        print(upperCase)
        for c in inputLine:
            if c == smallCase or c == upperCase:
                continue
            if stack:
                if stack[-1].lower() == c.lower():
                    if (stack[-1].islower() and c.isupper()) or (stack[-1].isupper() and c.islower()):
                        stack.pop()
                        continue
            stack.append(c)

        if len(stack) < minSize:
            minSize = len(stack)
    print(minSize)
    
func1()
func2()