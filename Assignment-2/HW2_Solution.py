from time import time
import copy

def game_spla(spla_days_1,spla_id_1,lahsa_days_1,lahsa_id_1,spla_left_list_1,lahsa_left_list_1,alpha,beta):


    if(len(spla_id_1)==0):
        if(len(lahsa_id_1)!=0):
            # for key, value in enumerate(lahsa_id_1):
            #     lahsa_left_list_1= map(int.__sub__, lahsa_left_list_1, lahsa_days_1[key])
            #     for m in lahsa_left_list_1:
            #         flag = 0
            #         if(m<0):
            #             flag = 1
            #             lahsa_left_list_1= map(int.__add__, lahsa_left_list_1, lahsa_days_1[key])
            #             break
            #     if(flag==1):
            #         ij=key
            #         removed_id = lahsa_id_1[ij]
            #         del(lahsa_id_1[ij])
            #         del(lahsa_days_1[ij])
            #         continue
            _ = game_lahsa(spla_days_1,spla_id_1,lahsa_days_1,lahsa_id_1,spla_left_list_1,lahsa_left_list_1,alpha,beta)
            return sum(spla_left_list_1)
        return sum(spla_left_list_1)

    infinity = float('inf')
    
    min_value_spla = infinity

    #print "Game Play SPLA"
    
    #print "lahsa_id_1: {}".format(lahsa_id_1)
    #print "spla_id_1: {}".format(spla_id_1)
    #print ""
    for key, value in enumerate(spla_id_1):

 
        spla_left_list_1= map(int.__sub__, spla_left_list_1, spla_days_1[key])
        for m in spla_left_list_1:
            flag = 0
            if(m<0):
                flag = 1
                spla_left_list_1= map(int.__add__, spla_left_list_1, spla_days_1[key])
                break
                
        if(flag==1):
            continue

        spla_days_2 = copy.deepcopy(spla_days_1)
        spla_id_2 = copy.deepcopy(spla_id_1)
        #print(spla_id_2)
        #print(spla_days_2)
        del(spla_days_2[key])
        del(spla_id_2[key])

        lahsa_days_2 = copy.deepcopy(lahsa_days_1)
        lahsa_id_2 = copy.deepcopy(lahsa_id_1)
        
        for i,j in enumerate(lahsa_id_2):
            if(value==j):
                ghe=lahsa_id_2[i]
                del(lahsa_id_2[i])
                del(lahsa_days_2[i])
                break

            

        temp_spla = game_lahsa(spla_days_2,spla_id_2,lahsa_days_2,lahsa_id_2,spla_left_list_1,lahsa_left_list_1,alpha,beta)
        min_value_spla=min(min_value_spla,temp_spla)

        if min_value_spla <= alpha:
            return min_value_spla
        beta = min(beta,min_value_spla)

        
        
        spla_left_list_1= map(int.__add__, spla_left_list_1, spla_days_1[key]) 

    return min_value_spla

def game_lahsa(spla_days_1,spla_id_1,lahsa_days_1,lahsa_id_1,spla_left_list_1,lahsa_left_list_1,alpha,beta):

    #print("initial_spla",spla_id_1)
    #print("initial_lahsa",lahsa_id_1)


    if(len(lahsa_id_1)==0):
        if(len(spla_id_1)!=0):
            # for key, value in enumerate(spla_id_1):
            #     spla_left_list_1= map(int.__sub__, spla_left_list_1, spla_days_1[key])
            #     for m in spla_left_list_1:
            #         flag = 0
            #         if(m<0):
            #             flag = 1
            #             spla_left_list_1= map(int.__add__, spla_left_list_1, spla_days_1[key])
            #             break
            #     if(flag==1):
            #         ij=key
            #         removed_id = spla_id_1[ij]
            #         del(spla_id_1[ij])
            #         del(spla_days_1[ij])
            #         continue
            temp_spla =  game_spla(spla_days_1,spla_id_1,lahsa_days_1,lahsa_id_1,spla_left_list_1,lahsa_left_list_1,alpha,beta)
            return temp_spla
        return sum(spla_left_list_1)

    infinity = float('inf')
    #mini_value_lahsa = infinity
    mini_value_spla = -infinity
    #print "Game Play LAHSA"
    
    #print "lahsa_id_1: {}".format(lahsa_id_1)
    #print "spla_id_1: {}".format(spla_id_1)
    #print ""
    for key, value in enumerate(lahsa_id_1):

 
        lahsa_left_list_1= map(int.__sub__, lahsa_left_list_1, lahsa_days_1[key])
        for m in lahsa_left_list_1:
            flag = 0
            if(m<0):
                flag = 1
                lahsa_left_list_1= map(int.__add__, lahsa_left_list_1, lahsa_days_1[key])
                break
                
        if(flag==1):
            continue

        lahsa_days_2 = copy.deepcopy(lahsa_days_1)
        lahsa_id_2 = copy.deepcopy(lahsa_id_1)
        #print(lahsa_days_2)
        del(lahsa_days_2[key])
        del(lahsa_id_2[key])
        spla_days_2 = copy.deepcopy(spla_days_1)
        spla_id_2 = copy.deepcopy(spla_id_1)
        for i,j in enumerate(spla_id_2):
            if(value==j):
                del(spla_id_2[i])
                del(spla_days_2[i])
                break


        #print("lahsa_left",lahsa_id_2)

            

        temp_spla =  game_spla(spla_days_2,spla_id_2,lahsa_days_2,lahsa_id_2,spla_left_list_1,lahsa_left_list_1,alpha,beta)
        
        mini_value_spla=max(mini_value_spla,temp_spla)

        if mini_value_spla >= beta:
            return mini_value_spla
        alpha = max(alpha,mini_value_spla)
        
        
        lahsa_left_list_1= map(int.__add__, lahsa_left_list_1, lahsa_days_1[key])

    return mini_value_spla

def main():
    t1 = time()
    ipFile=open("input0.txt", "r")
    opFile=open("output.txt","w+")
    #f1=f.readlines()
    count_beds = int(ipFile.readline())
    count_spaces = int(ipFile.readline())
    if(count_spaces == 0):
        return
    appli_lah = int(ipFile.readline())
    lahsa =[]
    for i in range(appli_lah):
        line = ipFile.readline()
        arrLine = line.rstrip()
        lahsa.append(arrLine)
    copy_lahsa=copy.deepcopy(lahsa)
    appli_spl = int(ipFile.readline())
    spla =[]
    for i in range(appli_spl):
        line = ipFile.readline()
        arrLine = line.rstrip()
        spla.append(arrLine)
    appli_tot = int(ipFile.readline())
    total =[]
    ids =[]
    gender =[]
    age =[]
    pets=[]
    med_c=[]
    car=[]
    driver_l=[]
    days_w=[]
    
    for i in range(appli_tot):
        line = ipFile.readline()
        arrLine = line.rstrip()
        total.append(arrLine)
        ids.append(arrLine[0:5])
        gender.append(arrLine[5])
        age.append(arrLine[6:9])
        pets.append(arrLine[9])
        med_c.append(arrLine[10])
        car.append(arrLine[11])
        driver_l.append(arrLine[12])
        days_w.append(arrLine[13:20])
        

    total_1=copy.deepcopy(total)
    ids_1=copy.deepcopy(ids)
    gender_1=copy.deepcopy(gender)
    age_1=copy.deepcopy(age)
    pets_1=copy.deepcopy(pets)
    med_c_1=copy.deepcopy(med_c)
    car_1=copy.deepcopy(car)
    driver_l_1=copy.deepcopy(driver_l)
    days_w_1=copy.deepcopy(days_w)

    
    spla_already_days=[]
    if(len(spla)>0):
        for i,x in enumerate(ids_1):
            if x in spla:
                spla_already_days.append(list(map(int, days_w_1[i])))

    lahsa_already_days=[]
    if(len(lahsa)>0):
        for i,x in enumerate(ids_1):
            if x in lahsa:
                lahsa_already_days.append(list(map(int, days_w_1[i])))

    copy_lahsa.extend(spla)
    #remain_ids = [x for i,x in enumerate(ids) if x not in copy_lahsa]
    pos_ids = [i for i,x in enumerate(ids) if x in copy_lahsa]
    
    for i in sorted(pos_ids, reverse=True):
        del total_1[i]
        del ids_1[i]
        del gender_1[i]
        del age_1[i]
        del pets_1[i]
        del med_c_1[i]
        del car_1[i]
        del driver_l_1[i]
        del days_w_1[i]

    #deleted those already present in lahsa and spla

    spla_total=[]
    spla_id=[]
    spla_days=[]
    for i,x in enumerate(ids_1):
        if((car_1[i]=='Y')and(driver_l_1[i]=='Y')and(med_c_1[i]=='N')):
            spla_total.append(total_1[i])
            spla_id.append(ids_1[i])
            spla_days.append(list(map(int, days_w_1[i])))

    #filtered out the ones which satisfy the constraint of driver license, car and medical condition.
    #converted string of integer (days required) to list        
    #print(spla_id)

    spaces_spla_list=[]
    empty_spla_list=[]

    for _ in range(7):
        spaces_spla_list.append(count_spaces)
        empty_spla_list.append(0)

    empty = empty_spla_list
    

    if(len(spla)>0):
        spla_left_list = map(int.__sub__, spaces_spla_list, [sum(i) for i in zip(*spla_already_days)])
        empty_spla_list = map(int.__add__, empty_spla_list, [sum(i) for i in zip(*spla_already_days)])
        
    else:
        spla_left_list = spaces_spla_list
        empty_spla_list = empty

    empty_spla_list = map(int.__add__, empty_spla_list, [sum(i) for i in zip(*spla_days)])
    spla_max = max(empty_spla_list)

    
    #spla_left_list is the no. of spaces left for each day in the week for spla

    lahsa_total=[]
    lahsa_spla_total=[]
    lahsa_id=[]
    lahsa_spla_id=[]
    lahsa_days=[]
    lahsa_spla_days=[]
    for i,x in enumerate(ids_1):
        if((gender_1[i]=='F')and(int(age_1[i])>17)and(pets_1[i]=='N')):
            lahsa_total.append(total_1[i])
            lahsa_id.append(ids_1[i])
            lahsa_days.append(list(map(int, days_w_1[i])))
            if((car_1[i]=='Y')and(driver_l_1[i]=='Y')and(med_c_1[i]=='N')):
                lahsa_spla_total.append(total_1[i])
                lahsa_spla_id.append(ids_1[i])
                lahsa_spla_days.append(list(map(int, days_w_1[i])))
            
    #filtered out the ones which satisfy the constraint of driver license, car and medical condition by getting lahsa_total
    #also from lahsa_total, got the ones which satisfy the constraints of spla
    
    beds_lahsa_list=[]

    for _ in range(7):
        beds_lahsa_list.append(count_beds)

    #print(beds_lahsa_list)
    if(len(lahsa)>0):
        lahsa_left_list = map(int.__sub__, beds_lahsa_list, [sum(i) for i in zip(*lahsa_already_days)])
    else:
        lahsa_left_list = beds_lahsa_list
    #print(lahsa_left_list)

    
    #print(spla_id)
    #print(lahsa_id)
    all_values = []
    all_left = []
    print(spla_id)
    print(empty_spla_list)

    if(spla_max > count_spaces):
        print("hi")

        for key, value in enumerate(spla_id):
            
            lahsa_in_id_1=copy.deepcopy(lahsa_id)
            lahsa_in_days_1=copy.deepcopy(lahsa_days)
            spla_in_id_1=copy.deepcopy(spla_id)
            spla_in_days_1=copy.deepcopy(spla_days)
            lahsa_in_left_list_1=copy.deepcopy(lahsa_left_list)
            spla_in_left_list_1=copy.deepcopy(spla_left_list)

            spla_in_left_list_1= map(int.__sub__, spla_in_left_list_1, spla_in_days_1[key])
            for m in spla_in_left_list_1:
                flag = 0
                if(m<0):
                    flag = 1
                    spla_in_left_list_1= map(int.__add__, spla_in_left_list_1, spla_in_days_1[key])
                    break
                    
            if(flag==1):
                continue

            del(spla_in_days_1[key])
            del(spla_in_id_1[key])


            
            for i,j in enumerate(lahsa_in_id_1):
                if(value==j):
                    del(lahsa_in_id_1[i])
                    del(lahsa_in_days_1[i])
                    break

            infinity = float('inf')
            alpha = -infinity
            beta = infinity

            result = game_lahsa(spla_in_days_1,spla_in_id_1,lahsa_in_days_1,lahsa_in_id_1,spla_in_left_list_1,lahsa_in_left_list_1,alpha,beta)
            spac = count_spaces*7

            left_out = spac - result

            print value,left_out

            all_values.append(value)
            all_left.append(result)

        Z = [x for _,x in sorted(zip(all_left,all_values))]

        cvb =Z[0]
        opFile.write(str(cvb))
        opFile.close()

    else:
        print("hey")
        minus_spla_list=[]
        if(len(lahsa_spla_id)>0):
            for i in range(len(lahsa_spla_id)):
                minus = map(int.__sub__, spla_left_list, lahsa_spla_days[i])
                minus_spla_list.append(sum(minus))
            #constraint imposed that checks that the result of days left shouldn't go in negative when spla_left_list and lahsa_spla_days are subtracted

            Z = [x for _,x in sorted(zip(minus_spla_list,lahsa_spla_id))]

            

            cvb =Z[0]
            opFile.write(str(cvb))
            opFile.close()

        else:
            for i in range(len(spla_id)):
                minus = map(int.__sub__, spla_left_list, spla_days[i])
                minus_spla_list.append(sum(minus))
            #constraint imposed that checks that the result of days left shouldn't go in negative when spla_left_list and lahsa_spla_days are subtracted

            Z = [x for _,x in sorted(zip(minus_spla_list,spla_id))]

            

            cvb =Z[0]
            opFile.write(str(cvb))
            opFile.close()
    
        

        

        
        
        
        
    



    



    

    

    '''

    t2=time()

    print(t2-t1)

    minus_spla_list=[]
    for i in range(len(lahsa_spla_id)):
        minus = map(int.__sub__, spla_left_list, lahsa_spla_days[i])
        for m in minus:
            flag = 0
            if(m<0):
                flag = 1
                break
        if(flag==1):
            ij=i
            removed_id = lahsa_spla_id[i]
            del(lahsa_spla_id[ij])
            continue
        minus_spla_list.append(sum(minus))
    #constraint imposed that checks that the result of days left shouldn't go in negative when spla_left_list and lahsa_spla_days are subtracted

    Z = [x for _,x in sorted(zip(minus_spla_list,lahsa_spla_id))]

    

    cvb =Z[0]
    opFile.write(str(cvb))
    opFile.close()


    def lahsa_play(spla_acceptance_dict,lahsa_acceptance_dict,spla_value,lahsa_value):


        if not lahsa_acceptance_dict: #Returning lahsa_value if lahsa_acceptance_dict is empty
            if(len(spla_acceptance_dict)!=0):
                for key, value in spla_acceptance_dict.iteritems():
                    spla_value = spla_value + value.count('1')
            return spla_value

        infinity = float('inf')
        min_value = infinity


        for key, value in lahsa_acceptance_dict.iteritems():

            lahsa_value = lahsa_value + value.count('1') #adding first key's value to lahsa's value

            lahsa_acceptance_dict_duplicate = lahsa_acceptance_dict.copy() #creating copy of lahsa_acceptance_dict
            lahsa_acceptance_dict_duplicate.pop(key, None) #removing first key and it's corresponding value from lahsa_acceptance_dict

            spla_acceptance_dict.pop(key,None) #removing first_key and it's corresponding value from spla_acceptance_dict

            min_value = min(min_value, spla_play(spla_acceptance_dict,lahsa_acceptance_dict_duplicate,spla_value,lahsa_value))

        return min_value
                            
'''
    



    
        
        

    
    
            
    


    


    
    
    
    #print(t2-t1)


    
        
    



if __name__=="__main__":
    main()
