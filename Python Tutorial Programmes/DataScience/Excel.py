# Microsoft Excel is a very widely used spread sheet program.
# Its user friendliness and appealing features makes it a very frequently used tool in Data Science.
# The Panadas library provides features using which we can read the Excel file in full as well as
# in parts for only a selected group of Data. We can also read an Excel file with multiple sheets in it.
# We use the read_excel function to read the data from it.

import pandas as pd
data = pd.read_excel('input.xlsx')
print (data)

# Similar to what we have already seen in the previous chapter to read the CSV file, the read_excel function of the
# pandas library can also be used to read some specific columns and specific rows.

print (data.loc[[1,3,5],['salary','name']])

# Multiple sheets with different Data formats can also be read by
# using read_excel function with help of a wrapper class named ExcelFile.

with pd.ExcelFile(r'C:\Users\User\Desktop\Python\DataScience\input.xlsx') as xls:
    df1 = pd.read_excel(xls, 'Лист1')
    df2 = pd.read_excel(xls, 'Лист2')

print("****Result Sheet 1****")
print (df1[0:5]['salary'])
print("")
print("***Result Sheet 2****")
print (df2[0:5]['zipcode'])
