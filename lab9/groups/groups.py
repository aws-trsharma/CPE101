def groups_of_3(list1):
    list2 = []
    list3 = []
    for i in range(0,len(list1),3):
        list2.append(list1[i:i+3])
    return list2

       
