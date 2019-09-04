import xlutils
import xlrd
import xlwt
import smtplib
import random
import time
print('WELCOME')
rb=xlrd.open_workbook('newgmail.xls')
wb=xlwt.Workbook()
from xlutils.copy import copy
wb=copy(rb)
ws1=wb.get_sheet(0)
while(True):
    for j in range(0,100):
        a=input('''press 1 for signup a account
press 2 for login a account\n''')
        if(a=='1'):
            print('For signup please enter your details:')
            name=input('''Enter your name:''')
            ws1.write(j,0,name)
            eid=input('''Enter your Email ID:''')
            if(eid[-1]=='m' and eid[-2]=='o' and eid[-3]=='c' and eid[-4]=='.' and eid[-5]=='l' and eid[-6]=='i' and eid[-7]=='a' and eid[-8]=='m' and eid[-9]=='g' and eid[-10]=='@'):
                ws1.write(j,1,eid)
            else:
                print('enter valid email')
                continue
            number=int(input('''Enter Your Mobile Number:'''))
            s=str(number)
            l=len(s)
            if(l!=10):
                print('mobile number should be of 10 digits')
                continue
            else:
                pass
            while(True):
                number=int(s)
                ws1.write(j,2,number)    
                print('''Enter your Date of Birth''')
                d=int(input('Enter the Birth day:\n'))
                m=int(input('Enter the Birth month:\n'))
                y=int(input('Enter the Birth year:\n'))
                if(1<=d<=31 and 1<=m<=12 and 190<=y<=2008):
                    break
                else:
                    print('Enter valid DOB')
                    continue
            dt=str(d)
            mon=str(m)
            yr=str(y)
            dob=dt+'-'+mon+'-'+yr
            ws1.write(j,3,dob)
            uname=input('''Enter your Username:''')
            ws1.write(j,4,uname)
            pwd=input('''Enter your Password[it should be of atleast 6 characters and contain atleast 1 letter,1 number]:''')
            l=len(pwd)
            if(l<6):
                print('password should be of 6 characters')
                continue
            else:
                pass
            for i in pwd:
                d=i.isdigit()
                if(d==1):
                    break
                else:
                    continue
            for i in pwd:
                a=i.isalpha()
                if(a==1):
                    break
                else:
                    continue
            if(d!=1 or a!=1):
                print('Password should contain atleast 1  letter,1 number')
                continue
            else:
                ws1.write(j,5,pwd)
            repwd=input('''Retype your password:''')
            if(pwd==repwd):
                pass
            else:
                print('Enter same password')
                continue
            ws1.write(j,6,repwd)
            wb.save('newgmail.xls')
            print('Account created successfully.')
        if(a=='2'):
            while(True):
                wb=xlrd.open_workbook('newgmail.xls')
                ws1=wb.sheet_by_index(0)
                uname=input('Enter your username:')
                pwd=input('Enter password:')
                p=ws1.col_values(4)
                q=ws1.col_values(5)
                count=0
                if(count>=3):
                    print('you have entered the wrong password 3 times,wait for 10 sec')
                    time.sleep(10)
                    continue
                for e in range(0,j):
                    if(p[e]==uname and q[e]==pwd):
                        break
                    else:
                        print('enter valid username and password')
                        count=count+1
                        continue
                otp=random.randint(100000,999999)
                s=ws1.cell_value(e,1)
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login('praveen93146@gmail.com','praveen@1998')
                server.sendmail('praveen93146@gmail.com',s,str(otp))
                check=int(input('Enter the OTP:'))
                if(check==int(otp)):
                    print('login successful')
                else:
                    print('enter correct otp')
                break    
    break                    
            
               
                    
                
                    
            
            
            
    
