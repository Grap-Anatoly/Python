import json

class PhoneBook:
    
    def setTemporaryList(name,surname,phone,personalPhone,age):
        tempList={}
        
        tempList["name"] = name
        tempList["surname"] = surname
        tempList["phone"] = phone
        tempList["phoneBook"] = personalPhone
        tempList["age"] = age
    
        return tempList
        
    def exportData(dataList):
        file = open("phoneBook.json", "w")
        # or use direct adress r"C:\Users\User\Desktop\Python\Lab-3\phoneBook.json"
        file.write(json.dumps(dataList))
        file.close
    
    online = True
    
    print ("Enter name: ") 
    name = input() 
    print ("Enter Surname: ")
    surname = input() 
    print ("Enter phone: ")
    phone = int(input()) 
    print ("Enter Personal phone: ")
    personalPhone = int(input()) 
    print ("Enter age: ")
    age = int(input())  
    
    tempDataList = setTemporaryList(name,surname,phone,personalPhone,age)
    
    dataList = [tempDataList]
    
    while online == True:
        
        print("1.Enter additional data")
        print("2.Examine data")
        print("3.End programm")
        
        choice = int(input("Enter 1-3: "))
        
        # print(choice)

        if (choice == 1) : 
            print ("Enter name: ") 
            name = input() 
            print ("Enter Surame: ")
            surname = input() 
            print ("Enter phone: ")
            phone = int(input()) 
            print ("Enter Personal phone: ")
            personalPhone = int(input()) 
            print ("Enter age: ")
            age = int(input()) 
            tempDataList = setTemporaryList(name,surname,phone,personalPhone,age)
            dataList.append(tempDataList)
            
        elif (choice == 2) : 
            print(dataList) 
            
        elif (choice == 3) : 
            exportData(dataList)
            online = False