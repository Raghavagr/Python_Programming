import random

play_game = 'y'
start = 0
end =100
smallest = start
largest = end
direction = 'N'
while play_game == 'y':
    smallest=start
    largest = end
    print("Guess the no.")
    try_no=random.randint(start,end)
    print(try_no)
    count=0
    direction = 'N'
    while direction!='c':
        direction=input("Its Too Large 'l' or its too small 's' OR its correct 'c'")
        if direction == 's':
            if try_no>smallest:
                smallest = try_no + 1
                try_no = random.randint(smallest,largest)
                print(try_no)
        if direction == 'l':
            if try_no<largest:
                largest = try_no - 1
                try_no = random.randint(smallest,largest)
                print(try_no)
        count=count+1  
    print("I Got it! I tried "+str(count)+" no. of Times")
    play_game = input("continue?y/n")  

