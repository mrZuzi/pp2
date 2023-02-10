def solve(numheads, numlegs):
    count1 = 0 
    count2 = 0   
     
    if(numheads >= numlegs):
        print('error')
    elif (numlegs %2 != 0):
        print("error")
    else:
         count1 = (numlegs-2*numheads)/2
         count2 = numheads - count1
    print(count1, count2)

solve(35,94)
