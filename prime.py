l= [3,7,5,1,9,45,96,17,11,19]
prime=[]
for i in l:
    count =0
    for j in range(2,i):
        if(i%j ==0):
            count =count + 1
            break

            if (count ==1):
                prime.append(i)
                print("prime are",prime)
