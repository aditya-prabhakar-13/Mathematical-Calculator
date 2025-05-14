from ast import Lambda
import tkinter
import mysql.connector
from tkinter import *
from tkinter import ttk
import math
db=mysql.connector.connect(host="127.0.0.1",user="root",password="burningbeast@1972")
if db.is_connected():
    print("Server Connected")
curs=db.cursor()
#curs.execute("create database csproject")
curs.execute("use csproject")
#curs.execute("create table calhistory(input varchar(50), output varchar(50))")
def tabinput(inpf,outf):
    global curs
    global db
    sqlcmd="insert into calhistory(input,output)values(%s,%s)"
    valcmd=(inpf,outf)
    curs.execute(sqlcmd,valcmd)
    db.commit()


#CALCULUS

def log(base,exp):
    n3=math.log(base,exp)
    return n3




#CODE


window=tkinter.Tk()
xp=400
yp=200
algebratitle=PhotoImage(file='algebratitle.png')
calculustitle=PhotoImage(file='calculustitle.png')
logbase10=PhotoImage(file="logbase10.png")
logtitle=PhotoImage(file="log.png")
lntitile=PhotoImage(file="ln.png")
def HomeChangeClick():
    global L1, B1, B2
    L1.after(10, L1.destroy())
    B1.after(10, B1.destroy())
    B2.after(10, B2.destroy())
    #B3.after(10, B3.destroy())
def Check_History():
    global curs
    
    history=curs.fetchall()
    return history

def Algebra_Screen():
    global LA1,EA1,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAplus,BAminus,BAmultiply,BAdivide,BAreturn,BAclear,BAdot
    HomeChangeClick()
    global expression
    expression=''
    def numadd(numb):
        global expression

        expression=expression + str(numb)

        equation.set(expression)
    
    def numequal():
        try:
            global expression
            total= str(eval(expression))
            valcmd=(EA1.get(),total)
            equation.set(total)
            sqlcmd="insert into calhistory(input,output)values(%s,%s)"
            curs.execute(sqlcmd,valcmd)
            db.commit()
            expression ="" 
        except:
            equation.set("ERROR")
            expression = ""

    def clear():
        global expression
        expression=''
        equation.set("")

    equation=StringVar()
    
    def homereturnalgebra():
        global LA1,EA1,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAplus,BAminus,BAmultiply,BAdivide,BAreturn,BAclear,ListAlgebra,BAdot
        ListAlgebra=[LA1,EA1,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAplus,BAminus,BAmultiply,BAdivide,BAreturn,BAclear,BAdot]
        for i in ListAlgebra:
            i.after(2,i.destroy())
        Homescreen()

    LA1=Label(window, image=algebratitle, relief='groove')
    LA1.place(x=345,y=75)
    EA1=Entry(window, bg="#14ebeb", fg="#df0a0a", width =20,borderwidth='3',relief='groove', font=("Times New Roman", 80), textvariable=equation )
    EA1.place(x= 250, y=320)
    BA1=Button(window, text="1",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(1))
    BA1.place(x=250, y=450)
    BA2=Button(window, text="2",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(2))
    BA2.place(x=455, y=450)
    BA3=Button(window, text="3",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(3))
    BA3.place(x=660,y=450)
    BA4=Button(window, text="4",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(4))
    BA4.place(x=250,y=550)
    BA5=Button(window, text="5",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(5))
    BA5.place(x=455,y=550) 
    BA6=Button(window, text="6",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(6))
    BA6.place(x=660,y=550)
    BA7=Button(window, text="7",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(7))
    BA7.place(x=250, y=650)
    BA8=Button(window, text="8",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(8))
    BA8.place(x=455, y=650)
    BA9=Button(window, text="9",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(9))
    BA9.place(x=660, y=650)
    BA0=Button(window, text="0",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd(0))
    BA0.place(x=250, y=750)  
    BAequal=Button(window, text="=",bg="blue",width="15",height="3", fg="white", relief="raised",font=("Times New Roman",18), command=numequal)
    BAequal.place(x=660, y=750)
    BAplus=Button(window, text="+",bg="#11ca74",width="18",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numadd('+'))
    BAplus.place(x=865, y=450)
    BAminus=Button(window, text="-",bg="#11ca74",width="17",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numadd('-'))
    BAminus.place(x=1109,y=450)
    BAmultiply=Button(window, text="*",bg="#11ca74",width="18",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numadd('*'))
    BAmultiply.place(x=865, y=550)
    BAdivide=Button(window, text="/",bg="#11ca74",width="17",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numadd('/'))
    BAdivide.place(x=1109, y=550)
    BAclear=Button(window, text="CLEAR",bg='black',width="35",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=clear)
    BAclear.place(x=865, y=650)
    BAreturn=Button(window, text="RETURN",bg='white',width="35",height="3", fg='black',relief='raised',font=("Times New Roman",18),command=homereturnalgebra)
    BAreturn.place(x=865, y=750)
    BAdot=Button(window, text=".",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numadd('.'))
    BAdot.place(x=455, y=750)
#CALCULUS    
def Calculus_Screen():
    global LC1,Blog10,Blog,Bln,Bgif,Bff,Breturn,ListCalculusinside
    HomeChangeClick()
    global equationcalculus,LC1,Blog10,Blog,Bln,Bgif,Bff,ListCalculusinside
    def Calculusinsideclean():
        global LC1,Blog10,Blog,Bln,ListCalculusinside,Breturn #Bgif,Bff,
        ListCalculusinside=[LC1,Blog10,Blog,Bln,Breturn]
        for i in ListCalculusinside:
            i.after(1,i.destroy())
    def Calculusreturn():
        Calculusinsideclean()
        Homescreen()
    def LogBase():
        global expressionlog, expressionlogbase,Llog,Lanslog,Lanslogonly,Elog,Elogbase,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,BA1B,BA2B,BA3B,BA4B,BA5B,BA6B,BA7B,BA8B,BA9B,BA0B,BAclearB,Calculuslogclean,BAdot,BAdotB
        Calculusinsideclean()
        expressionlog=" "
        expressionlogbase= " "
        def numaddlog(numb):
            global expressionlog
            expressionlog=expressionlog + str(numb)
            equationlog.set(expressionlog)
        equationlog=StringVar()
        equationanslog=StringVar()
        def numaddlogbase(numb):
            global expressionlogbase
            expressionlogbase = expressionlogbase + str(numb)
            equationlogbase.set(expressionlogbase)
        equationlogbase=StringVar()
        def clearlog():
            global expressionlog
            expressionlog=""
            equationanslog.set('')
            equationlog.set('')
        def clearlogbase():
            global expressionlogbase
            expressionlogbase = ""
            equationanslog.set('')
            equationlogbase.set('')
        
        def numequallog():
            try:
                global expressionlog, expressionlogbase
                total= str(log(float(expressionlog),float(expressionlogbase)))
                valcmdlog=[Elog.get(),  Elogbase.get()]
                valcmdexp='Exponent = '+ str(valcmdlog[0])
                valcmdbase="Base = " + str(valcmdlog[1])
                valcmdstr=valcmdexp+valcmdbase
                valcmd=(valcmdstr,total)
                equationanslog.set(total)
                sqlcmd="insert into calhistory(input,output)values(%s,%s)"
                curs.execute(sqlcmd,valcmd)
                db.commit()
                expressionlog =""
                expressionlogbase = ""
            except:
                equationanslog.set("ERROR")
                expressionlogbase = ""
                expressionlog='' 

        def calculusreturnlog():
            global Llog,Lanslog,Lanslogonly,Elog,Elogbase,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,BA1B,BA2B,BA3B,BA4B,BA5B,BA6B,BA7B,BA8B,BA9B,BA0B,BAclearB,Calculuslogclean,BAdotB,BAdot
            Calculuslogclean=[Llog,Lanslog,Lanslogonly,Elog,Elogbase,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,BA1B,BA2B,BA3B,BA4B,BA5B,BA6B,BA7B,BA8B,BA9B,BA0B,BAclearB,BAdot,BAdotB]
            for i in Calculuslogclean:
                i.after(10,i.destroy())
            Calculus_Screen()

        Llog=Label(window, image=logtitle)
        Llog.place(x=145, y=125)
        Lanslog=Label(window, text="Answer =",textvariable=equationanslog, width=35, height=5, font=("Times New Roman",26), bg="#0df0ea", fg="#c9210d", bd=3, relief="sunken")
        Lanslog.place(x=344, y=230)
        Lanslogonly=Label(window, text="Answer =", width=10, height=5, font=("Times New Roman",26), bg="#0df0ea", fg="#c9210d", bd=3, relief="sunken")
        Lanslogonly.place(x=145,y=230)
        Elog=Entry(window, bg="#14ebeb", fg="#df0a0a", width =12,borderwidth='3',relief='groove', font=("Times New Roman", 40), textvariable=equationlog)
        Elog.place(x=350, y=110)
        Elogbase=Entry(window, bg="#14ebeb", fg="#df0a0a", width =12,borderwidth='3',relief='groove', font=("Times New Roman", 20), textvariable=equationlogbase)
        Elogbase.place(x=310,y=180)
        BA1=Button(window, text="1",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(1))
        BA1.place(x=50, y=450)
        BA2=Button(window, text="2",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(2))
        BA2.place(x=255, y=450)
        BA3=Button(window, text="3",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(3))
        BA3.place(x=460,y=450)
        BA4=Button(window, text="4",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(4))
        BA4.place(x=50,y=550)
        BA5=Button(window, text="5",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(5))
        BA5.place(x=255,y=550) 
        BA6=Button(window, text="6",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(6))
        BA6.place(x=460,y=550)
        BA7=Button(window, text="7",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(7))
        BA7.place(x=50, y=650)
        BA8=Button(window, text="8",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(8))
        BA8.place(x=255, y=650)
        BA9=Button(window, text="9",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(9))
        BA9.place(x=460, y=650)
        BA0=Button(window, text="0",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog(0))
        BA0.place(x=50, y=750)
        BAequal=Button(window, text="=",bg="blue",width="35",height="3", fg="white", relief="raised",font=("Times New Roman",18), command=numequallog)
        BAequal.place(x=1100, y=50)
        BAclear=Button(window, text="CLEAR\nEXPONENT",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=clearlog)
        BAclear.place(x=460, y=750)
        BAreturn=Button(window, text="RETURN",bg='#5f6161',width="35",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=calculusreturnlog)
        BAreturn.place(x=1100, y=175)
        BAdot=Button(window, text=".",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog('.'))
        BAdot.place(x=255, y=750)


        BA1B=Button(window, text="1",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(1))
        BA1B.place(x=860, y=450)
        BA2B=Button(window, text="2",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(2))
        BA2B.place(x=1065, y=450)
        BA3B=Button(window, text="3",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(3))
        BA3B.place(x=1270,y=450)
        BA4B=Button(window, text="4",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(4))
        BA4B.place(x=860,y=550)
        BA5B=Button(window, text="5",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(5))
        BA5B.place(x=1065,y=550) 
        BA6B=Button(window, text="6",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(6))
        BA6B.place(x=1270,y=550)
        BA7B=Button(window, text="7",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(7))
        BA7B.place(x=860, y=650)
        BA8B=Button(window, text="8",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(8))
        BA8B.place(x=1065, y=650)
        BA9B=Button(window, text="9",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(9))
        BA9B.place(x=1270, y=650)
        BA0B=Button(window, text="0",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase(0))
        BA0B.place(x=1270, y=750)
        BAclearB=Button(window, text="CLEAR\nBASE",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=clearlogbase)
        BAclearB.place(x=1065, y=750)
        BAdotB=Button(window, text=".",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlogbase('.'))
        BAdotB.place(x=860, y=750)




    def Logbase10():
        global BAdot,BAplus,BAminus,BAmultiply,BAdivide,expressionlog10,Elog10,Llog10,Lanslog10,Lanslog10only,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,Calculuslog10clean, eval10
        expressionlog10=''
        eval10=''
        Calculusinsideclean()
        Llog10=Label(window, image=logbase10)
        Llog10.place(x=345,y=125)
        def numaddlog10(numb):
            global expressionlog10      
            expressionlog10=expressionlog10 + str(numb)
            equationlog10.set(expressionlog10)
        def numequallog10():
            try:
                global expressionlog10,eval10
                eval10=str(eval(expressionlog10))
                total= str(log(float(eval10),10))
                valcmd=(Elog10.get(),total)
                equationanslog10.set(total)
                sqlcmd="insert into calhistory(input,output)values(%s,%s)"
                curs.execute(sqlcmd,valcmd)
                db.commit()
                expressionlog10 ="" 
            except:
                equationanslog10.set("ERROR")
                expressionlog10 = ""

        def clearlog10():
            global expressionlog10
            expressionlog10=""
            equationanslog10.set('')
            equationlog10.set('')
        def calculusreturnlog10():
            global Llog10,Lanslog10,Lanslog10only,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,Calculuslog10clean,Elog10,BAplus,BAminus,BAmultiply,BAdivide,BAdot
            Calculuslog10clean=[Llog10,Lanslog10,Lanslog10only,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,Elog10,BAplus,BAminus,BAmultiply,BAdivide,BAdot]
            for i in Calculuslog10clean:
                i.after(10,i.destroy())
            Calculus_Screen()


        equationlog10=StringVar()
        equationanslog10=StringVar()
        Lanslog10=Label(window, text="Answer =",textvariable=equationanslog10, width=35, height=5, font=("Times New Roman",26), bg="#0df0ea", fg="#c9210d", bd=3, relief="sunken")
        Lanslog10.place(x=544, y=230)
        Lanslog10only=Label(window, text="Answer =", width=10, height=5, font=("Times New Roman",26), bg="#0df0ea", fg="#c9210d", bd=3, relief="sunken")
        Lanslog10only.place(x=345,y=230)
        Elog10=Entry(window, bg="#14ebeb", fg="#df0a0a", width =20,borderwidth='3',relief='groove', font=("Times New Roman", 40), textvariable=equationlog10)
        Elog10.place(x=550, y=130)
        BA1=Button(window, text="1",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(1))
        BA1.place(x=250, y=450)
        BA2=Button(window, text="2",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(2))
        BA2.place(x=455, y=450)
        BA3=Button(window, text="3",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(3))
        BA3.place(x=660,y=450)
        BA4=Button(window, text="4",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(4))
        BA4.place(x=250,y=550)
        BA5=Button(window, text="5",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(5))
        BA5.place(x=455,y=550) 
        BA6=Button(window, text="6",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(6))
        BA6.place(x=660,y=550)
        BA7=Button(window, text="7",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(7))
        BA7.place(x=250, y=650)
        BA8=Button(window, text="8",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(8))
        BA8.place(x=455, y=650)
        BA9=Button(window, text="9",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(9))
        BA9.place(x=660, y=650)
        BA0=Button(window, text="0",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10(0))
        BA0.place(x=250, y=750)
        BAequal=Button(window, text="=",bg="blue",width="15",height="3", fg="white", relief="raised",font=("Times New Roman",18), command=numequallog10)
        BAequal.place(x=660, y=750)
        BAclear=Button(window, text="CLEAR",bg='black',width="35",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=clearlog10)
        BAclear.place(x=865, y=650)
        BAreturn=Button(window, text="RETURN",bg='#5f6161',width="35",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=calculusreturnlog10)
        BAreturn.place(x=865, y=750)
        BAplus=Button(window, text="+",bg="#11ca74",width="18",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddlog10('+'))
        BAplus.place(x=865, y=450)
        BAminus=Button(window, text="-",bg="#11ca74",width="17",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddlog10('-'))
        BAminus.place(x=1109,y=450)
        BAmultiply=Button(window, text="*",bg="#11ca74",width="18",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddlog10('*'))
        BAmultiply.place(x=865, y=550)
        BAdivide=Button(window, text="/",bg="#11ca74",width="17",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddlog10('/'))
        BAdivide.place(x=1109, y=550)
        BAdot=Button(window, text=".",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddlog10('.'))
        BAdot.place(x=455, y=750)
        

    def Ln():
        global BAdot,BAe,evalln,expressionln,Ln,Lansln,Lanslnonly,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,Calculuslnclean,Eln,BAplus,BAminus,BAmultiply,BAdivide
        Calculusinsideclean()
        expressionln=' '
        Ln=Label(window, image=lntitile)
        Ln.place(x=345,y=118)
        def numaddln(numb):
            global expressionln      
            expressionln=expressionln + str(numb)
            equationln.set(expressionln)
        def numequalln():
            try:
                global expressionln

                expressionln=expressionln.replace('e', str(math.e))
                evalln=str(eval(expressionln))
                total= str(log(float(evalln),math.e))
                valcmd=(Eln.get(),total)
                equationansln.set(total)
                sqlcmd="insert into calhistory(input,output)values(%s,%s)"
                curs.execute(sqlcmd,valcmd)
                db.commit()
                expressionln ="" 
            except:
                equationansln.set("ERROR")
                expressionln = ""

        def clearln():
            global expressionln
            expressionln=""
            equationansln.set('')
            equationln.set('')
        def calculusreturnln():
            global BAdot,BAe,Ln,Lansln,Lanslnonly,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,Calculuslnclean,Eln,BAplus,BAminus,BAmultiply,BAdivide
            Calculuslnclean=[BAdot,BAe,Ln,Lansln,Lanslnonly,BA1,BA2,BA3,BA4,BA5,BA6,BA7,BA8,BA9,BA0,BAequal,BAclear,BAreturn,Eln,BAplus,BAminus,BAmultiply,BAdivide]
            for i in Calculuslnclean:
                i.after(10,i.destroy())
            Calculus_Screen()


        equationln=StringVar()
        equationansln=StringVar()
        Lansln=Label(window, text="Answer =",textvariable=equationansln, width=35, height=5, font=("Times New Roman",26), bg="#0df0ea", fg="#c9210d", bd=3, relief="sunken")
        Lansln.place(x=544, y=230)
        Lanslnonly=Label(window, text="Answer =", width=10, height=5, font=("Times New Roman",26), bg="#0df0ea", fg="#c9210d", bd=3, relief="sunken")
        Lanslnonly.place(x=345,y=230)
        Eln=Entry(window, bg="#14ebeb", fg="#df0a0a", width =20,borderwidth='3',relief='groove', font=("Times New Roman", 40), textvariable=equationln)
        Eln.place(x=550, y=130)
        BA1=Button(window, text="1",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(1))
        BA1.place(x=250, y=450)
        BA2=Button(window, text="2",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(2))
        BA2.place(x=455, y=450)
        BA3=Button(window, text="3",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(3))
        BA3.place(x=660,y=450)
        BA4=Button(window, text="4",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(4))
        BA4.place(x=250,y=550)
        BA5=Button(window, text="5",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(5))
        BA5.place(x=455,y=550) 
        BA6=Button(window, text="6",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(6))
        BA6.place(x=660,y=550)
        BA7=Button(window, text="7",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(7))
        BA7.place(x=250, y=650)
        BA8=Button(window, text="8",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(8))
        BA8.place(x=455, y=650)
        BA9=Button(window, text="9",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(9))
        BA9.place(x=660, y=650)
        BA0=Button(window, text="0",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln(0))
        BA0.place(x=250, y=750)
        BAequal=Button(window, text="=",bg="blue",width="17",height="3", fg="white", relief="raised",font=("Times New Roman",18), command=numequalln)
        BAequal.place(x=865, y=750)
        BAclear=Button(window, text="CLEAR",bg='black',width="18",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=clearln)
        BAclear.place(x=1094, y=750)
        BAreturn=Button(window, text="RETURN",bg='#5f6161',width="36",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=calculusreturnln)
        BAreturn.place(x=865, y=650)
        BAplus=Button(window, text="+",bg="#11ca74",width="18",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddln('+'))
        BAplus.place(x=865, y=450)
        BAminus=Button(window, text="-",bg="#11ca74",width="17",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddln('-'))
        BAminus.place(x=1109,y=450)
        BAmultiply=Button(window, text="*",bg="#11ca74",width="18",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddln('*'))
        BAmultiply.place(x=865, y=550)
        BAdivide=Button(window, text="/",bg="#11ca74",width="17",height="3", fg="red", relief="raised",font=("Times New Roman",18), command=lambda: numaddln('/'))
        BAdivide.place(x=1109, y=550)
        BAe=Button(window, text="e",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln('e'))
        BAe.place(x=455, y=750)
        BAdot=Button(window, text=".",bg='black',width="15",height="3", fg='white',relief='raised',font=("Times New Roman",18),command=lambda: numaddln('.'))
        BAdot.place(x=660, y=750)



    LC1=Label(window, image=calculustitle, relief='groove')
    LC1.place(x=345, y=75)
    Blog10=Button(window, text="Log10", width=15, height=2, relief='raised', bd=5, bg="#47ce16", font=("Times New Roman", 30), command=Logbase10)
    Blog10.place(x=200, y=400)
    Blog=Button(window, text="Log", width=15, height=2, relief='raised', bd=5, bg="#47ce16", font=("Times New Roman", 30), command=LogBase)
    Blog.place(x=600, y=400)
    Bln=Button(window, text="Ln", width=15, height=2, relief='raised', bd=5, bg="#47ce16", font=("Times New Roman", 30), command=Ln)
    Bln.place(x=1000, y=400)
    Breturn=Button(window, text="Return", width=15, height=2, relief='raised', bd=5, bg="gray", font=("Times New Roman", 30), command=Calculusreturn)
    Breturn.place(x=600, y=700)


window.state('zoomed')
window.title("Mathematical Calculator")
headtitleimage=PhotoImage(file="headtitle.png")
window.iconbitmap("calculator.ico")
photobg=PhotoImage(file="bground.png")

def Homescreen():
    global bg, L1, B1, B2, B3
    bg=Canvas(window, width=1920, height=1080)
    bg.pack(fill="both", expand=True)
    bg.create_image( 0, 0, image=photobg, anchor='nw')



    L1=tkinter.Label(window, image=headtitleimage)
    L1.place(x=xp, y=yp)

    B1=Button(window, text="ALGEBRA", bd=5, bg="#1ae9e9", font=("Times New Roman", 36), command=Algebra_Screen)
    B1.place(x=450, y=500)

    B2=Button(window, text="CALCULUS", bd=5, bg="#1ae9e9", font=("Times New Roman", 36), command=Calculus_Screen)
    B2.place(x=850, y= 500)
Homescreen()
window.mainloop()