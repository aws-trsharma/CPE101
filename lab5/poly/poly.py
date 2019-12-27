
def poly_add2(list1, list2):
 sum = []
 tot = len(list1)
 tot1 = (list1[0] + list2[0])
 sum.append(tot1)
 tot2 = (list1[1] + list2[1])
 sum.append(tot2)
 tot3 = (list1[2] + list2[2])
 sum.append(tot3)
 return sum
def poly_mult2(list1, list2):
 product = []
 tot1 = (list1[0] * list2[0])
 tot2 = list1[0] * list2[1] + list1[1]*list2[0]
 tot3 = list1[0] * list2[2] + list1[1]*list2[1] + list1[2]*list2[0]
 tot4 = list1[1]* list2[2] + list1[2]*list2[1]
 tot5 = list1[2] * list2[2]
 product = [tot1, tot2, tot3, tot4, tot5]
 return product
