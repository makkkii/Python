print('**********WELCOME TO MY CALCULATOR**********')

num1,num2 = input('Enter the two numbers separated by a comma ').split(',')
num1 = int(num1)
num2 = int(num2)

#func-->fucntion of calculator

func = input('Please choose what function you want to run\nTo add  type add\nTo subtract type subtract\nTo get product type multiply\nTo divide type divide\nTo get the modulus modulus\n ')

#****************************************
func = str(func)


#***************************************

sum = num1+num2
subtract = num1-num2
multiply = num1*num2
divide = num1/num2
modulus = num1%num2

#***************************************

if func == ('add'):
  print('{}+{}={}'.format(num1,num2,sum))
elif func == ('subtract'):
  print('{}-{}={}'.format(num1,num2,subtract))
elif func == ('multiply'):
  print('{}*{}={}'.format(num1,num2,multiply))
elif func == ('divide'):
  print('{}/{}={}'.format(num1,num2,divide))
elif func == ('modulus'):
  print('{}%{}={}'.format(num1,num2,modulus))
