from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from CalculatorUI import *
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        self.__product = 0
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Calculator')
        self.Output.setReadOnly(True)
        self.pbEq.clicked.connect(lambda: self.Equal())
        self.pbAdd.clicked.connect(lambda: self.Add())
        self.pbSub.clicked.connect(lambda: self.Subtract())
        self.pbMult.clicked.connect(lambda: self.Multiply())
        self.pbDiv.clicked.connect(lambda: self.Divide())
        self.pbBack.clicked.connect(lambda: self.BackSpace())
        self.pbClear.clicked.connect(lambda: self.Clear())
        self.pbClearE.clicked.connect(lambda: self.ClearEntry())
        self.pbPerc.clicked.connect(lambda: self.Percent())
        self.pb1Over.clicked.connect(lambda: self.Denominator())
        self.pbSqr.clicked.connect(lambda: self.Square())
        self.pbRoot.clicked.connect(lambda: self.SquareRoot())
        self.pb0.clicked.connect(lambda: self.Zero())
        self.pb1.clicked.connect(lambda: self.One())
        self.pb2.clicked.connect(lambda: self.Two())
        self.pb3.clicked.connect(lambda: self.Three())
        self.pb4.clicked.connect(lambda: self.Four())
        self.pb5.clicked.connect(lambda: self.Five())
        self.pb6.clicked.connect(lambda: self.Six())
        self.pb7.clicked.connect(lambda: self.Seven())
        self.pb8.clicked.connect(lambda: self.Eight())
        self.pb9.clicked.connect(lambda: self.Nine())
        self.pbDec.clicked.connect(lambda: self.Decimal())
        self.pbPosNeg.clicked.connect(lambda: self.PosNeg())

    def Equal(self):
        this = self.Output.text()
        self.Output.clear()
        if this[-1] == '+' or this[-1] == '-' or this[-1] == '*' or this[-1] == '/':
            this = this[:-1]
        try:   #TRY EXCEPT THIS IT WILL BREAK THINGS
            self.__product = eval(this)
            self.Output.setText(str(self.__product))
        except ZeroDivisionError:
            self.Output.clear()
            self.Output.setText("Cannot divide by zero!")
            self.Lock()
        except Exception as e:
            self.Output.setText("Error")
            print(e)

    def Add(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            pass
        else:
            self.Output.setText(f'{current}+')

    def Subtract(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            pass
        else:
            self.Output.setText(f'{current}-')

    def Multiply(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            pass
        else:
            self.Output.setText(f'{current}*')

    def Divide(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            pass
        else:
            self.Output.setText(f'{current}/')

    def BackSpace(self):
        current = self.Output.text()
        self.Output.setText(f'{current[:-1]}')

    def Clear(self):
        current = self.Output.text()
        self.__product = 0
        self.Output.clear()
        self.Unlock()

    def ClearEntry(self):
        current = self.Output.text()
        op = -1
        for i in range(len(current)):
            if current[i] == '+' or current[i] == '-' or current[i] == '*' or current[i] == '/':
                op = i
        self.Output.setText(f'{current[:op+1]}')

    def Percent(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            current = current[:-1]
        self.__product = eval(current)
        self.__product = self.__product / 100
        self.Output.setText(str(self.__product))

    def Denominator(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            current = current[:-1]
        try:
            self.__product = eval(current)
            self.__product = 1/self.__product
            self.Output.clear()
            self.Output.setText(str(self.__product))
        except ZeroDivisionError:
            self.Output.clear()
            self.Output.setText("Cannot divide by zero!")
            self.Lock()

    def Square(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            current = current[:-1]
        self.__product = eval(current)
        self.__product = math.pow(self.__product, 2)
        self.Output.clear()
        self.Output.setText(str(self.__product))

    def SquareRoot(self):
        current = self.Output.text()
        if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
            current = current[:-1]
        try:
            self.__product = eval(current)
            self.__product = math.sqrt(self.__product)
            self.Output.setText(str(self.__product))
        except ValueError:
            self.Output.clear()
            self.Output.setText("Math domain error!")
            self.Lock()

    def Zero(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}0')
        else:
            self.Output.setText(f'0')

    def One(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}1')
        else:
            self.Output.setText(f'1')

    def Two(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}2')
        else:
            self.Output.setText(f'2')

    def Three(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}3')
        else:
            self.Output.setText(f'3')

    def Four(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}4')
        else:
            self.Output.setText(f'4')

    def Five(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}5')
        else:
            self.Output.setText(f'5')

    def Six(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}6')
        else:
            self.Output.setText(f'6')

    def Seven(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}7')
        else:
            self.Output.setText(f'7')

    def Eight(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}8')
        else:
            self.Output.setText(f'8')

    def Nine(self):
        current = self.Output.text()
        if current != '0':
            self.Output.setText(f'{current}9')
        else:
            self.Output.setText(f'9')
    
    def Decimal(self):
        current = self.Output.text()
        if '.' in current:
            pass
        else:
            self.Output.setText(f'{current}.')
    
    def PosNeg(self):
        current = self.Output.text()
        if len(current) > 0:
            if current[0] == "-":
                self.Output.setText(current[1:])
            else:
                new = f'-{current}'
                self.Output.setText(new)
        else:
            self.Output.setText('-')
    
    def Lock(self):
        self.pb0.setEnabled(False)
        self.pb1.setEnabled(False)
        self.pb2.setEnabled(False)
        self.pb3.setEnabled(False)
        self.pb4.setEnabled(False)
        self.pb5.setEnabled(False)
        self.pb6.setEnabled(False)
        self.pb7.setEnabled(False)
        self.pb8.setEnabled(False)
        self.pb9.setEnabled(False)
        self.pbAdd.setEnabled(False)
        self.pbSub.setEnabled(False)
        self.pbMult.setEnabled(False)
        self.pbDiv.setEnabled(False)
        self.pbEq.setEnabled(False)
        self.pb1Over.setEnabled(False)
        self.pbPerc.setEnabled(False)
        self.pbPosNeg.setEnabled(False)
        self.pbRoot.setEnabled(False)
        self.pbSqr.setEnabled(False)
        self.pbSub.setEnabled(False)
        self.pbDec.setEnabled(False)
        self.pbBack.setEnabled(False)
        
    def Unlock(self):
        self.pb0.setEnabled(True)
        self.pb1.setEnabled(True)
        self.pb2.setEnabled(True)
        self.pb3.setEnabled(True)
        self.pb4.setEnabled(True)
        self.pb5.setEnabled(True)
        self.pb6.setEnabled(True)
        self.pb7.setEnabled(True)
        self.pb8.setEnabled(True)
        self.pb9.setEnabled(True)
        self.pbAdd.setEnabled(True)
        self.pbSub.setEnabled(True)
        self.pbMult.setEnabled(True)
        self.pbDiv.setEnabled(True)
        self.pbEq.setEnabled(True)
        self.pb1Over.setEnabled(True)
        self.pbPerc.setEnabled(True)
        self.pbPosNeg.setEnabled(True)
        self.pbRoot.setEnabled(True)
        self.pbSqr.setEnabled(True)
        self.pbSub.setEnabled(True)
        self.pbDec.setEnabled(True)
        self.pbBack.setEnabled(True)        
    
