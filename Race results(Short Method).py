#Backstory--Three friends naming Makki, Rahul and Sahil participated in a race, Makki came first, Rahul second and Sahil came last. So this program returns the position of the person when we enter his name.
#Smaller version.
def choice_to_number(choicee):
  choice = str(input("Enter your choice-->"))
  return {'Makki':1,'Rahul':2,'Sahil':3}[choice]
print(choice_to_number('choice'))
