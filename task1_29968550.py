import re

global list_char
global list_repl
list_char = ['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)','(j)','(k)','(l)','(m)','(n)','(o)','(p)','(q)','(r)','(s)','(t)','(u)','(v)','(w)','(x)','(y)','(z)']
list_repl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def dataClean(source, target):

    fileObj = open(source,'r')
    lineStr = fileObj.read()

    fileObj = fileObj.close()

    lineStr = lineStr.replace("\n\t"," ")
    lineStr = lineStr.split('\n')

    child_SLI = []
    for element in lineStr:
        if '*CHI:' in element:
            child_SLI.append(element)


    #print(child_SLI)

    fileObj_write = open(target, "w")

    for item in child_SLI:
        item = item[5:]
        #print("OG: ",item)

        for elem in list_char:
            if elem in item:
                repl_elem = list_repl[list_char.index(elem)]
                item = item.replace(elem,repl_elem)
        match = item
        match = re.sub(r'\* m\:\+ed','*',match)
        match = re.sub(r'\*\sm(\:\W\w\w)*','*',match)
        match = re.sub(r'\[\W\s\w*?\W*?\w*?\]','',match)
        match = re.sub(r'\[\W(\s\w+)+?\]','',match)
        match = re.sub(r'\[\W*(\s\w+){2}?\W\w+\W\]','',match)
        match = re.sub(r'\[\?\]|\[\!\]|\[/\-\]','',match)
        match = re.sub(r'\[\^.+?\]','',match)
        match = re.sub(r'\+.*','.',match)
        match = re.sub(r'\[\w\s\d\]','',match)
        match = re.sub(r'\<|\>','',match)
        match = re.sub(r'\&\W*\w*|\+(\.)*','',match)
        match = re.sub(r'\(\.\.\)|\(\.\.\.\)','(.)',match)

        match = match.replace("\t","")
        match = match + "\n"

        pattern = re.compile(r"\(\w{2,}\)")
        matchPar = pattern.findall(match)

        for iters in matchPar:
            iters = iters.replace("(","")
            iters = iters.replace(")","")
            repl = iters
            match = re.sub(pattern,repl,match)


        #print("fil: ",match)

        fileObj_write.write(match)


    fileObj_write.close()

SLIlist = ["SLI-"]*10
TDlist = ["TD-"]*10
targetSLIlist = ["SLI-"]*10
targetTDlist = ["TD-"]*10
sourcelist = []
targetlist = []

i=1
for item in SLIlist:
    item = item+str(i)+".txt"
    i+=1
    sourcelist.append(item)


i=1
for item in TDlist:
    item = item+str(i)+".txt"
    i+=1
    sourcelist.append(item)

i=1
for item in targetSLIlist:
    item = item+str(i)+"-Cleaned.txt"
    i+=1
    targetlist.append(item)

i=1
for item in targetTDlist:
    item = item+str(i)+"-Cleaned.txt"
    i+=1
    targetlist.append(item)


filenumber = 0
for temp_iter in range(len(sourcelist)):
    dataClean(sourcelist[filenumber],targetlist[filenumber])
    filenumber+=1
