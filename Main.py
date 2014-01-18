#Product Name: Simple Sales Center (Castor Enterprise)
#Purpose: Contains the essential functions that are required to run the program
#
#These functions include:
#Searching
#Retreive save files
#Saving employee files
#deleting an employee
#Adding a new employee
#Changing an associate type to manager
#Changing an manager type to associate
#

import os

from Associate import *
from Manager import *

workIDList=[]
employeeList = []
outputList = []

"""
pre: if the files can be read succesfully, the information in the textfiles has to correspond to
     an integer, or a string, depending on which variable it represents.
     e.g. phone number must be an integer, names must be a string
post:The largest Id number is set by reading the first line of workIdNumbers.txt.
     The numbers after that(if any, )represent the textfiles that are supposed to be read by the program.
     e.g. if the textdocument says:
        5
        1
        2
        3
        5
        Then the largest Id number is set to 5
        The text documents that have to be read are 1.txt, 2.txt, 3.txt, 5.txt
     Based on those textdocuments, instances of the corresponding employees will be appended to the employeeList
purpose: To read the save files, contained in text documents, into the program
"""
def ReadFile():
    global largestEmployeeID
    try:

        f = open("workIdNumbers.txt", "r")

        largestEmployeeID = int(f.readline())


        workIDList = f.readlines()

        f.close()




        for fileName in workIDList:


            if (fileName[-1:] == "\n"):
                fileName = fileName[:-1]

            f = open ( (str(fileName) + ".txt"), "r")


            jobTitle = f.readline()[:-1]


            if (jobTitle == "Associate"):
                fileName= Associate(jobTitle, f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1],  f.readline()[:-1],
                                 f.readline()[:-1], f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],
                                 f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1],
                                 f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline())
                employeeList.append(fileName)


            elif (jobTitle == "Manager"):


                fileName = Manager(jobTitle, f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1],  f.readline()[:-1],
                                 f.readline()[:-1], f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],  f.readline()[:-1],
                                 f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1],
                                 f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline()[:-1], f.readline())
                employeeList.append(fileName)
            f.close()


    except:	#the workIDNumbers.txt will be reset to blank workId.txt if it can not read the save files properly

        print "except"
        f= open("WorkIDNumbers.txt", "w")
        f.write("0\n")
        largestEmployeeID = 0
        f.close()

"""
def UpdateIDFile():
    f=open("WorkIDNumbers.txt","w")

    for i in employeeList:
        f.write(i+"\n")

    f.close()

def WriteProfile(number, employeeList):
    for x in range(len(employeeList)):
        if employeeList[x]==number:
            f = open(str(number)+".txt","w")
            f.write(employeeList[x].GetFullInfo)
    f.close()
"""


"""
pre: largestEmployeeID must exist. employeeList must contain no instances, or instances of managers or associates
post:

All information of employeeList will be saved into textfiles.
ID numbers will be written into WorkIDNumbers.txt
Then, the getfull() info will be used to get all the information of an employee.

e.g.
for employeeList[0]
the employeeID will be written into WorkIDNumbers.txt
Then the string, getFullInfo, will be written into the textfile

purpose: To save all the information of employees in to corresponding textfiles
"""
def saveEverything():
    f=open("WorkIDNumbers.txt","w")
    f.write(str(largestEmployeeID) + "\n")
    for x in employeeList:
        f.write(str(x.GetEmployeeID()) + "\n")
        g=open(str(x.GetEmployeeID()) + ".txt","w")
        g.write(x.GetFullInfo())
        g.close()
    f.close()

"""
pre:
Each parameter put into the function has to correspond with the attributes in Employee
IDNUMBER IS NOT INPUTTED

post:
A new Associate or Manager will be appeneded to largestEmployeeID with the corresponding parameters.
purpose: To add new employee into the database
"""
def newEmployee(a,     c, d, e, f, g, i, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    global largestEmployeeID

    largestEmployeeID  =  largestEmployeeID + 1


    if   a == "Associate":
        blah = Associate(a, largestEmployeeID, c, d, e, f, g, i, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
        employeeList.append(blah)
    elif a == "Manager":
        blah = Manager(a, largestEmployeeID, c, d, e, f, g, i, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
        employeeList.append(blah)
"""
pre: index i must exist of employeeList
post: the employee of index I will have its type, and class changed to Manager
purpose: to change an employee from an associate(or manager) to manager
"""
def toManager(i):
    a = employeeList[i].GetJobTitle()
    b = employeeList[i].GetEmployeeID()
    c = employeeList[i].GetDepartment()
    d = employeeList[i].GetFirstName()
    e = employeeList[i].GetLastName()
    f = employeeList[i].GetGender()
    g = employeeList[i].GetBirthDate()
    h = employeeList[i].GetSINNumber()
    I = employeeList[i].GetPayroll()
    j = employeeList[i].GetMaritalStatus()
    k = employeeList[i].GetHomePhone()
    l = employeeList[i].GetWorkPhone()
    m = employeeList[i].GetAddress()
    n = employeeList[i].GetManagerName()
    o = employeeList[i].GetEducation()
    p = employeeList[i].GetStartDate()
    q = employeeList[i].GetEmail()
    r = employeeList[i].GetEmergencyFirstName()
    s = employeeList[i].GetEmergencyLastName()
    t = employeeList[i].GetEmergencyRelationship()
    u = employeeList[i].GetEmergencyPhoneNumber()
    v = employeeList[i].GetNumSickDaysTaken()
    w = employeeList[i].GetNumVacationDaysTaken()
    x = employeeList[i].GetPaytype()
    y = employeeList[i].GetNumDaysWorked()
    z = employeeList[i].GetOvertimeHours()
    deleteEmployee(b)
    blah = Manager("Manager", b, c, d, e, f, g, h, I, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
    employeeList.insert(i, blah)
"""
pre: index i must exist of employeeList
post: the employee of index I will have its type, and class changed to associate
purpose: to change an employee from an manager(or associate) to associate
"""
def toAssociate(i):
    a = employeeList[i].GetJobTitle()
    b = employeeList[i].GetEmployeeID()
    c = employeeList[i].GetDepartment()
    d = employeeList[i].GetFirstName()
    e = employeeList[i].GetLastName()
    f = employeeList[i].GetGender()
    g = employeeList[i].GetBirthDate()
    h = employeeList[i].GetSINNumber()
    I = employeeList[i].GetPayroll()
    j = employeeList[i].GetMaritalStatus()
    k = employeeList[i].GetHomePhone()
    l = employeeList[i].GetWorkPhone()
    m = employeeList[i].GetAddress()
    n = employeeList[i].GetManagerName()
    o = employeeList[i].GetEducation()
    p = employeeList[i].GetStartDate()
    q = employeeList[i].GetEmail()
    r = employeeList[i].GetEmergencyFirstName()
    s = employeeList[i].GetEmergencyLastName()
    t = employeeList[i].GetEmergencyRelationship()
    u = employeeList[i].GetEmergencyPhoneNumber()
    v = employeeList[i].GetNumSickDaysTaken()
    w = employeeList[i].GetNumVacationDaysTaken()
    x = employeeList[i].GetPaytype()
    y = employeeList[i].GetNumDaysWorked()
    z = employeeList[i].GetOvertimeHours()
    deleteEmployee(b)
    blah = Associate("Associate", b, c, d, e, f, g, h, I, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
    employeeList.insert(i, blah)

"""
pre: The Id number of the employee to be deleted, should exist, but it doesn't have to.
Post: to delete instance of the employee with an ID of "IdToBeDeleted". This will also remove the corresponding textfile
Purpose: To delete an employee from the system.
"""
def deleteEmployee(IdToBeDeleted):
    #IdToBeDeleted

    employeeListIndexToBeDeleted = -1
    for x in range(len(employeeList)):

        if employeeList[x].GetEmployeeID() == IdToBeDeleted:
            employeeListIndexToBeDeleted = x

    if (employeeListIndexToBeDeleted != -1):
        os.remove ( str(IdToBeDeleted) + ".txt")
        employeeList.pop(employeeListIndexToBeDeleted)
    else:
        print "Employee " + str(IdToBeDeleted) + " can not be deleted because it does not exist."

"""
pre : the index has to be an integer, the list has to be a list
post: This will place the index in the list, if that index isn't there already
purpose: This is to make sure that employee instance that matches the search
        query does not get repeated in the list. This is so that search results are not duplicated

"""
def putIndexInOutputList(index, list):
    isIndexInList = False
    counter = 0
    while(isIndexInList == False) and (counter < len(list)):
        if (list[counter] == index):
            isIndexInList = True
        counter +=1
    if isIndexInList == False:
        list.append(index)

    return list

"""
pre:query, must be a basic type of variable like string, integer or float.
post:
A list will be generated that contains the indexes of employeeList that have attributes that match query.
Using, putIndexInOutputList(), no results will be duplicated

purpose: to find employees who have an attribute that matches the query

"""
def search(query):
    global outputList
    outputList = [] #resets outputList to nothing so that new search results can be put in.

    query = str(query) # converts the query into a string so that it is easier to compare

    #each of these for loops are the same, except for the parameter that it is searching through.
    # I am just going to comment one to prevent redundancy

    for x in range(len(employeeList)):				#A for loop to scan through each employee
        if query in str(employeeList[x].GetSINNumber()):	#The loop checks if the query matches the SIN of the employee being scanned
            putIndexInOutputList(x, outputList)			#The index of that is put into the outputList if it isn't there already.


    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetStartDate()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetHomePhone()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetWorkPhone()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetPayroll()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetEmergencyPhoneNumber()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetEmployeeID()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetNumSickDaysTaken()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetNumVacationDaysTaken()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetPaytype()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetNumVacationDaysAvilable()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in str(employeeList[x].GetBirthDate()):
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetFirstName():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetLastName ():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetGender ():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetJobTitle ():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetDepartment ():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetEmail():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetMaritalStatus():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetAddress ():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetManagerName():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetEducation():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetEmergencyFirstName():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetEmergencyLastName():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetEmergencyRelationship():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetNumDaysWorked():
            putIndexInOutputList(x, outputList)
    for x in range(len(employeeList)):
        if query in employeeList[x].GetOvertimeHours():
            putIndexInOutputList(x, outputList)
    return outputList
