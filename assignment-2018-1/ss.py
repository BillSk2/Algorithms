import sys
import pprint

pat=sys.argv[1]
b=float(sys.argv[2])
s=sys.argv[3]
t=sys.argv[4]
graph = {}

#Ανοιγμα αρχείου και δημιουργία γράφου
with open(pat) as input_file:
    #Για καθε γραμμη του αρχειου
    for line in input_file:
        #Για καθε μερος της γραμμης
        parts=line.split()
        [n1, n2, w] = [x for x in parts]
        #το κοστος συνδεσης των γραφων πρεπει να ειναι ακεραιο
        int(parts[-1])
        #Λιστα γειτνιασης αρχικοποιηση
        if n1 not in graph:
            graph[n1] = []
        #Λιστα γειτνιασης αρχικοποιηση
        if n2 not in graph:
            graph[n2] = []
            #Βαζει στη λιστα του ν1 τον ν2 με το κοστος συνδεσης του
        graph[n1].append((n2, w))

#Ελεγχος αρχικοποιησης γραφου
#pprint.pprint(graph)
#Λιστα με το μονοπατι
path = []
#Λιστα με ολα τα μονοπατια
paths = []
visited={}
for k,i in enumerate(graph.keys()):
    visited[i]=False
    #print(k,i)
#print('dd')

#Συναρτηση που βρισκει ολα τα απλά μονοπατια
def allsimplepaths(g ,st, ts):
    #print(g[st])
    #print("ξεκιναω\n")
    visited[st]=True
    #Push(path,s)
    path.append(st)
    if st==ts:
        #Push(paths,path)
        #print("ΕΙΝΑΙ ΙΣΑ\n")
        npath=list(path)
        paths.append(npath)
        #print(paths)
        #print("evala to path sto paths\n")
        #print(path)
    else:
        #print("Δεν ειναι ισα")
        for m,v in g[st]:
            #print(m,v)
            if not visited[m]:
                #print("αναδρομη\n")
                allsimplepaths(g,m,ts)
    #print("petao tin timi=")
    c=path.pop(-1)
    #print(c)
    visited[st]=False
    #print(paths)

allsimplepaths(graph,s,t)
#print('ss')
#pprint.pprint(paths)

#print("PART 3!!!!!!!!!")
Costs=[]
for x in paths :
    cost=0
    #print(x)
    #print(len(x))
    i=0
    while(i<len(x)-1):
        node1=x[i]
        node2=x[i+1]
        #print(node1)
        #print(node2)
        for m,v in graph[node1]:
            if (m==node2):
                cost=cost+int(v)
                #print(cost)
        i=i+1
    Costs.append(cost)
    cost=0
#pprint.pprint(Costs)
#print(Costs.index(min(Costs)))
min_path=paths[Costs.index(min(Costs))]
min_path_value=min(Costs)
print(min_path,min_path_value)
#print("TELOS")

Costs2=[]
j=len(min(paths))
#print("Μηκος μεγαλυτερου μονοπατιου")
#print(j)
d=0
#print("Αριθμος εξωτερικης επαναληψης")
#print(d)
path2=[]
path2.append(s)
#print("path2=")
#print(path2)
l=0
f=True
while (d<(j-1)and f):
    #print("Αριθμος εξωτερικης επαναληψης")
    #print(d)
    #print("arithmos monopatiou")
    k=0
    #print(k)
    for x in paths:
        node=d
        #print("Κομβος")
        #print(node)
        for m,v in graph[x[node]]:
            if m==x[node+1] and set(path2)<set(paths[k])and b!=0:
                #print('11111')
                #print(m,v)
                costt=int(v)
                #print("222222")
                #print(costt)
                #print("333333")
                #print(Costs[k])
                h=Costs[k]-costt
                h=h*b
                #print("44444")
                #print(h)
                Costs2.insert(k,h+costt)
            elif(b==0 and f):
                print(min_path,min_path_value)
                f=False
                break
            else:
                Costs2.insert(k,100000000)
        #print(Costs2)
        if k==j-2 and f:
            l=Costs2.index(min(Costs2))
            #print(l)
            stoix=paths[l][node+1]
            path2.append(stoix)
            #print(path2)
            d=d+1
        k=k+1
        #print(Costs2)
    del Costs2[:]
if f:
    print(path2,Costs[l])

