### Part Four -- your code goes here. 
import random
randomnum = [random.randint(1, 100) for _ in range(10)]
print("List of 10 random numbers: ", randomnum)
index = 0
while index < len(randomnum):
    if randomnum[index] % 2 == 0: 
        randomnum.pop(index)  
    else:
        index += 1  

print("Odd numbers from the list are: ", randomnum)