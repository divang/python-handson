# Exploring Panda module
import pandas as pd
print(pd.__version__)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
#print(mydataset)
# Creating Dataframe -> Multi Dimension

first_dataframe=pd.DataFrame(mydataset)

#print(first_dataframe)

# Creating Series -> ! dimension array
a = [1,2,3,4,5]
first_series = pd.Series(a)
#print(first_series)
#print(first_series[1])

# Series with default index
patrol_expense_list = [1000,3000,4000]
patrol_expense_series_with_default_index = pd.Series(patrol_expense_list)
#print(patrol_expense_series_with_default_index)
#print(patrol_expense_series_with_default_index[0])

# Creating Labels 
patrol_expense_series_with_label = pd.Series(patrol_expense_list, index =["Jan", "Feb" , "Mar"]) 
#print(patrol_expense_series_with_label)
#print(patrol_expense_series_with_label["Jan"])


# More calculation around DataFrame (Multi Arrays)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

gym_stat = pd.DataFrame(data)
print(gym_stat)
'''
   calories  duration
0       420        50  [row one]
1       380        40  [row two]
2       390        45  [row three]
'''

# Get First Row
print(gym_stat.loc[0])

# Get Multiple rows
print(gym_stat.loc[[0,2]])
'''
   calories  duration
0       420        50 [row one]
2       390        45 [row three]
'''





