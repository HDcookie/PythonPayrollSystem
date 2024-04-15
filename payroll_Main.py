import json
import os
from datetime import date

today = date.today()
# initialize variables and constants
counter = 0
process_record = 'y'

OTRATE = 1.5
ST_TAX_RATE = 0.04
FED_TAX_RATE = 0.1
SS_TAX_RATE = 0.062
MED_TAX_RATE = 0.0145


def checkstub():
    # open the file to read the data
    cis202file = open("../NewPayrollSystem/payroll.json", "r")

    # read the data from the file
    data = cis202file.read()
    print(data)
    cis202file.close()

    # calculate the pay
    data = calculate_pay(json.loads(data))

    try:
        os.mkdir("../NewPayrollSystem/payroll_checks")
    except FileExistsError:
        pass

    # delete all files in the payroll_checks folder upon user comfirmation
    delete = input("Continuing will delete all files in the payroll checks folder.  Continue? (y/n): ")
    if delete == "y":
        for file in os.listdir("../NewPayrollSystem/payrollHTML"):
            os.remove("payrollHTML/" + file)
        print("Files deleted")


    else:
        print("Exiting program")
        return

    # create a list with each user and data as one element
    for i in range(len(data)):
        print(data[i])
        print("\n \n \n")
        # run the code that formats the check and stores it in the payroll_checks folder
        import formatCheck
        formatCheck.formatCheck(data[i])

    # copys the css file to the payrollHTML folder
    import shutil
    shutil.copy("template.css", "payrollHTML/template.css")

    # sets the employee hours to 0 for each employee
    for i in range(len(data)):
        data[i]["Hours Worked"] = 0

    # write the data back to the file
    with open("../NewPayrollSystem/payroll.json", "w") as file:
        json.dump(data, file, indent=4)
    print("All checks created and hours reset")


def payRoll():
    # open the file to write the data
    print(" ")
    print("Insert a new employee record")
    process_record = 'y'
    data = []
    while process_record == 'y':
        empID = input("Enter the employee ID: ")
        empfName = input("Enter First name: ")
        emplName = input("Enter Last name: ")
        hours = 0  # this is now based on the timecard system
        payrate = float(input("Enter the pay rate: "))

        # calculate the date
        date = today.strftime("%m/%d/%y")

        tempData = {
            "Employee ID": empID,
            "Employee Name": empfName + " " + emplName,
            "Hours Worked": hours,
            "Pay Rate": payrate,
            "Date": date
        }

        # add temp data to the data json object before we close the loop
        data.append(tempData)

        process_record = input("Do you want to add another record? (y/n): ")

    # Outside the loop, write the data to the file

    # first get the current data from the file
    existing_data = []

    with open("payroll.json", "r") as file:
        fileContent = file.read()
        if fileContent != "":
            existing_data = json.loads(fileContent)

    # add the new data to the existing data
    newData = existing_data
    for item in data:
        newData.append(item)

    # write the data back to the file
    with open("payroll.json", "w") as file:
        json.dump(newData, file, indent=4)


def menu():
    print("Welcome to the New Payroll System")
    answer = input("Process Payroll or create check? (p for payroll, c for check): ")
    if answer == 'p':
        payRoll()
    elif answer == 'c':
        checkstub()
    else:
        print("Invalid option")
        return


def calculate_pay(data):
    # Calculate the pay per employee, and return the correct data, with net pay, taxes, etc.

    # start loopin through the data
    for i in range(len(data)):
        # calculate the gross pay
        data[i]["Gross Pay"] = data[i]["Hours Worked"] * data[i]["Pay Rate"]

        # calculate the overtime pay
        if data[i]["Hours Worked"] > 40:
            data[i]["Overtime Hours"] = data[i]["Hours Worked"] - 40
            data[i]["Overtime Pay"] = data[i]["Overtime Hours"] * OTRATE
        else:
            data[i]["Overtime Hours"] = 0
            data[i]["Overtime Pay"] = 0

        # calculate the state tax
        data[i]["State Tax"] = data[i]["Gross Pay"] * ST_TAX_RATE

        # calculate the federal tax
        data[i]["Federal Tax"] = data[i]["Gross Pay"] * FED_TAX_RATE

        # calculate the social security tax
        data[i]["Social Security Tax"] = data[i]["Gross Pay"] * SS_TAX_RATE

        # calculate the medicare tax
        data[i]["Medicare Tax"] = data[i]["Gross Pay"] * MED_TAX_RATE

        # calculate the net pay
        data[i]["Net Pay"] = (data[i]["Gross Pay"] - data[i]["State Tax"] - data[i]["Federal Tax"] -
                              data[i]["Social Security Tax"] - data[i]["Medicare Tax"])

    return data
