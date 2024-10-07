# NO1. the volume of a sphere with radius r is (4/3)*pie r**2
#what is the volume of the sphere with radius 5
# make sure the program enters
#the radius from the kyeboard and provide the answer in 2 decimal places  

radius=int(input ("Enter the radius of the sphere:  "))
volume_of_the_sphere= (5)*(4/3)*(3.14)*(radius**2)
print(f"The volume of sphere {volume_of_the_sphere :.2f}")

#NO2 create a program to calculate the area of a triangle (1/2 *base* height).
#Base and height should be entered using the kyeboard
Base=int(input("Enter the base of the triangle:  "))
Height=int(input("Enter the height of the triangle:  "))
Area=(1/2)*Base*Height
print(f"The area of the triangle is {Area}")



#NO3 (i)WITI has tasked you to automate a simple grading sytem
#as a python student, write a program used to display the grades that the students will be receiving based on marks
#scored in the subject.The grades are:
#90% - 100% grade is A
#80% - 89% grade is B
#70% - 79% grade is C
#60% - 69% grade is D
#50% -59% grade is E
#<50% Fail 
marks_scored=int(input("\n Enter the scored marks:")) 
if marks_scored >= 90 and marks_scored <= 100:
    print("Grade is A")
elif marks_scored>=80 and marks_scored <=89: 
    print("Grade is B")
elif marks_scored>= 70 and marks_scored <=79:
    print("Grade is C")
elif marks_scored>= 60 and  marks_scored <=69:
    print("Grade is D")
elif marks_scored>=50 and marks_scored <= 59:
    print("Grade is E")
else:
    print("Fail")

 #NO4  WITI academy proposing the sacco to help students save their money
# design a platform that will do the following
# welcome to WITU ACADEMY SACCO
# 1.Deposit money
# 2.withdraw money
# 3.check balance
# ensure if the students selects 1, money is deposited and a minimum deposit should be 1000
# if the student selects two money should be withdrwn and the minum withdraw is 500
# if the student select 3 the account balance should be displayed
def sacco_transactions ():

    

    account_balance = 0 #Initial account_balance is 0
    run = 1
    while run == 1: #while loop
        print("\nWelcome to,WITI Academy Sacco")
        print("1.Deposit Money")
        print("2.Withdraw Money")
        print("3.Check Balance")
        
        student_choice = int(input("Please enter your choice(1,2,or 3):"))

        if student_choice == 1:
            print("\n....Processing a deposit transaction....")
            deposit_amount  = int(input("Enter amount to be deposited:"))
            if deposit_amount < 1000:
                print("\nMinimum deposit is 1000")
            else:
                account_balance += deposit_amount #same as account_balance = account_balance + deposit_amount
                print(f"Dear student, You have deposited {deposit_amount: ,} and Your new account balance is {account_balance: ,}")

        elif student_choice == 2:
            print("\n....Processing a withdraw transaction....")
            withdraw_amount = int(input("Enter amount to be withdrawn:"))
            if account_balance == 0:
                print("Your balance is 0")
            elif withdraw_amount <500:
                print("Minimum withdraw amount is 500")
            elif withdraw_amount > account_balance:
                print(f"Withdraw failed, insufficient funds.")
            else:
                account_balance -= withdraw_amount #same as account_balance = account_balance - withdraw_amount
                print(f"Dear student,You have withdrawn {withdraw_amount: ,} and Your new account balance is {account_balance: ,}")

        elif student_choice == 3:
            print(f"Your account balance is {account_balance: ,}")
        else:
            print("You entered a wrong choice! Please select 1,2 or 3\n")

        run = int(input("Enter 1 to continue or any number to exit:"))

        if run != 1:
            print(f"Thanks for using our Sacco.")
            break

sacco_transactions()

