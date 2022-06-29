import numpy as np
print(np.__version__)

# 1 Dimension array
list=  [1,2,3,4,5,6]
# index 0 1 2 3 4 5
print(list[1])

print(list)
one_dimension_array=np.array(list)
print(one_dimension_array)
print("Dimension of one_dimension_array:", one_dimension_array.ndim)

row0=[1,2,3,4]
row1=[11,12,13,14]
row2=[21,22,23,24]

'''
    [0]   [1]    [2]    [3]
[0]  1     2     3      4
	[0,0] [0,1]  [0,2] [0,3]
[1] 11     12    13     14
	[1,0] [1,1]  [1,2]
[2] 21     22     23    24 
	[2,0]              [2,3] 
'''
list_of_lists= [row0, row1, row2]

two_dimension_array=np.array(list_of_lists)
print(two_dimension_array)
print("Dimension of two_dimension_array:", two_dimension_array.ndim)

# Acces elements from 2D array
print(two_dimension_array[2,3])

group0_row0=[1,2,3,4]
group0_row1=[11,12,13,14]
group1_row0=[21,22,23,24]
group1_row1=[31,32,33,34]

list_of_list_of_list= [[group0_row0, group0_row1], [group1_row0,group1_row1]]

three_dimension_array=np.array(list_of_list_of_list)
print(three_dimension_array)
print("Dimension of three_dimension_array:", three_dimension_array.ndim)

# Acces elements from 3D array
print(three_dimension_array[1,1,1])




