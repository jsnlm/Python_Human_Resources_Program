#Product Name: Simple Sales Center (Castor Enterprise)
#Purpose: the employee class is the super class to Manager and Associate.
#         it has all the attributes that a regular employee has, including birthday, email, phone number, adress etc.


import datetime # to import the library that tells the current time/date


class Employee:

    #pre: all the parameters should be a string or an integer depending on the type of parameter is contains
    #     e.g. date, pone number and num sickdays are all examples of parameters that have to be integers
    #     e.g. jobTitle, department, first are example of paramteters that have to be strings
    #post: the attributes of the mployee instance are initiated
    #purpost: to set up an employee
    def __init__(self, jobTitle, employeeID, department, first,last, gender,birth, SIN,
    salaryOrRate, marital, homePhone, workPhone, address, managerName, education, startDate, #fax,
    email, emergencyFirst, emergencyLast, emergencyRelation, emergencyNumber       , numSickDaysTaken, numVacationDaysTaken, #bonus,
    paytype,
    numDaysWorked, overtimeHours):     #there are 25 parameters
        self.jobTitle=jobTitle;
        self.employeeID=employeeID;
        self.department=department;
        self.firstName=first;
        self.lastName=last;
        self.gender=gender;
        self.birthDate=birth;
        self.SIN=SIN;
        self.salaryOrRate=salaryOrRate;
        self.maritalStatus=marital;
        self.homePhone=homePhone;
        self.workPhone=workPhone;
        self.address=address;
        self.managerName=managerName;
        self.education=education;
        self.startDate=startDate;
        #self.fax=fax;
        self.email=email;
        self.emergencyFirstName=emergencyFirst;
        self.emergencyLastName=emergencyLast;
        self.emergencyRelationship=emergencyRelation;
        self.emergencyNumber=emergencyNumber
        self.paytype = paytype

        self.numSickDaysTaken = numSickDaysTaken
        self.numSickDaysAvilable = 5
        self.numVacationDaysTaken = numVacationDaysTaken
        self.numVacationDaysAvilable = 0
        #self.bonus = bonus
        self.type = "Employee"

        self.numDaysWorked = numDaysWorked
        self.overtimeHours = overtimeHours



    """
    pre : all the attributes should have been initiated
    post:
    returns all the attributes of the employee in the same format as would be read by ReadFile()
    purpose: helps out with the saving of employees by compoiling all the attributes into a single variable

    """
    def GetFullInfo(self):
        result=self.GetJobTitle() + "\n" + str(self.GetEmployeeID()) + "\n"+self.GetDepartment() + "\n" + self.GetFirstName() + "\n" + self.GetLastName() + "\n"+ self.GetGender() + "\n" + str(self.GetBirthDate()) +"\n"
        result += str(self.GetSINNumber())+"\n"+ str(self.GetPayroll())+"\n"+self.GetMaritalStatus()+ "\n"+ str(self.GetHomePhone())+"\n"+ str(self.GetWorkPhone())+"\n"
        result += self.GetAddress()+"\n"+self.GetManagerName()+"\n"+self.GetEducation()+"\n"+str(self.GetStartDate()) # +"\n"+str(self.GetFax())
        result +="\n"+self.GetEmail()+"\n"
        result += self.GetEmergencyFirstName()+ "\n" + self.GetEmergencyLastName() + "\n" + self.GetEmergencyRelationship()+"\n"+ str(self.GetEmergencyPhoneNumber()) +"\n"
        result += str(self.GetNumSickDaysTaken()) + "\n" + str(self.GetNumVacationDaysTaken()) #+ "\n"  + str(self.GetBonus())
        result += "\n" + self.GetPaytype() + "\n"
        result += str(self.GetNumDaysWorked()) + "\n" + str(self.GetOvertimeHours())
        return result

    #jobTitle, department, first, last, gender,birth,SIN,
    #salaryOrRate, marital, homePhone, workPhone, address, managerName, education, startDate, fax, email,
    #emergencyFirst, emergencyLast, emergencyRelation, emergencyNumber)

    #pre: self.firstName must have a value
    #post: self.firstName is returned
    #purpose: so that programs can reach the attribute, firstName, from employee list.
    def GetFirstName (self):
        return self.firstName

    #pre: self.lastName must have  a value
    #post: self.lastName is returned
    #purpose: so that programs can reach the attribute, lastName, from employee list.
    def GetLastName (self):
        return self.lastName

    #pre: self.gender must have  a value
    #post: self.gender is returned
    #purpose: so that programs can reach the attribute, gender, from employee list.
    def GetGender (self):
        return self.gender
    #pre: self.GetBirthDate must have  a value
    #post: self.GetBirthDate is returned
    #purpose: so that programs can reach the attribute, GetBirthDate, from employee list.
    def GetBirthDate(self):
        return self.birthDate
    def GetJobTitle (self):
        return self.jobTitle
    def GetDepartment (self):
        return self.department
    def GetSINNumber(self):
        return self.SIN
    def GetStartDate(self):
        return self.startDate
    def GetHomePhone (self):
        return self.homePhone
    def GetWorkPhone (self):
        return self.workPhone
    def GetEmail (self):
        return self.email
    def GetPayroll(self):
        return float(self.salaryOrRate)
    def GetMaritalStatus (self):
        return self.maritalStatus
    def GetAddress (self):
        return self.address
    def GetManagerName (self):
        return self.managerName
    def GetEducation (self):
        return self.education
    def GetEmergencyFirstName (self):
        return self.emergencyFirstName
    def GetEmergencyLastName (self):
        return self.emergencyLastName
    def GetEmergencyRelationship (self):
        return self.emergencyRelationship
    def GetEmergencyPhoneNumber (self):
        return self.emergencyNumber
    def GetEmployeeID (self):
        return int(self.employeeID)

    def GetNumSickDaysTaken (self):
        return int(self.numSickDaysTaken)
    def GetNumVacationDaysTaken (self):
        return int(self.numVacationDaysTaken)
    #def GetBonus (self):
    #    return self.bonus
    def GetPaytype (self):
        return self.paytype
    def GetNumDaysWorked (self):
        return self.numDaysWorked
    def GetOvertimeHours (self):
        return self.overtimeHours

    def GetNumVacationDaysAvilable(self):
        now = datetime.datetime.now()

        startDateYear = int(self.GetStartDate())/10000


        if ((now.year - startDateYear) <= 5) and ((now.year - startDateYear) >=0):
            numVacationDaysAvilable = 14
        elif ((now.year - startDateYear) <= 10) and ((now.year - startDateYear) >=6):
            numVacationDaysAvilable = 21
        elif (now.year - startDateYear) >=11:
            numVacationDaysAvilable = 28

        return numVacationDaysAvilable


    def SetFirstName(self, newName):
        self.firstName=newName
    def SetLastName(self, newName):
        self.lastName=newName
    def SetGender (self, gender):
        self.gender=gender
    def SetJobTitle(self, newJobTitle):
        self.jobTitle=newJobTitle
    def SetPayroll(self, newSalaryOrPayRate):
        self.salaryOrRate=newSalaryOrPayRate
    def SetDepartment(self, newDepartment):
        self.department=newDepartment
    def SetSINNumber(self, newNumber):
        self.SIN=newNumber
    def SetMaritalStatus(self, newStatus):
        self.maritalStatus= newStatus
    def SetManagerName (self, manName):
        self.managerName=manName
    def SetEducation(self, newEducation):
        self.education=newEducation
    def SetStartDate(self, startDate):
        self.startDate=startDate
    def SetBirthDate(self,birthDate):
        self.birthDate=birthDate
    def SetAddress(self, newAddress):
        self.address=newAddress
    def SetHomePhone(self, newPhone):
        self.homePhone=newPhone
    def SetWorkPhone(self, newPhone):
        self.workPhone=newPhone
    def SetEmail(self, newEmail):
        self.email=newEmail
    #def SetFax(self, newFax):
    #    self.fax=newFax
    def SetEmergencyFirstName(self, firstName):
        self.emergencyFirstName=firstName
    def SetEmergencyLastName(self, lastName):
        self.emergencyLastName=lastName
    def SetEmergencyRelationship(self, newRelation):
        self.emergencyRelationship=newRelation
    def SetEmergencyNumber(self, newNumber):
        self.emergencyNumber=newNumber
    def SetEmployeeID(self, newNumber):
        self.employeeID=newNumber

    def SetNumSickDaysTaken (self, newNumber):
        self.numSickDaysTaken = newNumber
    def SetNumVacationDaysTaken (self, newNumber):
        self.numVacationDaysTaken = newNumber
    #def SetBonus (self, newNumber):
    #    self.bonus = newNumber
    def SetPaytype (self, newpaytype):
        self.paytype = newpaytype

    def SetNumDaysWorked (self, newNumDaysWorked):
        self.numDaysWorked = newNumDaysWorked
    def SetOvertimeHours (self, newOvertimeHours):
        self.overtimeHours = newOvertimeHours












