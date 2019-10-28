#interpreter
def interpreter(inputlist):
    intermediate = []
    skip = [-1]
    
#this for loop identifies certain seperators and non number characters
#and decides whether or not to flag them
    for x in range(0, len(inputlist)):
        try:
            int(inputlist[x])
            intermediate.append(inputlist[x])
        except ValueError:
            if (inputlist[x] == ".") or (inputlist[x] == "(") or (inputlist[x] == ")") or (inputlist[x] == "e") or (inputlist[x] == "pi"):
                intermediate.append(inputlist[x])
            else:
                skip.append(x)
                intermediate.append(inputlist[x])
    skip.append(len(intermediate))
    intermediate.append("")
    outputlist = []

#this for loop conjoins related numbers and seperates them from operators
#e.g. '4, 1, *, 8' would be joint to 41 * 8
#this allows for the program to properly understand the users intention
    for x in range(0, len(skip)-1):
        temp = ""
        for i in range(skip[x]+1, skip[x+1]):
            temp=temp + intermediate[i]
        outputlist.append(temp)
        outputlist.append(intermediate[skip[x+1]])
    outputlist = outputlist[:len(outputlist)-1]
    return outputlist

#interpart2 deals with bracketed equations, at this point simply expressing
#them in an easier to deal with format, which can be utilised more later
def interpart2(checkee):
    skippy=-1
    refurb=[]
    for x in range(0, len(checkee)):
        temp = ""
        if x > skippy:
            if "(" in checkee[x]:
                if ")" not in checkee[x]:
                    for y in range(x+1, len(checkee)):
                        if ")" in checkee[y]:
                            for z in range(x,y+1):
                                temp = temp + checkee[z]
                            refurb.append(temp)
                            skippy = y
                            break
            else:
                refurb.append(checkee[x])
    return refurb



##Now need to work on classifying each member of ufx
##Identify numbers and operators, but also recognise things like powers and brackets.
uflist = list(input("Enter your Operation: "))
ufx = interpart2(interpreter(uflist))
print(ufx)

#ufxtypes = []
#for element in ufx:
#    if "(" in element:
#        print()
#    else:
#        try:
#            int(element)
#            ufxtypes.append("Number")
#        except ValueError:
#            try:
#                double(element)
#                ufxtypes.append("Number")
#            except ValueError:
#                ufxtypes.append("Operator")
