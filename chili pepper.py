n = int(input())
pepper_name = []

shu_table = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, 
             "Cayenne": 40000, "Thai": 75000, "Habanero": 125000}
    
for i in range(n):
    pepper_name.append(input())
 
total = 0
for name in pepper_name:
    total = total + shu_table[name]
   
print(total)
    
    
