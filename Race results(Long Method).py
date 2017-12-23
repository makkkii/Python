#Backstory--Three friends naming Makki, Rahul and Sahil participated in a race, Makki came first, Rahul second and Sahil came last. So this program returns the position of the person when we enter his name.
def choice_to_number(choice):
  choice = str(input("Enter your choice"))
  
  if choice == 'Makki':
    return 1
  elif choice == 'Rahul':
    return 2
  elif choice == 'Sahil':
    return 3
print(choice_to_number('choice'))
