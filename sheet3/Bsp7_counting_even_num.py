

from re import M
from pytz import country_names

count =0  # dont forgett to define count
My_list = []  #empty list
product = 1

for y in range (1,10): 
    if y % 2 == 0:      # %  ->division by 2 is 0     
        # count even number print("We have", count, "even numbers.")
        count += 1
        product *= count  
        print(" we have %d even numbers." %count )  
        print("the product is" % product)
        My_list.append(y)
        # here we append the output numbers to the my_list
print(My_list)        
print(f"We have {count} even numbers") # formatted string modern with {}
           
import math                         
result_2 = math.prod(My_list)       # use the product function =multiply all outputs

print("The product of these numbers is",result_2,".") # formatted string old with ""