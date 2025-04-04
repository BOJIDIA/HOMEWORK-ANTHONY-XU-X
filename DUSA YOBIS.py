dusa_size = int(input())

check = False
while check == False:
  nxt_yobi = int(input())
  
  if dusa_size > nxt_yobi:
    dusa_size = dusa_size + nxt_yobi
    
  if dusa_size <= nxt_yobi:
    check = True
      
print(dusa_size)
    

    
    



