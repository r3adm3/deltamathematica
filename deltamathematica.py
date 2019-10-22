#interpreter
uflist = list(input("Enter your Operation: "))
uflistx = []
skip = [-1]
#this for loop identifies certain seperators and non number characters
#and decides whether or not to flag them
for x in range(0, len(uflist)):
    try:
        int(uflist[x])
        uflistx.append(uflist[x])
    except ValueError:
        if (uflist[x] == ".") or (uflist[x] == "^") or (uflist[x] == "(") or (uflist[x] == ")") or (uflist[x] == "e") or (uflist[x] == "pi"):
            uflistx.append(uflist[x])
        else:
            skip.append(x)
            uflistx.append(uflist[x])
skip.append(len(uflistx))
uflistx.append("")
ufx = []
#this for loop conjoins related numbers and seperates them from operators
#e.g. '4, 1, *, 8' would be joint to 41 * 8
#this allows for the program to properly understand the users intention
for x in range(0, len(skip)-1):
    temp = ""
    for i in range(skip[x]+1, skip[x+1]):
        temp=temp + uflistx[i]
    ufx.append(temp)
    ufx.append(uflistx[skip[x+1]])
