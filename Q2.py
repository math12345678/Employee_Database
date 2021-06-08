run=True
def exit_code():
    global run
    run=False
def findby_ID():
    check=input("Enter your ID\n")
    f=open("employee_database2.txt","r")
    lines=f.readlines()
    for line in lines:
        data=line.split(',')
        if data[0]==check:
            print("ID: "+str(data[0])+"\nName: "+data[1]+"\nSalary: "+str(data[2]))
    f.close()
def findby_Name():
    check=input("Enter your Name\n")
    f=open("employee_database2.txt","r")
    lines=f.readlines()
    for line in lines:
        data=line.split(',')
        if data[1]==check:
            print("ID: "+str(data[0])+"\nName: "+data[1]+"\nSalary: "+str(data[2]))
    f.close()
def findby_Salary():
    check=input("Enter your Salary\n")
    f=open("employee_database2.txt","r")
    lines=f.readlines()
    for line in lines:
        data=line.split(',')
        if data[2]==check:
            print("ID: "+str(data[0])+"\nName: "+data[1]+"\nSalary: "+str(data[2]))
    f.close()
def new_employee():
    f=open("employee_database2.txt","a")
    ID=input("What is the new employee's ID\n")
    name=input("What is the new employee's name\n")
    salary=int(input("What is the new employee's salary\n"))
    f.write(str(ID)+","+name+","+str(salary)+"\n")
    f.close()
def filter_salary():
    limit=int(input("Enter the salary amount that you want to filter on\n"))
    f=open("employee_database2.txt","r")
    lines=f.readlines()
    for line in lines:
        data=line.split(',')
        if int(data[2].replace("\n",""))>=limit:
            print("ID: "+str(data[0])+"\nName: "+data[1]+"\nSalary: "+str(data[2]))
    f.close()
def all_employees():
    f=open("employee_database2s.txt","r")
    lines=f.readlines()
    for line in lines:
        data=line.split(",")
        print("ID: "+str(data[0])+"\nName: "+data[1]+"\nSalary: "+str(data[2]))
while run:
    choices=int(input("Enter the choice you would like to choose\n1: Add new employee\n2: Search an employee by filtering if the employee's salary is greater than a certain amount\n3: Find an employee by his/her ID\n4: Find an employee by his/her Name\n5: Find an employee by his/her Salary\n6: See all the employees\n7: Exit the code\n"))
    if choices==1:
        new_employee()
    elif choices==2:
        filter_salary()
    elif choices==3:
        findby_ID()
    elif choices==4:
        findby_Name()
    elif choices==5:
        findby_Salary()
    elif choices==6:
        all_employees()
    elif choices==7:
        exit_code()
    else:
        exit_code()