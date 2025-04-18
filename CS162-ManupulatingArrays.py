import numpy as np
array1 = np.random.randint(0,99, size=(5,5), dtype=int) #generate a 5x5 array filled with random integers from 0-99
print(array1) #print the array
print(array1[1,2]) #print the number from the 2nd row, 3rd column
print(np.sum(array1[:,:])) #print the sum of all the elements in the array
print(np.mean(array1, axis=1)) #print the mean of each row in the array
print(np.max(array1, axis=0)) #print the maximum value in each column of the array