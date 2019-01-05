
# coding: utf-8

# In[1]:


from time import time
import numpy as np
import copy


# In[20]:


def main():
    t1 = time()
    #ipFile=open("corrected_testcases/testcases/input20.txt", "r")
    #ipFile=open("corrected_testcases/input30.txt", "r")
    ipFile=open("grading_case/input30.txt", "r")
    #ipFile=open("input.txt", "r")
    opFile=open("output.txt","w+")
    #f1=f.readlines()
    grid_size = int(ipFile.readline())
    full_grid = grid_size*grid_size
    num_cars = int(ipFile.readline())
    num_obstacles = int(ipFile.readline())
    loc_obstacles =[]
    for i in range(num_obstacles):
        line = ipFile.readline()
        arrLine = line.rstrip()
        loc_obstacles.append(list(map(int, arrLine.split(','))))
    loc_start =[]
    for i in range(num_cars):
        line = ipFile.readline()
        arrLine = line.rstrip()
        loc_start.append(list(map(int, arrLine.split(','))))
    loc_terminal = []
    for i in range(num_cars):
        line = ipFile.readline()
        arrLine = line.rstrip()
        loc_terminal.append(list(map(int, arrLine.split(','))))

    grid = np.ones((grid_size,grid_size)) * -1
    

    for a in loc_obstacles:
        grid[a[1],a[0]] = grid[a[1],a[0]] - 100
        
    #print(grid)
        
    neighbors = []
    direction_all_moves = []
    nof = []
    position_num = []
    counter = -1
        
    for index,val in enumerate(grid):
        for i,v in enumerate(val):
            
            results = []
            direction_move = []
            counter = counter + 1
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    newx = index+dx
                    newy = i+dy
                    if (((dx == 0) and (dy == 0)) or ((dx == -1) and (dy == -1)) or ((dx == 1) and (dy == 1)) or ((dx == -1) and (dy == 1)) or ((dx == 1) and (dy == -1))) :
                        continue
                        
                    else:
                        if(index<newx):
                            direction_move.append("south")
                        elif(index>newx):
                            direction_move.append("north")
                        elif(i<newy):
                            direction_move.append("east")
                        elif(i>newy):
                            direction_move.append("west")
                        if ((newx>=0) and (newx<grid_size) and (newy >=0) and (newy<grid_size)):
                        #print((newx,newy))
                            results.append( (newy, newx) )
                        else :
                            results.append((i,index))
#             if(len(results)==2):
#                 results.append((i,index))
#                 results.append((i,index))
#             elif(len(results)==3):
#                 results.append((i,index))
            
            nof.append((i,index))
            position_num.append(counter)
            neighbors.append(results)
            direction_all_moves.append(direction_move)
            
    
    
#     neighbors = np.flip(neighbors,0)
#     neighbors = np.flip(neighbors,1)
#     print(nof)
    #print(neighbors)
    #print(direction_all_moves)
        

    
    

    #print(rewards)
    
    for i,a in zip(range(num_cars),loc_terminal):
        #print("hi")
        rewards = copy.deepcopy(grid)
        rewards[a[1],a[0]] = rewards[a[1],a[0]] + 100
        #print(rewards)
        #print((loc_terminal[i][0],loc_terminal[i][1]))
        
        
        
#     print(rewards)
#     print(rewards[neighbors[0][1]])
    
        utilities = np.zeros((grid_size,grid_size))
        #utilities[(loc_terminal[i][1],loc_terminal[i][0])] = 99
        #utilities = rewards
        arglist = []
        t_d = []
        counte = 0
        while(1):
            counte = counte + 1
            #print(counte)
            initial_util = copy.deepcopy(utilities)
#             init_list = copy.deepcopy(arglist)
#             turn_direction = copy.deepcopy(t_d)
            for j in range(full_grid):
#                 print(j)
#                 print(i)
#                 print(nof[j])
#                 print((loc_terminal[i][0],loc_terminal[i][1]))
                if(nof[j] == (loc_terminal[i][0],loc_terminal[i][1])):
                    utilities[(loc_terminal[i][1],loc_terminal[i][0])] = 99
                    arglist.append((loc_terminal[i][0],loc_terminal[i][1]))
                    t_d.append((loc_terminal[i][0],loc_terminal[i][1]))
                    continue
                else:
                    Adir = (0.7*(utilities[neighbors[j][0][1],neighbors[j][0][0]])) + (0.1*(utilities[neighbors[j][1][1],neighbors[j][1][0]])) + (0.1*(utilities[neighbors[j][2][1],neighbors[j][2][0]])) + (0.1*(utilities[neighbors[j][3][1],neighbors[j][3][0]]))
                    Bdir = (0.7*(utilities[neighbors[j][1][1],neighbors[j][1][0]])) + (0.1*(utilities[neighbors[j][0][1],neighbors[j][0][0]])) + (0.1*(utilities[neighbors[j][2][1],neighbors[j][2][0]])) + (0.1*(utilities[neighbors[j][3][1],neighbors[j][3][0]]))
                    Cdir = (0.7*(utilities[neighbors[j][2][1],neighbors[j][2][0]])) + (0.1*(utilities[neighbors[j][1][1],neighbors[j][1][0]])) + (0.1*(utilities[neighbors[j][0][1],neighbors[j][0][0]])) + (0.1*(utilities[neighbors[j][3][1],neighbors[j][3][0]]))
                    Ddir = (0.7*(utilities[neighbors[j][3][1],neighbors[j][3][0]])) + (0.1*(utilities[neighbors[j][1][1],neighbors[j][1][0]])) + (0.1*(utilities[neighbors[j][2][1],neighbors[j][2][0]])) + (0.1*(utilities[neighbors[j][0][1],neighbors[j][0][0]]))
                    
                    Maxdir = Adir
                    Maxarg = 0
                    if((Maxdir < Ddir) and (Ddir >= Cdir) and (Ddir >= Bdir)):
                        Maxdir = Ddir
                        Maxarg = 3

                    elif((Maxdir < Cdir) and (Cdir >= Ddir) and (Cdir >= Bdir)):
                        Maxdir = Cdir
                        Maxarg = 2

                    elif((Maxdir < Bdir) and (Bdir >= Ddir) and (Bdir >= Cdir)):
                        Maxdir = Bdir
                        Maxarg = 1
#                     Maxdir = max(Adir, Bdir, Cdir, Ddir)
#                     #print(Maxdir)
#                     Maxarg = np.argmax((Adir, Bdir, Cdir, Ddir))
#                     #print(Adir, Bdir, Cdir, Ddir)
                    if(Maxarg==0):
                        t_d.append(direction_all_moves[j][0])
                        arglist.append(neighbors[j][0])
            
                    elif(Maxarg==1):
                        t_d.append(direction_all_moves[j][1])
                        arglist.append(neighbors[j][1])
                        
                    elif(Maxarg==2):
                        t_d.append(direction_all_moves[j][2])
                        arglist.append(neighbors[j][2])
                        
                    else:
                        t_d.append(direction_all_moves[j][3])
                        arglist.append(neighbors[j][3])
                        
                    utilities[nof[j][1],nof[j][0]] = rewards[nof[j][1],nof[j][0]] + (Maxdir * 0.9)
                    #print(utilities)
                #print(arglist)
            #print(utilities)
            g = abs(initial_util - utilities).max()
            epsi = (0.1*0.1)/0.9
            if(g < epsi):
#                 init_list = arglist
#                 turn_direction = t_d
                break
            else:
                init_list = copy.deepcopy(arglist)
                turn_direction = copy.deepcopy(t_d)
                arglist = []
                t_d = []
                continue
                
        #print(initial_util)
        #print(init_list)
        #print(turn_direction)
        #init_list = [(0, 0), (0, 0), (1, 0), (0, 0), (1, 0), (2, 0), (1, 2), (1, 1), (2, 1)]
        #init_list = [(1, 0), (2, 0), (3, 0), (3, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (0, 0), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (5, 1), (7, 0), (8, 0), (8, 1), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3), (8, 2), (8, 3), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (6, 4), (8, 3), (9, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5), (6, 5), (9, 5), (9, 4), (0, 5), (1, 5), (1, 6), (4, 6), (4, 5), (5, 5), (5, 6), (6, 6), (8, 5), (9, 5), (0, 6), (1, 6), (1, 7), (2, 7), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 8), (7, 9), (8, 7), (9, 7), (0, 8), (1, 8), (1, 9), (3, 8), (4, 8), (5, 8), (5, 9), (6, 9), (7, 9), (8, 9)]
        #print(nof)
        
        all_rewards = []
        for j in range(10):
            #print("hey")
            pos = (loc_start[i][0],loc_start[i][1])
            np.random.seed(j)
            swerve = np.random.random_sample(1000000)
            #print(swerve)
            k=0
            add = 0
            term = (loc_terminal[i][0],loc_terminal[i][1])
            while pos != term:
                for index, value in enumerate(nof):
                    if pos == nof[index]:
                        x = position_num[index]
                        break
                move = init_list[x]
                direction = turn_direction[x]
                #print(init_list)
                #print(x)
                #print("move",move)
                #print("pos",pos)
#                 m_0 = move[0]
#                 p_0 = pos[0]
#                 m_1 = move[1]
#                 p_1 = pos[1]
#                 mp0 = m_0 - p_0
#                 mp1 = m_1 - p_1
#                 if(mp0>0): 
#                     direction = "east"
#                     #print(direction)
#                 elif(mp0<0):
#                     direction = "west"
#                     #print(direction)
#                 elif(mp1>0):
#                     direction = "south"
#                     #print(direction)
#                 elif(mp1<0):
#                     direction = "north"
#                     #print(direction)
#                 else:
#                     direction = 'n'
                    #print(direction)
                #print(swerve[k])
                if swerve[k] > 0.7:
                    if swerve[k] > 0.8:
                        if swerve[k] > 0.9:
                            
                            if(direction=="south"):
                                dx = pos[0]
                                dy = pos[1]-1
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)
                                    
                            elif(direction=="north"):
                                dx = pos[0]
                                dy = pos[1]+1
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)
                                    
                            elif(direction=="east"):
                                dx = pos[0]-1
                                dy = pos[1]
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)
                            
                            elif(direction=="west"):
                                dx = pos[0]+1
                                dy = pos[1]
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)
                        
                        
                        
                        else:
                            if(direction=="south"):
                                dx = pos[0]-1
                                dy = pos[1]
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)

                            elif(direction=="north"):
                                dx = pos[0]+1
                                dy = pos[1]
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)

                            elif(direction=="east"):
                                dx = pos[0]
                                dy = pos[1]+1
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)

                            elif(direction=="west"):
                                dx = pos[0]
                                dy = pos[1]-1
                                if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                    move = pos
                                else:
                                    move = (dx,dy)

                                
                    else:
                        if(direction=="south"):
                            dx = pos[0]+1
                            dy = pos[1]
                            if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                move = pos
                            else:
                                move = (dx,dy)

                        elif(direction=="north"):
                            dx = pos[0]-1
                            dy = pos[1]
                            if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                move = pos
                            else:
                                move = (dx,dy)

                        elif(direction=="east"):
                            dx = pos[0]
                            dy = pos[1]-1
                            if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                move = pos
                            else:
                                move = (dx,dy)

                        elif(direction=="west"):
                            dx = pos[0]
                            dy = pos[1]+1
                            if((dx<0) or (dy<0) or (dx>=grid_size) or (dy>=grid_size)):
                                move = pos
                            else:
                                move = (dx,dy)
                        
                        
                    
                                
                            
                    
                                
                                    
                pos = move
                add = add + rewards[pos[1],pos[0]]
                #print(move)
                #print(add)
                k=k+1
            
            #print(add)
            all_rewards.append(add)
        
        mean = sum(all_rewards)/len(all_rewards)
        #print(all_rewards)
        #print(all_rewards)
        print(np.floor(mean))
        
        cvb = np.floor(mean)
        opFile.write(str(int(cvb)))
        opFile.write("\n")
    opFile.close()
                
        
        
        
        
        
        


# In[21]:


if __name__=="__main__":
    main()

