#loads the main menu, gives you the option of registering as a time clock, or payroll system

def main():
    print("Welcome to the New Payroll System")
    print("1. Timeclock")
    print("2. Payroll")
    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            import timecard
            timecard.menu()
        elif choice == "2":
            import payroll_Main
            payroll_Main.menu()
        else:
            print("Invalid choice.  Please enter 1 or 2")




main()