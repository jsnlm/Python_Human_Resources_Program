#Product Name: Simple Sales Center (Castor Enterprise)

#Date: February 4, 2013
#Purpose: Associate class ia a subclass of an employee class, it is distinct from employee class becase of its type and the way it is paid

from Employee import *


class Associate(Employee):

    #pre: all the parameters should be a string or an integer depending on the type of parameter is contains
    #     e.g. date, pone number and num sickdays are all examples of parameters that have to be integers
    #     e.g. jobTitle, department, first are example of paramteters that have to be strings
    #post: the attributes of the mployee instance are initiated
    #purpost: to set up an Associate
    def __init__(self, jobTitle, employeeID, department, first,last, gender,birth, SIN,
    salaryOrRate, marital, homePhone, workPhone, address, managerName, education, startDate, #fax,
    email, emergencyFirst, emergencyLast, emergencyRelation, emergencyNumber       , numSickDaysTaken, numVacationDaysTaken, #bonus,
    paytype,
    numDaysWorked, overtimeHours):
        Employee.__init__(self, jobTitle, employeeID, department, first,last, gender,birth, SIN,# uses the parameters, and input them into the init statements of employee
    salaryOrRate, marital, homePhone, workPhone, address, managerName, education, startDate, #fax,
    email, emergencyFirst, emergencyLast, emergencyRelation, emergencyNumber       , numSickDaysTaken, numVacationDaysTaken, #bonus,
    paytype,
    numDaysWorked, overtimeHours)

        self.type = "Associate" #sets the type of the associate as Associate

    #pre: time, bonus and overtime must all be integers or floats
    #post: the pay of this associate is paid taking into accound the parameters, as well as the number of vacation days available and the number of sick days available
    #purpose: to get the pay of an associate
    def Pay(self, time, overtime):
        overtime = int(overtime)
        pay = 0
        if self.GetPaytype()=="Salary":
            time= int(time)/7
            pay = ((self.GetPayroll())/52)*time

            if self.GetNumVacationDaysTaken()>self.GetNumVacationDaysAvilable():
                pay=pay-(self.GetNumVacationDaysTaken()-self.GetNumVacationDaysAvilable())*(self.GetPayroll()/365)
            if self.GetNumSickDaysTaken()>5:
                pay=pay-(self.GetNumSickDaysTaken()-5)*(self.GetPayroll()/365)


        elif self.GetPaytype() == "Wage":
            time=int(time)*8
            pay = self.GetPayroll()*time + self.GetPayroll()*1.5*overtime
            if self.GetNumVacationDaysTaken()>self.GetNumVacationDaysAvilable():
                pay=pay-(self.GetNumVacationDaysTaken()-self.GetNumVacationDaysAvilable())*8
            if self.GetNumSickDaysTaken()>5:
                pay=pay-(self.GetNumSickDaysTaken()-5)*8

        return pay