n = int(input())


goal = []
foul = []

for i in range (n):
  goal.append(int(input()))
  foul.append(int(input()))

count = 0  
for i in range(n):
    rating = 5*goal[i]-3*foul[i]
    if rating > 40:
      count = count + 1
      
if count == n:
  print(str(n) + "+")
  
else:
  print(str(count))
  

    
  
  

