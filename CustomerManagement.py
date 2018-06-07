    #----------End of BLL------------
    #----------Start PL------------
import json
import pickle
#---------BLL Start------------
class Customer:
  cusList = []
  d = {}
  def __init__(self):
    self.Id = 0
    self.Name = None
    self.Age = 0
    # if (j == None):
    #   self.Id = 0
    #   self.Name = None
    #   self.Age = 0
    # else:
    #   self.Id = j['Id']
    #   self.Name = j['Name']
    #   self.Age = j['Age']
  def showCustomer(self):
    print('Id: ',self.Id,'Name: ',self.Name, 'Age: ',self.Age)
  def addCustomer(self):
    Customer.cusList.append(self)
  @staticmethod
  def showAllCustomer():
    for cus in Customer.cusList:
      cus.showCustomer()
  def getDetails(self,Id):
    for cus in Customer.cusList:
      if (cus.Id == Id):
        self.Id = cus.Id
        self.Name = cus.Name
        self.Age = cus.Age
  def deleteCustomer(self,Id):
    for index in range(len(Customer.cusList)):
      if Customer.cusList[index].Id == Id:
        Customer.cusList.pop(index)
        return
  @staticmethod
  def convertDictToObj(d):
    return Customer()
  @staticmethod
  def convertObjectIntoJson(obj):
    return vars(obj)
  @staticmethod
  def saveListIntoFile():
    f = open("CustomerList.txt",'w')
    json.dump(Customer.cusList,f,default=Customer.convertObjectIntoJson)
    f.close()
    print('Save file Success!!')
  @staticmethod
  def loadIntoList():
    f = open("CustomerList.txt",'r')
    data = json.load(f,object_hook=Customer.convertDictToObj)
    Customer.cusList = list(data)
    print('Done!')

cus=Customer()
count = 0
while(True):
  print('1. Add Customer: ')
  print('2. Search Customer: ')
  print('3. Delete Customer: ')
  print('4. Show all Customer: ')
  print('5. Sort: ')
  print('6. Save Data: ')
  print('7. Load Data: ')
  print('0. Exit: ')
  c = input("Enter your Choice: ")
  if c == '1':
    cus1 = Customer()
    count += 1
    cus1.Id = count
    cus1.Name = input('Enter Name: ')
    cus1.Age = input('Enter Age: ')
    cus1.addCustomer()
    print('Customer Added successfully.')
  elif(c=='2'):
    cusId = input('Enter Customer Id: ')
    cus = Customer()
    cus.getDetails(cusId)
    cus.showCustomer()
  elif(c=='3'):
    cusid = input('Enter the Id of Customer you want to delete: ')
    cus = Customer()
    cus.deleteCustomer(cusid)
  elif(c=='4'):
    Customer.showAllCustomer()
  elif(c=='6'):
    Customer.saveListIntoFile()
  elif(c=='7'):
    Customer.loadIntoList()
  elif(c=='0'):
    exit()
