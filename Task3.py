string = eval(input())
stack = []
error = False
for i in string:
    if type(i) is tuple:
        for e in i:
            stack.append(e)
    else:
        if i <= len(stack):
            buffer = []
            for e in range(0, i):
                buffer.append(stack.pop(0))
            buffer = str(buffer)
            print('('+buffer.strip('[,]')+")")
        else:

            break
