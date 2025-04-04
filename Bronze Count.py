n = int(input())
input_lst = []

for i in range(n):
    input_lst.append(int(input()))
    
first_max = max(input_lst)

count = 0

for elem in input_lst:
    if first_max == elem:
        count = count + 1
 
for i in range(count):
    input_lst.remove(first_max)

second_max = max(input_lst)
    
count = 0

for elem in input_lst:
    if second_max == elem:
        count = count + 1
    
for i in range(count):
    input_lst.remove(second_max)
    
third_max = max(input_lst)
        
count = 0
    
for elem in input_lst:
    if third_max == elem:
        count = count + 1
        
print(f"{third_max} {count}")
        
