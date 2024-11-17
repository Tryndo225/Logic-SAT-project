import random
l= []
num = input("How many vertexes?")
for i in range(120):
    l.append(i+1)

last=""
while len(l)!=0:
    if last == "":
        last = l.pop(random.randrange(len(l)))
    else:
        tmp = l.pop(random.randrange(len(l)))
        print("("+str(last)+","+str(tmp)+")", end = ";")
        last = tmp
    
