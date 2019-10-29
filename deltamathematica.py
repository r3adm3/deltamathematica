def main():
    uflist = list(input("Enter your Operation: "))
    ufx = bracketCheck(interpart2(interpreter(uflist)))
    for element in ufx:
        if "(" in element:
            resolve(element)

##interpreter takes the initial input and does some basic parsing which
##is essential in order for the later, more complicated parsing

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
    #e.g. '4, 1, *, 8' would be joint to '41, *, 8'
    #this allows for the program to properly understand the users intention

    for x in range(0, len(skip)-1):
        glue = ""
        for i in range(skip[x]+1, skip[x+1]):
            glue = glue + intermediate[i]
        outputlist.append(glue)
        outputlist.append(intermediate[skip[x+1]])
    outputlist = outputlist[:len(outputlist)-1]
    return outputlist

##interpart2 deals with bracketed equations, at this point simply expressing
##them in an easier to deal with format, which can be utilised more later

def interpart2(checkee):
    backside=-1
    refurb=[]
    for x in range(0, len(checkee)):
        stack = ""
        if x > backside:
            if "(" in checkee[x]:
                if ")" not in checkee[x]:
                    for y in range(x+1, len(checkee)):
                        if ")" in checkee[y]:
                            for z in range(x,y+1):
                                stack = stack + checkee[z]
                            refurb.append(stack)
                            backside = y
                            break
            else:
                refurb.append(checkee[x])
    return refurb

##bracketCheck identifies the use of brackets and then transforms the input
##into a more readable format, that can be evaluated

def bracketCheck(sequence):
    factor = ""
    internal = ""
    modi = 0
    neosequence = []
    for x in range(0, len(sequence)):
        if "(" in sequence[x]:
            modi = x
            scan = list(sequence[x])
            for y in range(0,len(scan)):
                if scan[y] == "(":
                    operation = y
                    break
            for y in range(0, operation):
                factor = factor + scan[y]
            internal = sequence[x][operation:]
            break
    for x in range(0,modi):
        neosequence.append(sequence[x])
    neosequence.append(factor)
    neosequence.append("*")
    neosequence.append(internal)
    for x in range(modi+1, len(sequence)):
        neosequence.append(sequence[x])
    return neosequence

##resolve takes any bracketed function and simplifies it down so that it can
##be manipulated further

##resolve depends on more functions so will take more time to develop

def resolve(materia):
    raw = materia[1:len(materia)-1]
    if "(" in raw:
        raw = resolve(bracketCheck(interpart2(interpreter(raw))))
    ing = []
    ingtype = []
    ing = interpart2(interpreter(raw))
    for x in range(0, len(ing)):
        ingtype.append(classify(ing[x]))
    print(ingtype)

##classify simply takes each part of the equation and identifies
##its type i.e. integers, decimals, operators, etc.

def classify(unknown):
    identity = ""
    try:
        int(unknown)
        identity = "integer"
    except ValueError:
        try:
            float(unknown)
            identity = "decimal"
        except ValueError:
            if unknown == "pi" or unknown == "e":
                identity = "constant"
            elif unknown == "x" or unknown == "y" or unknown == "z":
                identity = "variable"
            elif unknown == "+" or unknown == "-" or unknown == "*" or unknown == "/" or unknown == "^":
                identity = "operator"
    return identity

## TODO:
## start simplifying the equations given and actually doing some maths
## get interpreter to remove any spaces

main()
