#Product Name: Simple Sales Center (Castor Enterprise)
#Purpose: Manager class ia a subclass of an employee class, it is distinct from employee class becase of its type and the way it is paid
from Employee import *

class Manager(Employee):

   	#pre: all the parameters should be a string or an integer depending on the type of parameter is contains
    #     e.g. date, pone number and num sickdays are all examples of parameters that have to be integers
    #     e.g. jobTitle, department, first are example of paramteters that have to be strings
    #post: the attributes of the mployee instance are initiated
    #purpost: to set up an Manager

    def __init__(self, jobTitle, employeeID, department, first,last, gender,birth, SIN,
    salaryOrRate, marital, homePhone, workPhone, address, managerName, education, startDate, #fax,
    email, emergencyFirst, emergencyLast, emergencyRelation, emergencyNumber       , numSickDaysTaken, numVacationDaysTaken, #bonus,
    paytype,
    numDaysWorked, overtimeHours):
        Employee.__init__(self, jobTitle, employeeID, department, first,last, gender,birth, SIN,
    salaryOrRate, marital, homePhone, workPhone, address, managerName, education, startDate, #fax,
    email, emergencyFirst, emergencyLast, emergencyRelation, emergencyNumber       , numSickDaysTaken, numVacationDaysTaken, #bonus,
    paytype,
    numDaysWorked, overtimeHours)

        self.type = "Manager"

	#pre: time, bonus and overtime must all be integers or floats
    #post: the pay of this Manageris paid taking into accound the parameters, as well as the number of vacation days available and the number of sick days available
    #purpose: to get the pay of an Manager
    def Pay(self, time, overtime):
        time = float(time)
        time = time/7
        overtime = float(overtime)
        pay = 0
        pay = ((self.GetPayroll())/52)*time

        if self.GetNumVacationDaysTaken()>self.GetNumVacationDaysAvilable():
            pay=pay-(self.GetNumVacationDaysTaken()-self.GetNumVacationDaysAvilable())*(self.GetPayroll()/365)
        if self.GetNumSickDaysTaken()>5:
            pay=pay-(self.GetNumSickDaysTaken()-5)*(self.GetPayroll()/365)

        return pay