# loads the main menu, gives you the option of registering as a time clock, or payroll system

def main():
    for i in range(100):
        print(" ")
    print("Welcome to the New Payroll System")
    print("1. Timeclock")
    print("2. Payroll")
    print("q. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        import timecard
        timecard.menu()
    elif choice == "2":
        import payroll_Main
        payroll_Main.menu()
    elif choice == "q":
        exit()
    else:
        print("Invalid choice.  Please enter 1 or 2")


while True:
    main()
