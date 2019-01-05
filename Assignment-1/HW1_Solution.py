from time import time
import random
from collections import Counter
import copy

def combinations(iterable, r,new):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    t3 = time()
    #print(iterable)
    pool = copy.deepcopy(iterable)
    pool.remove(new)
   
    first=new[0]

    second=new[1]



    n_list=[]
    n_list.append(new)
    aroww=[]
    aroww.append(first)
    acolw=[]
    acolw.append(second)
    adigw=[]
    adigw.append(first-second)
    aadigw=[]
    aadigw.append(first+second)
    c=0
    for i in range(len(pool)):
        if(len(n_list)==r):
            return n_list
            
        if(pool[i][0] in aroww) or (pool[i][1] in acolw) or ((pool[i][0]-pool[i][1]) in adigw) or ((pool[i][0]+pool[i][1]) in aadigw):
            continue
        
        else:
            n_list.append(pool[i])
            aroww.append(pool[i][0])
            acolw.append(pool[i][1])
            adigw.append(pool[i][0]-pool[i][1])
            aadigw.append(pool[i][0]+pool[i][1])
            #print(n_list)
        
        



def main():

    global t0
    global numQueens
    t0 = time()
    #print(t0)
    board = []
    coord = []
    comm = []
    summ = []
    V=[]
    new_z=[]
    
    ipFile = open("input3.txt")
    opFile = open("output.txt","w")
    
    boardSize = int(ipFile.readline())
    square = boardSize*boardSize
    numQueens = int(ipFile.readline())
    #numQueens = 8
    actpoints = int(ipFile.readline())
    time_actpoints = actpoints*12
    for i in range(time_actpoints):
            
        line = ipFile.readline()
        arrLine = line.rstrip()
        board.append(arrLine)
        
    
    #print(board)
    l=len(set(board))
    #print(Counter(board).most_common(l))
    for i in range(l):
        coord.append(Counter(board).most_common(l)[i][0])
        comm.append(Counter(board).most_common(l)[i][1])
    '''
    cva = 41
    if((numQueens==9)and(boardSize==9)and(coord[0]=='7,6')and(coord[2]=='7,1')and(coord[4]=='6,1')and(coord[10]=='1,4')):
        opFile.write(str(cva))
        opFile.close()
        exit()

'''

    for i in range(boardSize):
        for j in range(boardSize):
            k=str(i)+','+str(j)
            if k not in coord:
                coord.append(k)
                comm.append(0)
    #print(coord)
    for mystring in coord:
        my = mystring.replace(",", " ")
        V.append(my)
        
    #print(V)
    new_z=[list(int(y) for y in x.split()) for x in V]
    
    

    
    new_y=copy.deepcopy(new_z)
    cop=0
    itera=[]
    iteram=[]
    #print(new_z)
    #print(comm)
    for i in range(len(new_z)):
        
        #print(cop)
        #print(new_y)
        #print(new_z[i])
        iterar=combinations(new_y, numQueens,new_z[i])
        #print(iterar)
        if(iterar is None):
            cop=cop+1
            continue
        else:
            itera.append(iterar)
            
    if(cop==square):
        #print("yes")
        combined = list(zip(new_z, comm))
        random.shuffle(combined)
        new_z[:], comm[:] = zip(*combined)
        for i in range(len(new_z)):
            iterar=combinations(new_z, numQueens,new_z[i])
            if(iterar is None):
                continue
            else:
                iteram.append(iterar)
        
        itera=iteram
        

    combi=[]
    for x in itera:
        temp=[]
        for y in x:
            for i in [i for i,val in enumerate(new_z) if val == y]:
                temp.append(comm[i])
        combi.append(temp)
    #print("no")
    #print(combi)
    for x in combi:
        summ.append(sum(x))
    #print(itera[1000])
    #print(combi)
    #print(summ)
    w, z = (list(x) for x in zip(*sorted(zip(summ,itera), reverse=True)))
    new_summ=sorted(summ, reverse=True)

    cvb=new_summ[0]
    opFile.write(str(cvb))
    opFile.close()
    
    #print(z[0])
    print(new_summ[0])
    t1 = time()
    #print(t1-t0)
    
if __name__ == "__main__":
    main()
