n = int(input())
   
   
name = []
bid = []
   
for i in range(n):
    name.append(input())
    bid.append(int(input()))
   
prev_max = bid[0]
prev_max_idx = 0
for i in range(len(bid)):
    if bid[i] > prev_max:
        prev_max = bid[i]
        prev_max_idx = i
          
print(name[prev_max_idx])
 
       
   
   
   
     