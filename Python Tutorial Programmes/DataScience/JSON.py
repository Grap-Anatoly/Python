# The read_json function of the pandas library can be used to read the JSON file into a pandas DataFrame.

import pandas as pd

data = pd.read_json('json.json')
print(data)

# Similar to what we have already seen in the previous chapter to read the CSV file,
# the read_json function of the pandas library can also be used to read some
# specific columns and specific rows after the JSON file is read to a DataFrame.

print (data.loc[[1,3,5],['Salary','Name']])

# We can also apply the to_json function along with parameters to read the JSON file content into individual records.

print(data.to_json(orient='records', lines=True))