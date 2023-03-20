a = [1,2,1,1,4,5]
item  = 1
count = 0
for i in range(0,len(a)-1):
        if(item == a[i]):
               count =  count + 1
               if(count == 2):
                      del a[i]
                      break
print(a)