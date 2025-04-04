b = int(input()) 
p = 5*b-400  

if p < 100:
    sea_level = 1  
elif p > 100:
    sea_level = -1  
else:
    sea_level = 0  
    
print(p)
print(sea_level)
