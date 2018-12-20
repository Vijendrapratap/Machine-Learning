"""
Write a python program to check whether two lists are circularly identical.
"""

def circ_identical(list1, list2): 
      
    list3 = list1 * 2
    for x in range(0, len(list1)): 
        z = 0 

        for y in range(x, x + len(list1)): 
            if list2[z]== list3[y]: 
                z+= 1
            else: 
                break

        if z == len(list1): 
            return True 
      
    return False
          
  
 
list1 = [10, 10, 0, 0, 10] 
list2 = [10, 10, 10, 0, 0] 
list3 = [1, 10, 10, 0, 0] 
  
  
# check for list 1 and list 2  
if(circ_identical(list1, list2)):
    print("Yes")
else: 
    print("No")
  
# check for list 2 and list 3  
if(circ_identical(list2, list3)):
    print("Yes")
else: 
    print("No")