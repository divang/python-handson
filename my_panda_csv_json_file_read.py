import pandas as pd
import numpy as np
dataframe_from_csv = pd.read_csv('data.csv')
#print(dataframe_from_csv)
#print(dataframe_from_csv.head(3))

dataframe_from_json = pd.read_json('data.json')
'''
#print(dataframe_from_json)
print(dataframe_from_json.head(3))
print(dataframe_from_json.info())

print(dataframe_from_json["Calories"].mean())
#print(dataframe_from_json["Calories"].avg())
print(dataframe_from_json["Calories"].min())
print(dataframe_from_json["Calories"].max())
print(dataframe_from_json["Calories"].sum())
'''

# Merge two Dataframes based on keys
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
print(left)
print(right)

merge_dataframe  = pd.merge(left, right, on="key")
print(merge_dataframe)

'''
   key  lval
0  foo     1
1  bar     2
   key  rval
0  foo     4
1  bar     5

   key  lval  rval
0  foo     1     4
1  bar     2     5
'''

# Grouping and aggregation
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

print(df)

print(df.groupby("A").sum())
print(df.groupby(["A", "B"]).sum())


