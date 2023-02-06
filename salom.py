# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
# from PyQt5.QtGui import QFont
# import sys,random
# app=QApplication(sys.argv)
# ls=[1,2,3,1,2,3]
# class Window(QWidget):
#     def init(self):
#         super().init()

#         self.setGeometry(250,250,500,600)
#         self.start()
#         self.show()
#     def font(self,obj,x,y):
#         obj.setFont(QFont("Times",24))
#         obj.setGeometry(x,y,80,80)
#     def start(self):
#         self.a1=QPushButton("",self)
#         self.font(self.a1,50,50)
#         self.a1.clicked.connect(self.A1)
#         self.a2=QPushButton("",self)
#         self.font(self.a2,150,50)
#         self.a2.clicked.connect(self.A2)
#         self.a3=QPushButton("",self)
#         self.font(self.a3,250,50)
#         self.a3.clicked.connect(self.A3)
#         self.a4=QPushButton("",self)
#         self.font(self.a4,50,150)
#         self.a4.clicked.connect(self.A4)
#         self.a5=QPushButton("",self)
#         self.font(self.a5,150,150)
#         self.a5.clicked.connect(self.A5)
#         self.a6=QPushButton("",self)
#         self.font(self.a6,250,150)
#         self.a6.clicked.connect(self.A6)
#     def check(self):
#         if self.a1.text()!="" and self.a2.text()!="" and self.a1.text()==self.a2.text():
#             self.a1.hide()
#             self.a2.hide()
#             self.a3.setText("")
#             self.a4.setText("")
#             self.a5.setText("")
#             self.a6.setText("")
#             ls.remove(int(self.a1.text()))
#             ls.remove(int(self.a2.text()))
#         elif self.a1.text()!="" and self.a2.text()!="":
#             self.a1.setText("")
#             self.a2.setText("")
#             self.a3.setText("")
#             self.a4.setText("")
#             self.a5.setText("")
#             self.a6.setText("")
#     def A1(self):
#         if self.a1.text()=="":
#             a=random.choice(ls)
#             self.a1.setText(str(a))
#         self.check()
#     def A2(self):
#         if self.a2.text()=="":
#             a=random.choice(ls)
#             self.a2.setText(str(a))
#         self.check()
#     def A3(self):
#         if self.a3.text()=="":
#             a=random.choice(ls)
#             self.a3.setText(str(a))
#         self.check()
#     def A4(self):
#         if self.a4.text()=="":
#             a=random.choice(ls)
#             self.a4.setText(str(a))
#         self.check()
#     def A5(self):
#         if self.a5.text()=="":
#             a=random.choice(ls)
#             self.a5.setText(str(a))
#         self.check()
#     def A6(self):
#         if self.a6.text()=="":
#             a=random.choice(ls)
#             self.a6.setText(str(a))
#         self.check()
# win=Window()
# app.exec_()
#########################################################################
###############################################################################
#1) 2ta QLabel va 2ta QLineEdit va 2ta QPushButton e'lon qiling.
# 1-Qlabel va 1-QLineEdit Login uchun
# 2-Qlabel va 2-QLineEdit Parol uchun
# 1-QPushButton SignIn uchun ya'ni foydalanuvchini sistemaga kiritadi va "Siz 
# tizimga kirdingiz" MessageBox orqali qilinishi kerak
# 2-QPushButton esa SignUp uchun ya'ni sizda faylda kamida 10ta Login va parol 
# yozilgan ro'yhatni ichida mavjud bo'lmasa ushbu login va parolni fayl ro'yhatiga 
# qo'shib qo'ysin.

from PyQt5.QtWidgets import QWidget, QApplication,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChekBox")
        self.setGeometry(340,100,700,900)
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",25))
        ob.move(x,y)
    def plus(self):
        a = int(self.q.text())
        b = int(self.qx.text())
        x=a + b
        self.lable.setText(str(x))
    def minus(self):
        a = int(self.q.text())
        b = int(self.qx.text())
        x=a - b
        self.lable.setText(str(x))
   
    def bolinma(self):
        a = int(self.q.text())
        b = int(self.qx.text())
        x=a / b
        self.lable.setText(str(x))
    def qoldiqli_bulish(self):
        a = int(self.q.text())
        b = int(self.qx.text())
        x=a % b
        self.lable.setText(str(x))
    def degree(self):
        a = int(self.q.text())
        b = int(self.qx.text())
        x=a ** b
        self.lable.setText(str(x))
         def kopaytma(self):
        a = int(self.q.text())
        b = int(self.qx.text())
        x=a * b
        self.lable.setText(str(x))
    def start(self):
        self.lable1 = QLabel("ISM : ",self)
        self.font(self.lable1,20,20)
        self.lable2 = QLabel("FAMILIYA : ",self)
        self.font(self.lable2,70,20)
        self.q = QLineEdit(self)
        self.font(self.q,20,100)
        self.qx = QLineEdit(self)
        self.font(self.qx,20,200)
        self.p = QPushButton(" + ",self)
        self.font(self.p,50,400)
        self.p.clicked.connect(self.plus)
        self.g = QPushButton(" - ",self)
        self.font(self.g,150,400)
        self.g.clicked.connect(self.minus)
        self.t = QPushButton(" * ",self)
        self.font(self.t,250,400)
        self.t.clicked.connect(self.kopaytma)
        self.p = QPushButton(" / ",self)
        self.font(self.p,350,400)
        self.p.clicked.connect(self.bolinma)
        self.g = QPushButton(" % ",self)
        self.font(self.g,450,400)
        self.g.clicked.connect(self.qoldiqli_bulish)
        self.t = QPushButton(" ** ",self)
        self.font(self.t,550,400)
        self.t.clicked.connect(self.degree)

app = QApplication(sys.argv)     
oyna = window()
oyna.show()
sys.exit(app.exec_())
