import json
from datetime import datetime

employees_clocked_in = {}
employeeIds = []


def get_clocked_in_employees():
    return employees_clocked_in


def clockin():
    print("What is your employee ID?")
    id = input("> ")

    if (id in employees_clocked_in):
        print("")
        print("")
        print("You are already clocked in.")
        return

    # checks if the employee ID is valid, if not, it will return an error
    if id not in employeeIds:
        print("")
        print("")
        print("Invalid employee ID.")
        return

    print("")
    print("")
    print("You clocked in at", datetime.now())

    employees_clocked_in[id] = datetime.now()


def clock_out():
    print("What is your employee ID?")
    id = input("> ")

    if id not in employees_clocked_in:
        print("")
        print("")
        print("You are not clocked in.")
        return

    print("")
    print("")
    print("You clocked out at", datetime.now())

    clocked_in_time = employees_clocked_in[id]
    clocked_out_time = datetime.now()
    hours_worked = clocked_out_time - clocked_in_time
    employees_clocked_in.pop(id)

    # format the hours worked to be in hours, minutes, seconds
    total_seconds = hours_worked.total_seconds()
    # get hours, remainder = total seconds
    hours, remainder = divmod(total_seconds, 3600)
    # get minutes from remainder, remainder = remaining seconds
    minutes, seconds = divmod(remainder, 60)

    print(f"You worked: {hours} hours, {minutes} minutes, {seconds} seconds")


    save_timecard(id, hours_worked)


def save_timecard(id, hours_worked):
    # code to save the timecard to a file

    # get the previously hours from the payroll.json file
    previous_hours = 0
    # copy of the file so we can read and write to it
    jsonn = {}

    with open("payroll.json", "r") as file:
        data = json.load(file)
        jsonn = data
        for employee in data:
            if employee["Employee ID"] == id:
                previous_hours = employee["Hours Worked"]
                break


    # update the hours worked
    with open("payroll.json", "w") as file:
        data = jsonn
        for employee in data:
            if employee["Employee ID"] == id:
                # convert the hours worked to a float
                employee["Hours Worked"] = previous_hours + hours_worked.total_seconds() / 3600
                print("Total Hours worked: ", hours_worked.total_seconds() / 3600)
                break
        json.dump(data, file)


def menu():
    # gets list of employee ID's that are valid employees from payroll.json
    # opens the file and reads the data
    with open("payroll.json", "r") as file:
        data = json.load(file)
        for employee in data:
            employeeIds.append(employee["Employee ID"])

    for i in range(100):
        print(" ")

    while True:

        print("")
        print("")
        print("Welcome to the timecard system")
        print("1. Clock in")
        print("2. Clock out")

        choice = input("Enter your choice: ")
        if choice == "1":
            clockin()
        elif choice == "2":
            clock_out()
        elif choice == "q":
            break
        else:
            print("")
            print("")
            print("Invalid choice.")


menu()
