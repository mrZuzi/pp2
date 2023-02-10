def spy_game(): 
    nums = [int(x) for x in input().split()]
    for i in nums:
        if i == 0:
            if nums[nums.index(i)+1] == 0:
                if nums[nums.index(i)+2] == 7:
                    print("True")
                    exit(0)
    print('False')
spy_game()
    
    