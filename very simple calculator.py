print('**********WELCOME TO MY CALCULATOR**********')

print('Just enter what you wanna do and this will give you result in one go! ie. if you wanna add 1 and 2, just enter 1 + 2 and so on\n')
num1,operator,num2 = input('Enter Calculations\n').split(' ')

num1 = int(num1)
num2 = int(num2)


#***************************************

sum = num1+num2
subtract = num1-num2
multiply = num1*num2
divide = num1/num2
modulus = num1%num2

#***************************************

if operator == ('+'):
  print('{}+{}={}'.format(num1,num2,sum))
elif operator == ('-'):
  print('{}-{}={}'.format(num1,num2,subtract))
elif operator == ('*'):
  print('{}*{}={}'.format(num1,num2,multiply))
elif operator == ('/'):
  print('{}/{}={}'.format(num1,num2,divide))
elif operator == ('%'):
  print('{}%{}={}'.format(num1,num2,modulus))