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
path = []
paths = []
visited={}
for k,i in enumerate(graph.keys()):
    visited[i]=False
def allsimplepaths(g ,st, ts):
    visited[st]=True
    path.append(st)
    if st==ts:
        npath=list(path)
        paths.append(npath)
    else:
        for m,v in g[st]:
            if not visited[m]:
                allsimplepaths(g,m,ts)
    c=path.pop(-1)
    visited[st]=False
allsimplepaths(graph,s,t)
Costs=[]
for x in paths :
    cost=0
    i=0
    while(i<len(x)-1):
        node1=x[i]
        node2=x[i+1]
        for m,v in graph[node1]:
            if (m==node2):
                cost=cost+int(v)
        i=i+1
    Costs.append(cost)
    cost=0
min_path=paths[Costs.index(min(Costs))]
min_path_value=min(Costs)
print(min_path,min_path_value)
Costs2=[]
j=len(min(paths))
o=len(paths)
d=0
path2=[]
if (len(paths)==1):
    print(min_path,min_path_value)
else:
    path2=[]
    path2.append(s)
    l=0
    f=True
    while (d<(j-1)and f):
        k=0
        for x in paths:
            node=d
            for m,v in graph[x[node]]:
                if m==x[node+1] and set(path2)<set(paths[k])and b!=0:
                    costt=int(v)
                    h=Costs[k]-costt
                    h=h*b
                    Costs2.insert(k,h+costt)
                elif(b==0 and f):
                    print(min_path,min_path_value)
                    f=False
                    break
                else:
                    Costs2.insert(k,100000000)
            if k==j-2 and f:
                l=Costs2.index(min(Costs2))
                stoix=paths[l][node+1]
                path2.append(stoix)
                d=d+1
            k=k+1
        del Costs2[:]
    if f:
        print(path2,Costs[l])
