import numpy as np
#1
vec=np.arange(0,10.5, 0.5)
print(vec)

#infos
vec.size
print("The size of vec is : ", vec.size)
vec.ndim
print ("The ndim of vec is : ", vec.ndim)

#3
print("The shape of vec is : ", vec.shape)

#4
print("The 7th value of vec is : ", vec[6])

#5
print("The 3 first items are : ", vec[0:3])

#6
print("The 3 last items are : ", vec[-3:])

#7
print("value of vec < 7 : are (boolean) ", vec > 7)
print("value of vec < 7 : are ",vec[vec < 7])
#ou
mask = (vec <7)
print(mask)

filtered_vec=vec[mask]
print(filtered_vec)

#8
def my_func(x,y):
    return x**2 + y

x = 0
y = 1

resultat = my_func(x,y)

print (resultat)

#9
matrix = np.fromfunction(my_func,(4,4),dtype=int)
print (matrix)

#10
for x in matrix.flat:
  print("When dividing {} by 2, the remainder is: {}".format(x, x%2))

mask2=(matrix%2==0)
even_numbers = matrix[mask2]
print("Even numbers are : ", even_numbers)

#11

even_numbers_reshaped = even_numbers.reshape(2, 4)
print(even_numbers_reshaped)

np.log(even_numbers_reshaped)

#12