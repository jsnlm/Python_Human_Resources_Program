#Castor Solutions
#Feburary 3, 2013




from Main import*       #Importing attributes and functions from the Main file/class
from PyQt4 import QtCore, QtGui     #Importing attributes and functions from the PyQt4 file/class related with QtCore and QtGui
import sys      #Importing sys file/class
#ReadFile()      #Allowing this file to read textfiles

global outputList           #A global variable named 'outputList' which will contain results that satisfy the search

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SearchWindow(object):      #Setting the window for the graphic user interface

    def setupUi(self, MainWindow):
        global outputList

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)     #Setting the size of the main search window

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.searchTable = QtGui.QTableWidget(self.centralwidget)
        self.searchTable.setGeometry(QtCore.QRect(20, 110, 751, 401))       #Setting the location/size of the table in the window
        self.searchTable.setObjectName(_fromUtf8("searchTable"))
        self.searchTable.setColumnCount(23)       #There are total 23 horizontal lines in the table
        self.searchTable.setRowCount(100)       #There are total 100 vertical lines in the table


        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(0, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(1, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(2, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(3, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(4, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(5, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(6, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(7, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(8, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(9, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(10, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(11, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(12, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(13, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(14, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(15, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(16, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(17, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(18, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(19, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(20, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(21, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(22, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(23, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(24, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(25, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(26, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(27, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(28, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(29, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(30, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(31, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(32, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(33, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(34, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(35, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(36, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(37, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(38, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(39, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(40, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(41, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(42, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(43, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(44, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(45, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(46, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(47, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(48, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(49, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(50, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(51, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(52, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(53, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(54, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(55, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(56, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(57, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(58, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(59, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(60, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(61, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(62, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(63, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(64, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(65, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(66, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(67, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(68, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(69, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(70, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(71, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(72, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(73, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(74, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(75, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(76, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(77, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(78, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(79, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(80, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(81, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(82, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(83, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(84, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(85, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(86, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(87, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(88, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(89, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(90, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(91, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(92, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(93, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(94, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(95, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(96, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(97, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(98, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setVerticalHeaderItem(99, item)     #Making a vertical header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(0, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(1, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(2, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(3, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(4, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(5, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(6, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(7, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(8, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(9, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(10, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(11, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(12, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(13, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(14, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(15, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(16, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(17, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(18, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(19, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        self.searchTable.setHorizontalHeaderItem(20, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        font = QtGui.QFont()        #Setting a specific font for the header
        font.setPointSize(7)        #Setting a specific size for the font
        item.setFont(font)          #Giving its font information to the item
        self.searchTable.setHorizontalHeaderItem(21, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()         #Making an item value using functions from QtGui
        font = QtGui.QFont()        #Setting a specific font for the header
        font.setPointSize(7)        #Setting a specific size for the font
        item.setFont(font)          #Giving its font information to the item
        self.searchTable.setHorizontalHeaderItem(22, item)     #Making a horizontal header for a table in the window
        item = QtGui.QTableWidgetItem()
        self.searchTitle = QtGui.QLabel(self.centralwidget)     #Setting an item that represents the title of the window
        self.searchTitle.setGeometry(QtCore.QRect(10, 10, 461, 51))     #Setting the location of the item in the window
        font = QtGui.QFont()        #Setting a specific font for the header
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(36)        #Setting a specific size for the font
        font.setItalic(False)        #Not an italic font
        font.setUnderline(False)        #Not underlined
        self.searchTitle.setFont(font)          #Giving its font information to the item
        self.searchTitle.setObjectName(_fromUtf8("searchTitle"))
        self.searchText = QtGui.QPlainTextEdit(self.centralwidget)
        self.searchText.setGeometry(QtCore.QRect(90, 70, 311, 31))     #Setting the location of the item in the window
        self.searchText.setObjectName(_fromUtf8("searchText"))
        self.searchLabel = QtGui.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(20, 70, 61, 31))     #Setting the location of the item in the window
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchLabel.setFont(font)
        self.searchLabel.setObjectName(_fromUtf8("searchLabel"))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(410, 70, 91, 31))     #Setting the location of the item in the window
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(730, 0, 50, 64))     #Setting the location of the item in the window
        self.dial.setObjectName(_fromUtf8("dial"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))     #Setting the location of the item in the window
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):        #This function further modifies/transforms the graphic user interface

        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Sales Centre - Search Window", None))
        self.searchTable.setSortingEnabled(True)        #Allowed sorting function for the table in the window
        item = self.searchTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "19", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "20", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "21", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "22", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "23", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "24", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "25", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "26", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "27", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "28", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "29", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(29)
        item.setText(_translate("MainWindow", "30", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(30)
        item.setText(_translate("MainWindow", "31", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(31)
        item.setText(_translate("MainWindow", "32", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(32)
        item.setText(_translate("MainWindow", "33", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(33)
        item.setText(_translate("MainWindow", "34", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(34)
        item.setText(_translate("MainWindow", "35", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(35)
        item.setText(_translate("MainWindow", "36", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(36)
        item.setText(_translate("MainWindow", "37", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(37)
        item.setText(_translate("MainWindow", "38", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(38)
        item.setText(_translate("MainWindow", "39", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(39)
        item.setText(_translate("MainWindow", "40", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(40)
        item.setText(_translate("MainWindow", "41", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(41)
        item.setText(_translate("MainWindow", "42", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(42)
        item.setText(_translate("MainWindow", "43", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(43)
        item.setText(_translate("MainWindow", "44", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(44)
        item.setText(_translate("MainWindow", "45", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(45)
        item.setText(_translate("MainWindow", "46", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(46)
        item.setText(_translate("MainWindow", "47", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(47)
        item.setText(_translate("MainWindow", "48", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(48)
        item.setText(_translate("MainWindow", "49", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(49)
        item.setText(_translate("MainWindow", "50", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(50)
        item.setText(_translate("MainWindow", "51", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(51)
        item.setText(_translate("MainWindow", "52", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(52)
        item.setText(_translate("MainWindow", "53", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(53)
        item.setText(_translate("MainWindow", "54", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(54)
        item.setText(_translate("MainWindow", "55", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(55)
        item.setText(_translate("MainWindow", "56", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(56)
        item.setText(_translate("MainWindow", "57", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(57)
        item.setText(_translate("MainWindow", "58", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(58)
        item.setText(_translate("MainWindow", "59", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(59)
        item.setText(_translate("MainWindow", "60", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(60)
        item.setText(_translate("MainWindow", "61", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(61)
        item.setText(_translate("MainWindow", "62", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(62)
        item.setText(_translate("MainWindow", "63", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(63)
        item.setText(_translate("MainWindow", "64", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(64)
        item.setText(_translate("MainWindow", "65", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(65)
        item.setText(_translate("MainWindow", "66", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(66)
        item.setText(_translate("MainWindow", "67", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(67)
        item.setText(_translate("MainWindow", "68", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(68)
        item.setText(_translate("MainWindow", "69", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(69)
        item.setText(_translate("MainWindow", "70", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(70)
        item.setText(_translate("MainWindow", "71", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(71)
        item.setText(_translate("MainWindow", "72", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(72)
        item.setText(_translate("MainWindow", "73", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(73)
        item.setText(_translate("MainWindow", "74", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(74)
        item.setText(_translate("MainWindow", "75", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(75)
        item.setText(_translate("MainWindow", "76", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(76)
        item.setText(_translate("MainWindow", "77", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(77)
        item.setText(_translate("MainWindow", "78", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(78)
        item.setText(_translate("MainWindow", "79", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(79)
        item.setText(_translate("MainWindow", "80", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(80)
        item.setText(_translate("MainWindow", "81", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(81)
        item.setText(_translate("MainWindow", "82", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(82)
        item.setText(_translate("MainWindow", "83", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(83)
        item.setText(_translate("MainWindow", "84", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(84)
        item.setText(_translate("MainWindow", "85", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(85)
        item.setText(_translate("MainWindow", "86", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(86)
        item.setText(_translate("MainWindow", "87", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(87)
        item.setText(_translate("MainWindow", "88", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(88)
        item.setText(_translate("MainWindow", "89", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(89)
        item.setText(_translate("MainWindow", "90", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(90)
        item.setText(_translate("MainWindow", "91", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(91)
        item.setText(_translate("MainWindow", "92", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(92)
        item.setText(_translate("MainWindow", "93", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(93)
        item.setText(_translate("MainWindow", "94", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(94)
        item.setText(_translate("MainWindow", "95", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(95)
        item.setText(_translate("MainWindow", "96", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(96)
        item.setText(_translate("MainWindow", "97", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(97)
        item.setText(_translate("MainWindow", "98", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(98)
        item.setText(_translate("MainWindow", "99", None))       #Setting specific name for this vertical header
        item = self.searchTable.verticalHeaderItem(99)
        item.setText(_translate("MainWindow", "100", None))       #Setting specific name for this vertical header
        item = self.searchTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Job Title", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Employee ID", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Department", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "First Name", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Last Name", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Gender", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Birth Date", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Sin #", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Salary Or Rate", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Marital Status", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Home Phone #", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Work Phone #", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Address", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Manager Name", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Education Level", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Work Start Date", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Email", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "EM First Name", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "EM Last Name", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "EM Relationship", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "EM Number", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "# of Sick Days Taken", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "# of Vaca.Days Taken", None))       #Setting specific name for this horizontal header
        item = self.searchTable.horizontalHeaderItem(23)


        self.searchTitle.setText(_translate("MainWindow", "Simple Sales Centre", None))         #Setting specific name for the title of the window
        self.searchLabel.setText(_translate("MainWindow", "SEARCH:", None))         #Setting specific name for a label of the window
        self.searchButton.setText(_translate("MainWindow", "Enter", None))         #Setting specific name for a button in the window
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ButtonClickedSearch)         #It performs function 'ButtonClickedSearch' when 'searchButton' is clicked

        for x in range(len(employeeList)):         #For the x values in range of the length of a list employeeList
            self.searchTable
            self.searchTable.setItem(x, 0, QtGui.QTableWidgetItem(str(employeeList[x].GetJobTitle())))          #It sets the value at this box with the value of job position of the employee from the employeeList
            self.searchTable.setItem(x, 1, QtGui.QTableWidgetItem(str(employeeList[x].GetEmployeeID())))          #It sets the value at this box with the value of employee ID of the employee from the employeeList
            self.searchTable.setItem(x, 2, QtGui.QTableWidgetItem(str(employeeList[x].GetDepartment())))          #It sets the value at this box with the value of department  of the employee from the employeeList
            self.searchTable.setItem(x, 3, QtGui.QTableWidgetItem(str(employeeList[x].GetFirstName())))          #It sets the value at this box with the value of first name of the employee from the employeeList
            self.searchTable.setItem(x, 4, QtGui.QTableWidgetItem(str(employeeList[x].GetLastName())))          #It sets the value at this box with the value of last name  of the employee from the employeeList
            self.searchTable.setItem(x, 5, QtGui.QTableWidgetItem(str(employeeList[x].GetGender())))          #It sets the value at this box with the value of gender of the employee from the employeeList
            self.searchTable.setItem(x, 6, QtGui.QTableWidgetItem(str(employeeList[x].GetBirthDate())))          #It sets the value at this box with the value of birth date of the employee from the employeeList
            self.searchTable.setItem(x, 7, QtGui.QTableWidgetItem(str(employeeList[x].GetSINNumber())))          #It sets the value at this box with the value of sin number of the employee from the employeeList
            self.searchTable.setItem(x, 8, QtGui.QTableWidgetItem(str(employeeList[x].GetPaytype())))          #It sets the value at this box with the value of pay type of the employee from the employeeList
            self.searchTable.setItem(x, 9, QtGui.QTableWidgetItem(str(employeeList[x].GetMaritalStatus())))          #It sets the value at this box with the value of marital status of the employee from the employeeList
            self.searchTable.setItem(x, 10, QtGui.QTableWidgetItem(str(employeeList[x].GetHomePhone())))          #It sets the value at this box with the value of home phone of the employee from the employeeList
            self.searchTable.setItem(x, 11, QtGui.QTableWidgetItem(str(employeeList[x].GetWorkPhone())))          #It sets the value at this box with the value of work phone of the employee from the employeeList
            self.searchTable.setItem(x, 12, QtGui.QTableWidgetItem(str(employeeList[x].GetAddress())))          #It sets the value at this box with the value of address of the employee from the employeeList
            self.searchTable.setItem(x, 13, QtGui.QTableWidgetItem(str(employeeList[x].GetManagerName())))          #It sets the value at this box with the value of manager name of the employee from the employeeList
            self.searchTable.setItem(x, 14, QtGui.QTableWidgetItem(str(employeeList[x].GetEducation())))          #It sets the value at this box with the value of education level of the employee from the employeeList
            self.searchTable.setItem(x, 15, QtGui.QTableWidgetItem(str(employeeList[x].GetStartDate())))          #It sets the value at this box with the value of work start date of the employee from the employeeList
            self.searchTable.setItem(x, 16, QtGui.QTableWidgetItem(str(employeeList[x].GetEmail())))          #It sets the value at this box with the value of email of the employee from the employeeList
            self.searchTable.setItem(x, 17, QtGui.QTableWidgetItem(str(employeeList[x].GetEmergencyFirstName())))          #It sets the value at this box with the value of emergency contact first name of the employee from the employeeList
            self.searchTable.setItem(x, 18, QtGui.QTableWidgetItem(str(employeeList[x].GetEmergencyLastName())))          #It sets the value at this box with the value of emergency contact last name of the employee from the employeeList
            self.searchTable.setItem(x, 19, QtGui.QTableWidgetItem(str(employeeList[x].GetEmergencyRelationship())))          #It sets the value at this box with the value of emergency contact relationship of the employee from the employeeList
            self.searchTable.setItem(x, 20, QtGui.QTableWidgetItem(str(employeeList[x].GetEmergencyPhoneNumber())))          #It sets the value at this box with the value of emergency contact phone number of the employee from the employeeList
            self.searchTable.setItem(x, 21, QtGui.QTableWidgetItem(str(employeeList[x].GetNumSickDaysTaken())))          #It sets the value at this box with the value of number of sicks days available of the employee from the employeeList
            self.searchTable.setItem(x, 22, QtGui.QTableWidgetItem(str(employeeList[x].GetNumVacationDaysTaken())))          #It sets the value at this box with the value of number of vacation days available  of the employee from the employeeList


    def ButtonClickedSearch(self):
        for x in range(100):
            if x<=(len(search(self.searchText.toPlainText()))-1):

                self.searchTable.setItem(x, 0, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetJobTitle())))          #It sets the value at this box with the value of job position of the employee from the searched/modified List
                self.searchTable.setItem(x, 1, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetEmployeeID())))          #It sets the value at this box with the value of employee ID of the employee from the searched/modified List
                self.searchTable.setItem(x, 2, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetDepartment())))          #It sets the value at this box with the value of department  of the employee from the searched/modified List
                self.searchTable.setItem(x, 3, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetFirstName())))          #It sets the value at this box with the value of first name of the employee from the searched/modified List
                self.searchTable.setItem(x, 4, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetLastName())))          #It sets the value at this box with the value of last name  of the employee from the searched/modified List
                self.searchTable.setItem(x, 5, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetGender())))          #It sets the value at this box with the value of gender of the employee from the searched/modified List
                self.searchTable.setItem(x, 6, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetBirthDate())))          #It sets the value at this box with the value of birth date of the employee from the searched/modified List
                self.searchTable.setItem(x, 7, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetSINNumber())))          #It sets the value at this box with the value of sin number of the employee from the searched/modified List
                self.searchTable.setItem(x, 8, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetPaytype())))          #It sets the value at this box with the value of pay type of the employee from the searched/modified List
                self.searchTable.setItem(x, 9, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetMaritalStatus())))          #It sets the value at this box with the value of marital status of the employee from the searched/modified List
                self.searchTable.setItem(x, 10, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetHomePhone())))          #It sets the value at this box with the value of home phone of the employee from the searched/modified List
                self.searchTable.setItem(x, 11, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetWorkPhone())))          #It sets the value at this box with the value of work phone of the employee from the searched/modified List
                self.searchTable.setItem(x, 12, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetAddress())))          #It sets the value at this box with the value of address of the employee from the searched/modified List
                self.searchTable.setItem(x, 13, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetManagerName())))          #It sets the value at this box with the value of manager name of the employee from the searched/modified List
                self.searchTable.setItem(x, 14, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetEducation())))          #It sets the value at this box with the value of education level of the employee from the searched/modified List
                self.searchTable.setItem(x, 15, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetStartDate())))          #It sets the value at this box with the value of work start date of the employee from the searched/modified List
                self.searchTable.setItem(x, 16, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetEmail())))          #It sets the value at this box with the value of email of the employee from the searched/modified List
                self.searchTable.setItem(x, 17, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetEmergencyFirstName())))          #It sets the value at this box with the value of emergency contact first name of the employee from the searched/modified List
                self.searchTable.setItem(x, 18, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetEmergencyLastName())))          #It sets the value at this box with the value of emergency contact last name of the employee from the searched/modified List
                self.searchTable.setItem(x, 19, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetEmergencyRelationship())))          #It sets the value at this box with the value of emergency contact relationship of the employee from the searched/modified List
                self.searchTable.setItem(x, 20, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetEmergencyPhoneNumber())))          #It sets the value at this box with the value of emergency contact phone number of the employee from the searched/modified List
                self.searchTable.setItem(x, 21, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetNumSickDaysTaken())))          #It sets the value at this box with the value of number of sicks days available of the employee from the searched/modified List
                self.searchTable.setItem(x, 22, QtGui.QTableWidgetItem(str(employeeList[search(self.searchText.toPlainText())[x]].GetNumVacationDaysTaken())))          #It sets the value at this box with the value of number of vacation days available  of the employee from the searched/modified List

            else:       #if it does not apply to the above condition
                for y in range(23):     #for range 0 ~ 22
                    self.searchTable.setItem(x, y, QtGui.QTableWidgetItem("-"))         #Puts in '-' for boxes
        self.searchText.setPlainText("")
if __name__=="__main__":        #if it is main
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QMainWindow()     #Frame gets functions/attributes from the QtGui
    ui = Ui_SearchWindow()      #Connects the interface with the 'Ui_SearchWindow'
    ui.setupUi(Frame)       #Sets up the user interface according to the frame
    Frame.show()        #Shows the graphic user interface
    sys.exit(app.exec_())