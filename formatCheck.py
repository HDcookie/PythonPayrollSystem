from jinja2 import FileSystemLoader, Environment
import json

from payroll_Main import today
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def formatCheckOld(data):
    file = open("payroll_checks/" + data["Employee ID"] + ".txt", "w")
    file.write("Date: " + str(today) + "\n")
    file.write("Employee ID: " + data["Employee ID"] + "\n")
    file.write("Employee Name: " + data["Employee Name"] + "\n")
    file.write("Hours Worked: " + str(data["Hours Worked"]) + "\n")
    file.write("Gross Pay: " + str(data["Gross Pay"]) + "\n")
    file.write("Net Pay: " + str(data["Net Pay"]) + "\n")
    file.write("State Tax: " + str(data["State Tax"]) + "\n")
    file.write("Federal Tax: " + str(data["Federal Tax"]) + "\n")
    file.write("Social Security Tax: " + str(data["Social Security Tax"]) + "\n")
    file.write("Medicare Tax: " + str(data["Medicare Tax"]) + "\n")
    file.write("Overtime Hours: " + str(data["Overtime Hours"]) + "\n")
    file.write("Overtime Pay: " + str(data["Overtime Pay"]) + "\n")
    file.close()
    print("Check created for " + data["Employee Name"] + " with ID: " + data["Employee ID"])

    pass


dataOLD = {
    "Employee ID": "123",
    "Employee Name": "John Doe",
    "Hours Worked": 45,
    "Gross Pay": 400,
    "Net Pay": 300,
    "State Tax": 20,
    "Federal Tax": 40,
    "Social Security Tax": 30,
    "Medicare Tax": 10,
    "Overtime Hours": 0,
    "Overtime Pay": 0,
    "Date": "3/13/24"
}


def formatCheck(data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("template.html")
    with open("payrollHTML/" + data["Employee ID"] + ".html", "w") as file:
        file.write(template.render(item=data))



