"""
 Convert multidimensional list rows into columns

    1 2 3     1 4 7
    4 5 6  >  2 5 8
    7 8 9     3 6 9
"""
def rowsIntoColumns(list):
    res = []
    for j in range(len(list[0])):
        temp = []
        for i in list:
            temp.append(i[j])
        res.append(temp)
"""

"""