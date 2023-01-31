### Caleb Rivich
### Case Study: if... else and while
### This code is to request student names, their GPA, and
### to determine if they are on the Dean's List or Honor Roll

LastName = input('Please enter student last name ')

while LastName != 'ZZZ':
    FirstName = input('Please enter student first name ')
    StuGPA = float(input('Please enter student GPA '))
    if StuGPA >= 3.5:
        print('The student is on the Dean List')
        LastName = input('Please enter student last name ')
    elif StuGPA >= 3.25:
        print('The student is on the Honor Roll')
        LastName = input('Please enter student last name ')
    else:
        print('The student is not on a list')
        LastName = input('Please enter student last name ')
