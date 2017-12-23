#This code takes name and age of the user as input, prints it and tells the user that when he is going to turn 100 years old.
Name = str(input('Please enter your name - '))
Age = int(input('And what is your age ? '))
year = 2017+(100-Age)

print('Hi ',Name,' Your age is - ',Age,' And i have one more option for you! ')
ques = str(input('Would you like to know by which year you will turn 100 ? , if yes press 1 or press 2 to exit - '))
if ques == ('1'):
    print('You will turn 100 by -',year)
else:

    print('Thanks You! & Bbye')
