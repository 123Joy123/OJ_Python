s="()"
stack=[]
if len(s)==0:
    print(1)
else:
    for i in s:
        if (i=='(' or i=='[' or i=='{'):
            stack.append(i)
        else:
            if len(stack)==0:
                print(0)
            else:
                j=stack.pop()
                if (i==')' and j!='('):
                    print(0)
                elif (i==']' and j!='['):
                    print(0)
                elif (i=='}' and j!='{'):
                    print(0)
    if(len(stack)!=0):
        print(0)
    else:
        print(1)