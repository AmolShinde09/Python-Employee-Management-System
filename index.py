# shree Ganesh
# Employee Management system using Python TKinter

from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox,filedialog
from PIL import ImageTk, Image
import pymongo
import random  
import time 

# creating DB Connection
conn = pymongo.MongoClient('mongodb://localhost:27017/')['EmpManagementSytemPy']
coll = conn['EmpDetails']
collReg = conn['userRegistration']



class Employee:
             
      # Login Form
      def loginAdminAnEmp(self):

                
                  # shows message to user software subscription end coming soon OR subscription end coming
                  liveTime = time.time()              

                  startTime = 1703645893
                  expireSoonTime = 1000  
                  expireTime = 10000  

                  expireSoonTime = (startTime + expireSoonTime)
                  expireTime = (startTime + expireTime)

                  # subscription ending coming soon
                  if( liveTime > expireSoonTime and liveTime < expireTime):
                        messagebox.showwarning(title="expire comming soon",message="subscription expire comming soon...")
                   
                  # subscription end
                  if(liveTime > expireTime):
                        return messagebox.showerror(title="expire",message="please pay bill to use sotware")
                  

                  em = Tk()

                  # Destroy Image from Screen  
                  def destroyImage():
                        i = 1
                        for widget in em.winfo_children():
                              if(i == 54 ): 
                                    widget.destroy()     
                              i = i + 1 
                              
                        
                  # Upload Image function    
                  def uploadImage():
                        
                        # Specifying which types images allowed
                        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])

                        # Destroy old image after taken new image  
                        if(file_path != ''):

                              destroyImage()

                              global getImagePath
                              getImagePath = file_path

                              # label for image
                              image_label = Label(em)
                              image_label.place(y=100,x=950)

                              # Showing image on label
                              image = Image.open(file_path)
                              image = image.resize((150,200))
                              image_tk = ImageTk.PhotoImage(image)
                              image_label.config(image=image_tk)
                              image_label.image = image_tk
                   

                  # Employee Details Screen 
                  def fun(loginId): 
                               
                        for widget in em.winfo_children():
                              widget.destroy()
                        
                        # Title
                        em.title("Employee Management System")
                                                      
                        # Header Div
                        header = Frame(em,height=30,width=1300).place(y=0,x=0)

                        # Left Div (Employee Details Div)
                        left = Frame(em,width=900,height=500).place(y=30,x=0)
                        
                        # Software Header
                        Label(header,text="Employee Management System",font=(' ',15,'bold'),fg='black').place(y=10,x=500)  # 1260


                        # Employee Details Label & Entery

                        # First Column
                        # 1) Name
                        global getName
                        getName = StringVar()
                        getName.set('')
                        Label(left,text="Name :",font=('',10),fg='black').place(y=80,x=50)
                        name = Entry(left,width=30,textvariable=getName,font=('',10),background='white')
                        name.place(y=80,x=150)
                  
                        # 2) Phone No
                        getPhonNo = StringVar()
                        getPhonNo.set('')
                        Label(left,text="Phone No :",font=('',10),fg='black').place(y=120,x=50)
                        phonNo = Entry(left,width=20,textvariable=getPhonNo,font=('',10),bd='1px',background='white')
                        phonNo.place(y=120,x=150)

                        # 3) Email
                        getEmail = StringVar()
                        getEmail.set('')
                        Label(left,text="Email:",font=('',10),fg='black').place(y=160,x=50)
                        email = Entry(left,width=30,textvariable=getEmail,font=('',10),bd='1px',background='white')
                        email.place(y=160,x=150)
                                   
                        # 4) Gender
                        getGender = StringVar()
                        getGender.set('Select Gender')
                        Label(left,text="Gender :",font=('',10),fg='black').place(y=200,x=50)
                        gender = ttk.Combobox(left,width=15,textvariable=getGender,font=('',10),background='white')
                        gender['state']='readonly'
                        gender['values']=('Male','Female')
                        gender.place(y=200,x=150)                        

                        # 5) Marital Status
                        getMaritalStatus = StringVar()
                        getMaritalStatus.set('Select Status')
                        Label(left,text="Marital Status:",font=('',10),fg='black').place(y=240,x=50)
                        maritalStatus = ttk.Combobox(left,width=15,textvariable=getMaritalStatus,font=('',10),background='white')
                        maritalStatus['state']='readonly'
                        maritalStatus['values']=('Unmarried','Married','Divorced')
                        maritalStatus.place(y=240,x=150)
                                    
                        # 6) DOB
                        getDay = StringVar()
                        getMonth = StringVar()
                        getYear = StringVar()
                        getDay.set('')
                        getMonth.set('')
                        getYear.set('')

                        Label(left,text="DOB :",font=('',10),fg='black').place(y=280,x=50)
                        day = Entry(left,width=5,justify='center',textvariable=getDay,validate='all',font=('',10),bd='1px',background='white')
                        day.place(y=280,x=150)
                        month = Entry(left,width=5,justify='center',textvariable=getMonth,validate='all',font=('',10),bd='1px',background='white')
                        month.place(y=280,x=200)
                        year = Entry(left,width=10,justify='center',textvariable=getYear,validate='all',font=('',10),bd='1px',background='white')
                        year.place(y=280,x=250)
                        Label(left,text="DD",font=('',8),fg='black').place(y=300,x=157)
                        Label(left,text="MM",font=('',8),fg='black').place(y=300,x=207)
                        Label(left,text="YYYY",font=('',8),fg='black').place(y=300,x=265)
            

                        # 7) Address
                        getAddress = StringVar()
                        getAddress.set('')
                        Label(left,text="Address :",font=('',10),fg='black').place(y=340,x=50)
                        adress = Entry(left,width=30,textvariable=getAddress,font=('',10),bd='1px',background='white')
                        adress.place(y=340,x=150)

                        # 8) Country
                        getCountry = StringVar()
                        getCountry.set('')
                        Label(left,text="Country :",font=('',10),fg='black').place(y=380,x=50)
                        getCountry.set("Select Country")
                        country = ttk.Combobox(left,width=20,textvariable=getCountry,font=('',10),background='white')
                        country['state']='readonly'
                        country['values']=('United States','China','Japan','United Kingdom','India','France','Canada','Other')
                        country.place(y=380,x=150)

                        # second Column 

                        # 9) Department Name
                        getDepartmentName = StringVar()
                        getDepartmentName.set('Select Department')
                        Label(left,text="Department Name :",font=('',10),fg='black').place(y=80,x=500)
                        departmentName = ttk.Combobox(left,width=20,textvariable=getDepartmentName,font=('',10),background='white')
                        departmentName['state']='readonly'
                        departmentName['values']=('Software Development','Quality Assurance (QA)','Technical Support','Project Management','Sales and Marketing','Human Resources (HR)','Finance and Accounting','Research and Development')
                        departmentName.place(y=80,x=650)

                        # 10) Designition 
                        getDesignition = StringVar()
                        getDesignition.set('Select Designition')
                        Label(left,text="Designition :",font=('',10),fg='black').place(y=120,x=500)
                        # designition = Entry(left,width=20,textvariable=getDesignition,font=('',10),bd='1px',background='white').place(y=120,x=650)
                        designition = ttk.Combobox(left,width=20,textvariable=getDesignition,font=('',10),background='white')
                        designition['state']='readonly'
                        designition['values']=('Software Developer','Software Tester','UI Designer','Project Manager','HR Manager','Business Analyst','Systems Administrator','Account Manager',)
                        designition.place(y=120,x=650)

                        # 11) salary(CTC)
                        getSalary = StringVar()
                        getSalary.set('')
                        Label(left,text="Salary (CTC) :",font=('',10),fg='black').place(y=160,x=500)
                        salary = Entry(left,width=20,textvariable=getSalary,font=('',10),bd='1px',background='white')
                        salary.place(y=160,x=650)
                        
                        # 12) Id Proof
                        getIdProof = StringVar()
                        getIdProof.set('')
                        getSelectedIdProof = StringVar()
                        getSelectedIdProof.set('Select Id Proof')
                        selectedIdProof = ttk.Combobox(left,width=15,textvariable=getSelectedIdProof,font=('',10),background='red')
                        selectedIdProof['state']='readonly'
                        selectedIdProof['values']=('Adhar Card','Pan Card','PassPort')
                        selectedIdProof.place(y=200,x=500)
                        idProof = Entry(left,width=20,textvariable=getIdProof,font=('',10),bd='1px',background='white')
                        idProof.place(y=200,x=650)
                        
                        # 13) Blood Gruop
                        getBloodGroup = StringVar()
                        getBloodGroup.set('Select Blood Group')
                        Label(left,text="Blood Group :",font=('',10),fg='black').place(y=240,x=500)
                        bloodGroup = ttk.Combobox(left,width=17,textvariable=getBloodGroup,font=('',10),background='white')
                        bloodGroup['state']='readonly'
                        bloodGroup['values']=('A+','A-','B+','B-','O+','O-','AB+','AB-')
                        bloodGroup.place(y=240,x=650)

                        # 14) JOD
                        getJDay = StringVar()
                        getJMonth = StringVar()
                        getJYear = StringVar()
                        Label(left,text="JOD :",font=('',10),fg='black').place(y=280,x=500)
                        jday = Entry(left,width=5,justify='center',textvariable=getJDay,validate='all',font=('',10),bd='1px',background='white')
                        jday.place(y=280,x=650)
                        jmonth = Entry(left,width=5,justify='center',textvariable=getJMonth,validate='all',font=('',10),bd='1px',background='white')
                        jmonth.place(y=280,x=700)
                        jyear = Entry(left,width=10,justify='center',textvariable=getJYear,validate='all',font=('',10),bd='1px',background='white')
                        jyear.place(y=280,x=750)
                        Label(left,text="DD",font=('',8),fg='black').place(y=300,x=660)
                        Label(left,text="MM",font=('',8),fg='black').place(y=300,x=710)
                        Label(left,text="YYYY",font=('',8),fg='black').place(y=300,x=770)
                                                
                        # 15) Employment Type
                        getEmployeetype = StringVar()
                        getEmployeetype.set('Selct Emp Type')
                        Label(left,text="Employee Type :",font=('',10),fg='black').place(y=340,x=500)
                        employeeType = ttk.Combobox(left,width=15,textvariable=getEmployeetype,font=('',10),background='white')
                        employeeType['state']='readonly'
                        employeeType['values']=('Full Time','Part Time','Intership','Contract ')
                        employeeType.place(y=340,x=650)
                  
                        # 16) Id
                        getEmpId = StringVar()
                        getEmpId.set('')
                        Label(left,text="Employee ID :",font=('',10),fg='black').place(y=380,x=500)
                        empId = Entry(left,width=20,textvariable=getEmpId,font=('',10),bd='1px',background='white')
                        empId.place(y=380,x=650)

                        # 17) Employee Image
                        Label(left,text="Employee Image ",font=('',10),fg='black').place(y=70,x=975)


                        # Screen for who is login as Employee shows below Readonly screen 
                        if(loginId != 0):

                              def fetchSingleEmployeeData(loginId):
                                                             
                                                            def destroyFields():
                                                                  i = 1
                                                                  for widget in em.winfo_children():
                                                                        if( i == 11 or i == 13 or i == 24 or i == 26 or i == 28 or i == 31 or i == 43 ): # image_label this lable on 54 no so deleting befor set new image
                                                                              widget.destroy()                                                                           
                                                                        i = i + 1                                          
                                                                 
                                                            try:
                                                                  
                                                                 # disabled (Readonly) field show to Employee login  
                                                                        
                                                                  name.config(state='readonly')
                                                                  phonNo.config(state='readonly') 
                                                                  email.config(state='readonly') 
                                                                  gender.config(state='readonly')
                                                                  maritalStatus.config(state='readonly')
                                                                  day.config(state='readonly')
                                                                  month.config(state='readonly')
                                                                  year.config(state='readonly')
                                                                  adress.config(state='readonly')
                                                                  departmentName.config(state='readonly')
                                                                  salary.config(state='readonly')
                                                                  idProof.config(state='readonly')
                                                                  jday.config(state='readonly')
                                                                  jmonth.config(state='readonly')
                                                                  jyear.config(state='readonly')
                                                                  employeeType.config(state='readonly')  
                                                                  empId.config(state='readonly')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                  data =  coll.find_one({'id':loginId})
                                    
                                                                  getName.set(data['name'])
                                                                  getPhonNo.set(data['phone_no'])
                                                                  getEmail.set(data['email'])                                                            
                                                                  getDay.set(data['dob'][0])
                                                                  getMonth.set(data['dob'][1])
                                                                  getYear.set(data['dob'][2])
                                                                  getAddress.set(data['address'])                                                                  
                                                                  getSalary.set(data['salary'])                                                                  
                                                                  getIdProof.set(data['idProof'])                                                                  
                                                                  getJDay.set(data['jod'][0])
                                                                  getJMonth.set(data['jod'][1])
                                                                  getJYear.set(data['jod'][2])                                                                  
                                                                  getEmpId.set(data['id'])   
                                                                                                                                                                                   
                                                                  getGender = StringVar()
                                                                  getGender.set(data['gender'])
                                                                  Entry(em,width=20,textvariable=getGender,font=('',10),bd='1px',background='white',state='readonly').place(y=200,x=150)
                                                                                                                              
                                                                  getMaritalStatus = StringVar()
                                                                  getMaritalStatus.set(data['maritalStatus'])
                                                                  Entry(em,width=20,textvariable=getMaritalStatus,font=('',10),bd='1px',background='white',state='readonly').place(y=240,x=150)

                                                                  getCountry = StringVar()
                                                                  getCountry.set(data['country'])
                                                                  Entry(em,width=20,textvariable=getCountry,font=('',10),bd='1px',background='white',state='readonly').place(y=380,x=150)
                                                                 
                                                                  getDepartmentName = StringVar()
                                                                  getDepartmentName.set(data['departmentName'])
                                                                  Entry(em,width=20,textvariable=getDepartmentName,font=('',10),bd='1px',background='white',state='readonly').place(y=80,x=650)
                                                                  
                                                                  getDesignition = StringVar()
                                                                  getDesignition.set(data['designition'])
                                                                  Entry(em,width=20,textvariable=getDesignition,font=('',10),bd='1px',background='white',state='readonly').place(y=120,x=650)
                                                                                                                                                     
                                                                  Label(em,width=10,text=f"{data['selcetedIdProof']} :",font=('',10),fg='black',justify='left').place(y=200,x=490)
                                                      
                                                                  getBloodGroup = StringVar()
                                                                  getBloodGroup.set(data['bloodGroup'])
                                                                  Entry(em,width=20,textvariable=getBloodGroup,font=('',10),bd='1px',background='white',state='readonly').place(y=240,x=650)
                                                                  
                                                                  getEmployeetype = StringVar()
                                                                  getEmployeetype.set(data['employeeType'])
                                                                  Entry(em,width=20,textvariable=getEmployeetype,font=('',10),bd='1px',background='white',state='readonly').place(y=340,x=650)
                                                         
                                                                  empFullName = data['name']
                                                                  empFirstAnLastName = empFullName.split()
                                                                  Label(em,width=25,text=f"{empFirstAnLastName[0]} {empFirstAnLastName[-1]}",font=('',12),fg='black',justify='center').place(y=310,x=915)
                                                                 
                                                                  Label(em,width=50,text="Your contributions are vital to our success...",font=('',15),fg='black',justify='left').place(y=500,x=380)


                                                                  try:
                                                                                                                                          
                                                                        destroyFields()
                                                                        
                                                                        # Set Image on Screen
                                                                        def setImage():

                                                                              image_label = Label(em)
                                                                              image_label.place(y=100,x=950)
                                                                              global getImagePath
                                                                              getImagePath = data['imagePath']
                                                                              image = Image.open(getImagePath)
                                                                              image = image.resize((150,200))
                                                                              image_tk = ImageTk.PhotoImage(image)
                                                                              image_label.config(image=image_tk)
                                                                              image_label.image = image_tk
                                                                  
                                                                        setImage()

                                                                  except:
                                                                              return  messagebox.showerror(title="Image",message="Image realeted problem by using login id")                                                                         
                                                                  
                                                            except:
                                                                  return  messagebox.showerror(title="Wrong id",message="Given id Data not exist in system")
                                                            

                                                            # login successfull message showing
                                                            return messagebox.showinfo(title="login Success",message="Your login Successfully")
          
                              fetchSingleEmployeeData(loginId)
                                                            
                                                                                                                                                                                                                                          
                        if(loginId == 0) :                                                                                                                                                

                                    Button(left,text="choose Image",command=uploadImage,width=15).place(y=320,x=972)                                                                  

                                    # Fetch Singe Employee Data using Employee Id


                                    #  After data insert or Update in DB then clear fields value
                                    def clearFields():
                                          
                                          getName.set('')
                                          getPhonNo.set('')
                                          getEmail.set('')
                                          getGender.set('Select Gender')
                                          getMaritalStatus.set('Select Status')
                                          getDay.set('')
                                          getMonth.set('')
                                          getYear.set('')
                                          getAddress.set('')
                                          getCountry.set('')
                                          getDepartmentName.set('Select Department')
                                          getDesignition.set('')
                                          getSalary.set('')
                                          getSelectedIdProof.set('Select Id Proof')
                                          getIdProof.set('')
                                          getBloodGroup.set('select blood group')
                                          getJDay.set('')
                                          getJMonth.set('')
                                          getJYear.set('')
                                          getEmployeetype.set('Select Emp Type')
                                          getEmpId.set('')
                  
                                          empId.config(state='normal')
                                                                        

                                    # Data Validation (user Entery Data Validation)
                                    def DataValidationAndInsert():
                  
                                          nameLenValid =len(getName.get())
                                          phoneLenValid = len(getPhonNo.get())
                                          emailValid = getEmail.get()[-10:]
                                          genderValid = getGender.get()
                                          maritalStatusValid = getMaritalStatus.get()                              
                                          addressValid = len(getAddress.get())
                                          countryValid = len(getCountry.get())
                                          departmentNameValid =getDepartmentName.get()
                                          designitionValid  = getDesignition.get()
                                          salaryValid = getSalary.get()
                                          selectedIdProofValid = getSelectedIdProof.get()
                                          idProofValid = getIdProof.get()
                                          bloodGroupValid = getBloodGroup.get()                                    
                                          employeeTypeValid = getEmployeetype.get()                                                  
                                          employeeIdValid  = getEmpId.get()
                                                                               

                                          if( nameLenValid< 6):
                                                return   messagebox.showinfo(title="Error",message="please Enter Name At least 5 char")
                                          if(nameLenValid > 30):
                                                return   messagebox.showinfo(title="Error",message="not allow above 30 char in Name")

                                          if( phoneLenValid < 10 or phoneLenValid > 10):
                                                return  messagebox.showinfo(title="less No",message="Please Enetr correct Phone Number... Amol.S")

                                          if(emailValid != '@gmail.com' and emailValid != '@email.com' ):
                                                return messagebox.showerror(title="invalid Email",message="Please Enter Valid Email...Amol.S")                                    

                                          if( genderValid == 'Select Gender'):
                                                return  messagebox.showerror(title="select Gender",message="your not selected gender please Select Gender")

                                          if(maritalStatusValid == 'Select Status'):
                                                return messagebox.showerror(title='select marital Status',message="your not selected Marital Status please select")

                                          # DoB Validation
                                          try:
                                                dayValid = int(getDay.get())
                                                monthValid =int(getMonth.get())
                                                yearValid = int(getYear.get())
                                          except:
                                                return messagebox.showerror(title="empty DOB",message="please Enter DOB")
                                          if(dayValid > 0 and dayValid < 32 and monthValid > 0 and monthValid < 13 and yearValid > 1960 and yearValid < 2009): 
                                                pass                                       
                                          else:
                                                return messagebox.showerror(title="Invalid Date",message="Please Enter Correct DOB Date check day/month/year  and check year allow between 1960 to 2009 ... Amol Shinde  ")

                                          if(addressValid > 100 ):
                                                return messagebox.showerror(title="long Address",message="not allow greater than 100 char address")
                                          if(addressValid < 1 ):
                                                return messagebox.showerror(title="Empty Address",message="please Enter Address")
                                          if(addressValid > 1 and addressValid < 5 ):
                                                return messagebox.showerror(title="Spam Address",message="please Enter Real/orignal Address")
                        
                                          if(countryValid == 'Select Country'):
                                                return messagebox.showerror(title="not selected",message="please Select country")
                                          
                                          if(departmentNameValid == 'Select Department'):
                                                return messagebox.showerror(title="Select Department",message="Please Select Department")
                                                                                    
                                          if(designitionValid == 'Select Designition'):
                                                return messagebox.showerror(title="Not selected designation",message="Please select designation")                                                                        
                                          
                                          if(salaryValid == ''):
                                                return messagebox.showerror(title="Empty Salary",message="Please Enter Salary .. Amol.S")
                                          
                                          try:
                                                salary = int(getSalary.get())
                                          except:
                                                return messagebox.showerror(title="Int Error",message="Salary Must be Digits Amol.S")

                                          if(salary > 1000000000):
                                                return messagebox.showerror(title="High Salary",message="Company Not allow above 100cr Salary (CTC) ... Amol.S")
                                                                                               
                                          if(selectedIdProofValid == 'Select Id Proof'):
                                                return messagebox.showerror(title="Not selected",message="Please Select Id Proof")
            
                                          if(selectedIdProofValid == 'Adhar Card'):
                                                if(len(idProofValid) >= 0 and len(idProofValid) < 12 or len(idProofValid) > 12 ): 
                                                      return messagebox.showerror(title="Invalid Adhar",message=f"Please Enter Valid 12 Digit Adhar Number You Entered {len(idProofValid)} Digit ... Amol.S")
                                                              
                                          if(selectedIdProofValid == 'Pan Card' ):
                                                if(len(idProofValid) >= 0 and len(idProofValid) < 10 or len(idProofValid) > 10 ): 
                                                      return messagebox.showerror(title="Invalid Pan Card",message=f"Please Enter Valid  Pan Card Number ... Amol Shinde")
                 
                                          if(selectedIdProofValid == 'PassPort'):
                                                if(len(idProofValid) >= 0 and len(idProofValid) < 12 or len(idProofValid) > 12 ): 
                                                      return messagebox.showerror(title="Invalid PassPort",message=f"Please Enter Valid PassPort Number ... Amol Shinde")
                                                           
                                          if(bloodGroupValid == 'select blood group'): 
                                                return messagebox.showerror(title="Empty Blood Group",message=f"Please Select Blood Group")
                  
                                          # Join Date Validation
                                          try:
                                                dayJValid = int(getJDay.get())
                                                monthJValid =int(getJMonth.get())
                                                yearJValid = int(getJYear.get())
                                          except:
                                                return messagebox.showerror(title="empty JOD",message="please Enter Join of Date")
                                          if(dayJValid > 0 and dayJValid < 32 and monthJValid > 0 and monthJValid < 13 and yearJValid > 2011 and yearJValid < 2024): 
                                                pass
                                          else:
                                                return messagebox.showerror(title="Invalid Date",message="Please Enter Correct JOD Date check day/month/year check year between 2011 to 2023 becuse compnay started from 2011 and now year 2023 .. Amol.S")

                                          # Employee Type
                                          if(employeeTypeValid == 'Selct Emp Type'):
                                                return messagebox.showerror(title="Empty Type",message="Please Select Employee Type")
                       
                                          # Employee Id Validation
                                          if(len(employeeIdValid) == 0):
                                                      return messagebox.showerror(title="Empty Id",message="Please Entery Id")
                                          if(len(employeeIdValid) > 3):
                                                      return messagebox.showerror(title="long Id",message="Id Must Be 3 Digit")
                                          if(len(employeeIdValid) < 3):
                                                      return messagebox.showerror(title="",message="Employee Id  Allowed 100 to 999")

                                          try:
                                                allData = coll.find()
                                                for e in allData:
                                                      if( employeeIdValid == e['id'] ):
                                                            return messagebox.showerror(title="exist id alrady",message=f"This Employee alrady exist with {employeeIdValid} id when you want to save updated data click on save updated button ... Amol Shinde")
                                          except:
                                                return messagebox.showerror(title="Ineer Error",message="Sorry  internal  emp Id realeated error try again")            
                                          
                                          # Image validation
                                          try:
                                                getImagePath 
                                          except:
                                                return messagebox.showerror(title="upload Image",message="Please upload Image  ... Amol.S")
                                                 
                                          allRegEmpData = collReg.find()
                                          flag = 0
                                          for e in allRegEmpData:
                                                if(e['empId'] == getEmpId.get()):
                                                     flag = 1                                                                                   
                                          
                                          if(flag):    

                                                # All Data is Valid then insert in DB

                                                # Inserting Data in DB
                                                coll.insert_one({
                                                      'name':getName.get(),
                                                      'phone_no':getPhonNo.get(),
                                                      'email':getEmail.get(),
                                                      'gender':getGender.get(),
                                                      'maritalStatus':getMaritalStatus.get(),
                                                      'dob':[
                                                            getDay.get(),
                                                            getMonth.get(),
                                                            getYear.get()
                                                      ],
                                                      'address':getAddress.get(),
                                                      'country':getCountry.get(),
                                                      'departmentName':getDepartmentName.get(),
                                                      'designition':getDesignition.get(),
                                                      'salary':salary,
                                                      'selcetedIdProof':getSelectedIdProof.get(),
                                                      'idProof':getIdProof.get(),
                                                      'bloodGroup':getBloodGroup.get(),
                                                      'jod':[
                                                            getJDay.get(),
                                                            getJMonth.get(),
                                                            getJYear.get()
                                                      ],
                                                      'employeeType':getEmployeetype.get(),
                                                      'id':getEmpId.get(),
                                                      'imagePath':getImagePath

                                                })

                                                # After Inserted data clear all fields

                                                # call destroy Iamge fun
                                                destroyImage()

                                                # clear field
                                                clearFields()                                              
                                             
                                                return messagebox.showinfo(title='success',message='Recored Inserted Successfuly... Amol Shinde')
                                          
                                          else:
                                                return messagebox.showinfo(title='not Register',message='Employee not rigister Please first Register')
                                                                                                                                           

                                    # botton for Insert Data in DB
                                    Button(em,text='Save',justify='center',command=DataValidationAndInsert, width=13,height=1,borderwidth=4,relief='raised',font=('',10,'bold')).place(y=450,x=300)                                                                                        


                                    # Fetching Single employee data using _id 
                                    getid = StringVar()
                                    getid.set('')
                                    singleEmployeeId = Entry(em,textvariable=getid,width=7,font=('',12),borderwidth=4)
                                    singleEmployeeId.place(y=452,x=820)
                                   
                                    def fetchSingleEmployeeData():

                                          if(getid.get() != ''):
                                                if(len(getid.get()) == 3 ):
                                                                 
                                                            try:
                                                                  empId.config(state='disabled')
                                                                  

                                                                  data =  coll.find_one({'id':getid.get()})
                                    
                                                                  getName.set(data['name'])
                                                                  getPhonNo.set(data['phone_no'])
                                                                  getEmail.set(data['email'])
                                                                  getGender.set(data['gender'])
                                                                  getMaritalStatus.set(data['maritalStatus'])
                                                                  getDay.set(data['dob'][0])
                                                                  getMonth.set(data['dob'][1])
                                                                  getYear.set(data['dob'][2])
                                                                  getAddress.set(data['address'])
                                                                  getCountry.set(data['country'])
                                                                  getDepartmentName.set(data['departmentName'])
                                                                  getDesignition.set(data['designition'])
                                                                  getSalary.set(data['salary'])
                                                                  getSelectedIdProof.set(data['selcetedIdProof'])
                                                                  getIdProof.set(data['idProof'])
                                                                  getBloodGroup.set(data['bloodGroup'])
                                                                  getJDay.set(data['jod'][0])
                                                                  getJMonth.set(data['jod'][1])
                                                                  getJYear.set(data['jod'][2])
                                                                  getEmployeetype.set(data['employeeType'])
                                                                  getEmpId.set(data['id'])       


                                                                  try:
                                                                        # deleting old Image
                                                                                                                                           
                                                                        destroyImage()
                                                                        
                                                                        # Set Image (Display Image on Screen)
                                                                        def setImage():

                                                                              image_label = Label(em)
                                                                              image_label.place(y=100,x=950)
                                                                              global getImagePath
                                                                              getImagePath = data['imagePath']
                                                                              image = Image.open(getImagePath)
                                                                              image = image.resize((150,200))
                                                                              image_tk = ImageTk.PhotoImage(image)
                                                                              image_label.config(image=image_tk)
                                                                              image_label.image = image_tk
                                                                  
                                                                        setImage()

                                                                        # After fetched data Id Remove from field
                                                                        getid.set('')

                                                                  except:
                                                                              return  messagebox.showerror(title="Image",message="Image realeted problem")
                                                                         
                                                            except:
                                                                  return  messagebox.showerror(title="Wrong id",message="Given ID is Not exist in system")                                                                                       
                                                                                                    
                                                else:
                                                      return  messagebox.showerror(title="3 digit",message="Please Enter 3 digit Id")
                                                               
                                          else:
                                                return  messagebox.showerror(title="Enter Id",message="Please Enter Employee Id for Search Employee Details ... Amol.S")
                                                 
                                    # Button Search Employee by Id                                   
                                    Button(em,text='Search Emp',justify='center',command=fetchSingleEmployeeData,width=13,height=1,borderwidth=4,relief='raised',font=('',10,'bold')).place(y=450,x=700)
                           
            
                                    # Update Employee Data 
                                   
                                    def updateData():
                                          
                                          nameLenValid =len(getName.get())
                                          phoneLenValid = len(getPhonNo.get())
                                          emailValid = getEmail.get()[-10:]
                                          genderValid = getGender.get()
                                          maritalStatusValid = getMaritalStatus.get()                                            
                                          addressValid = len(getAddress.get())
                                          countryValid = len(getCountry.get())
                                          departmentNameValid =getDepartmentName.get()
                                          designitionValid  = getDesignition.get()
                                          salaryValid = getSalary.get()
                                          selectedIdProofValid = getSelectedIdProof.get()
                                          idProofValid = getIdProof.get()
                                          bloodGroupValid = getBloodGroup.get()                                                                                               
                                          employeeTypeValid = getEmployeetype.get()                                                      
                                          employeeIdValid  = getEmpId.get()

                                          # Validating Data
                                          if( nameLenValid< 6):
                                                return   messagebox.showinfo(title="Error",message="please Enter Name At least 5 char")
                                          if(nameLenValid > 30):
                                                return   messagebox.showinfo(title="Error",message="not allow above 30 char in Name")

                                          if( phoneLenValid < 10 or phoneLenValid > 10):
                                                return  messagebox.showinfo(title="less No",message="Please Enetr correct Phone Number... Amol.S")

                                          if(emailValid != '@gmail.com' and emailValid != '@email.com' ):
                                                return messagebox.showerror(title="invalid Email",message="Please Enter Valid Email...Amol.S")                                          

                                          if( genderValid == 'Select Gender'):
                                                return  messagebox.showerror(title="select Gender",message="your not selected gender please Select Gender")

                                          if(maritalStatusValid == 'Select Status'):
                                                return messagebox.showerror(title='select marital Status',message="your not selected Marital Status please select")
                                         
                                          try:
                                                dayValid = int(getDay.get())
                                                monthValid =int(getMonth.get())
                                                yearValid = int(getYear.get())
                                          except:
                                                return messagebox.showerror(title="empty DOB",message="please Enter DOB")
                                          if(dayValid > 0 and dayValid < 32 and monthValid > 0 and monthValid < 13 and yearValid > 1960 and yearValid < 2009): 
                                                pass
                                          else:
                                                return messagebox.showerror(title="Invalid Date",message="Please Enter Correct DOB Date check day/month/year  and check year allow between 1960 to 2009 ... Amol Shinde  ")

                                          if(addressValid > 100 ):
                                                return messagebox.showerror(title="long Address",message="not allow greater than 100 char address")
                                          if(addressValid < 1 ):
                                                return messagebox.showerror(title="Empty Address",message="please Enter Address")
                                          if(addressValid > 1 and addressValid < 5 ):
                                                return messagebox.showerror(title="Spam Address",message="please Enter Real/orignal Address")
                        
                                          if(countryValid == 'Select Country'):
                                                return messagebox.showerror(title="not selected",message="please Select country")
                                          
                        
                                          if(departmentNameValid == 'Select Department'):
                                                return messagebox.showerror(title="Select Department",message="Please Select Department")
                                          
                                          if(designitionValid == 'Select Designition'):
                                                return messagebox.showerror(title="Not selected designation",message="Please select designation")
                                                                                  
                                          if(salaryValid == ''):
                                                return messagebox.showerror(title="Empty Salary",message="Please Enter Salary .. Amol.S")
                                                
                                          try:
                                                salary = int(getSalary.get())
                                          except:
                                                return messagebox.showerror(title="Int Error",message="Salary Must be Digits Amol.S")

                                          if(salary > 1000000000):
                                                return messagebox.showerror(title="High Salary",message="Company Not allow above 100cr Salary (CTC) ... Amol.S")
                                                            
                                          if(selectedIdProofValid == 'Select Id Proof'):
                                                return messagebox.showerror(title="Not selected",message="Please Select Id Proof")
            
                                          if(selectedIdProofValid == 'Adhar Card'):
                                                if(len(idProofValid) >= 0 and len(idProofValid) < 12 or len(idProofValid) > 12 ): 
                                                      return messagebox.showerror(title="Invalid Adhar",message=f"Please Enter Valid 12 Digit Adhar Number You Entered {len(idProofValid)} Digit ... Amol.S")
                                                        
                                          if(selectedIdProofValid == 'Pan Card' ):
                                                if(len(idProofValid) >= 0 and len(idProofValid) < 10 or len(idProofValid) > 10 ): 
                                                      return messagebox.showerror(title="Invalid Pan Card",message=f"Please Enter Valid  Pan Card Number ... Amol Shinde")
                 
                                          if(selectedIdProofValid == 'PassPort'):
                                                if(len(idProofValid) >= 0 and len(idProofValid) < 12 or len(idProofValid) > 12 ): 
                                                      return messagebox.showerror(title="Invalid PassPort",message=f"Please Enter Valid PassPort Number ... Amol Shinde")
                                                                                                      
                                          if(bloodGroupValid == 'select blood group'): 
                                                return messagebox.showerror(title="Empty Blood Group",message=f"Please Select Blood Group")
                  
                                          # Join Date geting
                                          try:
                                                dayJValid = int(getJDay.get())
                                                monthJValid =int(getJMonth.get())
                                                yearJValid = int(getJYear.get())
                                          except:
                                                return messagebox.showerror(title="empty JOD",message="please Enter Join of Date")
                                          if(dayJValid > 0 and dayJValid < 32 and monthJValid > 0 and monthJValid < 13 and yearJValid > 2011 and yearJValid < 2024): 
                                                pass
                                          else:
                                                return messagebox.showerror(title="Invalid Date",message="Please Enter Correct JOD Date check day/month/year check year between 2011 to 2023 becuse compnay started from 2011 and now year 2023 .. Amol.S")
                                     
                                          if(employeeTypeValid == 'Selct Emp Type'):
                                                return messagebox.showerror(title="Empty Type",message="Please Select Employee Type")
                                                             
                                          if(len(employeeIdValid) == 0):
                                                      return messagebox.showerror(title="Empty Id",message="Please Entery Id")
                                          if(len(employeeIdValid) > 3):
                                                      return messagebox.showerror(title="long Id",message="Id Must Be 3 Digit")
                                          if(len(employeeIdValid) < 3):
                                                      return messagebox.showerror(title="",message="Employee Id  Allowed 100 to 999")
                                          
                                          # Image geting
                                          try:
                                                getImagePath 
                                          except:
                                                return messagebox.showerror(title="upload Image",message="Please upload Image  ... Amol.S")
                                                                               
                                          # Validating data
                                          if(getEmpId.get() != ''): 
 
                                                # Not allowed update using save button
                                                existingId = coll.find_one({'id':getEmpId.get()})                                               
                                                if(not existingId):
                                                      return messagebox.showerror(title="New Emp Save first",message="This Employee  is new so first save recored then  update .... Amol.S")
                                                                                                                                                      
                                                # if Employee existing DB
                                                try:
                                                
                                                      result = coll.update_one({'id':getEmpId.get()}, {'$set':{
                                                      'name':getName.get(),
                                                      'phone_no':getPhonNo.get(),
                                                      'email':getEmail.get(),
                                                      'gender':getGender.get(),
                                                      'maritalStatus':getMaritalStatus.get(),
                                                      'dob':[
                                                            getDay.get(),
                                                            getMonth.get(),
                                                            getYear.get()
                                                      ],
                                                      'address':getAddress.get(),
                                                      'country':getCountry.get(),
                                                      'departmentName':getDepartmentName.get(),
                                                      'designition':getDesignition.get(),
                                                      'salary':getSalary.get(),
                                                      'selcetedIdProof':getSelectedIdProof.get(),
                                                      'idProof':getIdProof.get(),
                                                      'bloodGroup':getBloodGroup.get(),
                                                      'jod':[
                                                            getJDay.get(),
                                                            getJMonth.get(),
                                                            getJYear.get()
                                                      ],
                                                      'employeeType':getEmployeetype.get(),
                                                      'id':getEmpId.get(),
                                                      'imagePath': getImagePath   # from fetch Singe Data fun

                                                      }})
                                                                                                                            
                                                      destroyImage()
                                    
                                                      clearFields()
                                                      getid.set('')
                                                      
                                                except:
                                                      return messagebox.showerror(title="internal error",message="internal error may be db connection error")
                                          else:
                                                return messagebox.showerror(title="Save first",message="please firts fetch data then update .. Amol ")
                                                                                                                                                                                                         
                                          return messagebox.showinfo(title="success",message="data Updated succesfully")
                                                            
                                    Button(em,text='Save updated',justify='center',command=updateData,width=13,height=1,borderwidth=4,relief='raised',font=('',10,'bold')).place(y=450,x=500)


                                    # Delete Employee 
                                    def deleteData():
                                          if(getEmpId.get() != ''):
                                                      
                                                      conf = messagebox.askyesno(title="confirmation",message="Your Confirm to delete Employee ? ... Amol.S")
                                                      if(conf):
                                                      
                                                            try:      
                                                                  coll.delete_one({'id':getEmpId.get()})
                                                                
                                                                  destroyImage()                                                                 
                                                                  clearFields()
                                                                  getid.set('')

                                                                  return messagebox.showinfo(title="success",message="Emp Deleted succesfully")
                                                            except:
                                                                  return messagebox.showinfo(title="internal Error",message="Internal Error may be DB connection Error")
                                          else:
                                                return messagebox.showerror(title="Empty id",message="Please first fetch data(user) then Delete")                                                                                                                                                              
            
                                    Button(em,text='Delete',justify='center',command=deleteData,width=13,height=1,borderwidth=4,relief='raised',font=('',10,'bold')).place(y=450,x=100)


                                    

                                    # Fetch All Employees form DB
                                    def fetchAllData():

                                          # new Window
                                          top = Toplevel()

                                          #heading 
                                          Label(top,text="Data Fillter",font=('',10,'bold')).place(y=10,x=550)
                                          
                                          # Filtters

                                          # 1) Blood Group
                                          getBloodGroup = StringVar()
                                          getBloodGroup.set('select')
                                          Label(top,text="Blood Group",font=('',10),fg='black').place(y=50,x=58)
                                          bloodGroup = ttk.Combobox(top,width=10,textvariable=getBloodGroup,font=('',10),background='white')
                                          bloodGroup['state']='readonly'
                                          bloodGroup['values']=('A+','A-','B+','B-','O+','O-','AB+','AB-')
                                          bloodGroup.place(y=70,x=50)

                                           # 2) Gender 
                                          getGender = StringVar()
                                          getGender.set('select')
                                          Label(top,text="Gender ",font=('',10),fg='black').place(y=50,x=220)
                                          gender = ttk.Combobox(top,width=10,textvariable=getGender,font=('',10),background='white')
                                          gender['state']='readonly'
                                          gender['values']=('Male','Female')
                                          gender.place(y=70,x=200) 

                                          # 3) Country
                                          getCountry = StringVar()
                                          getCountry.set('select')
                                          Label(top,text="Country",font=('',10),fg='black').place(y=50,x=372)
                                          country = ttk.Combobox(top,width=10,textvariable=getCountry,font=('',10),background='white')
                                          country['state']='readonly'
                                          country['values']=('United States','China','Japan','United Kingdom','India','France','Canada','Other')
                                          country.place(y=70,x=350)
                                    
                                          # 4) Designation 
                                          getDesignition = StringVar()
                                          getDesignition.set('select')
                                          Label(top,text="Designition",font=('',10),fg='black').place(y=50,x=530)
                                          designition = ttk.Combobox(top,width=15,textvariable=getDesignition,font=('',10),background='white')
                                          designition['state']='readonly'
                                          designition['values']=('Software Developer','Software Tester','UI Designer','Project Manager','HR Manager','Business Analyst','Systems Administrator','Account Manager',)
                                          designition.place(y=70,x=500)
                                         
                                          # 5) Employeement Type
                                          getEmployeetype = StringVar()
                                          getEmployeetype.set('select')
                                          Label(top,text="Emp Type",font=('',10),fg='black').place(y=50,x=705)
                                          employeeType = ttk.Combobox(top,width=10,textvariable=getEmployeetype,font=('',10),background='white')
                                          employeeType['state']='readonly'
                                          employeeType['values']=('Full Time','Part Time','Intership','Contract ')
                                          employeeType.place(y=70,x=690)

                                          # 6) Department Name
                                          getDepartmentName = StringVar()
                                          getDepartmentName.set('select')
                                          Label(top,text="Department",font=('',10),fg='black').place(y=50,x=870)
                                          departmentName = ttk.Combobox(top,width=15,textvariable=getDepartmentName,font=('',10),background='white')
                                          departmentName['state']='readonly'
                                          departmentName['values']=('Software Development','Quality Assurance (QA)','Technical Support','Project Management','Sales and Marketing','Human Resources (HR)','Finance and Accounting','Research and Development')
                                          departmentName.place(y=70,x=840)
                                          
                                          # 7) salary(CTC)
                                          getSalary = StringVar()
                                          getSalary.set('')
                                          Label(top,text="Salary (CTC) ",font=('',10),fg='black').place(y=50,x=1070)
                                          salary = Entry(top,width=10,textvariable=getSalary,font=('',10),bd='1px',justify='center',background='white').place(y=71,x=1120)

                                          getCondition = StringVar()
                                          getCondition.set('select')
                                          condition = ttk.Combobox(top,width=10,textvariable=getCondition,font=('',10),background='white')
                                          condition['state']='readonly'
                                          condition['values']=('Equel ==','Less <','Greater >')
                                          condition.place(y=70,x=1030)



                                          # Clear All Filter Fields
                                          def clearFiltterFields():
                                                getBloodGroup.set('select')
                                                getGender.set('select')
                                                getCountry.set('select')
                                                getDesignition.set('select')
                                                getEmployeetype.set('select')
                                                getDepartmentName.set('select')
                                                getSalary.set('')
                                                getCondition.set('select')

                                          
                                          # Heading for show filltered Data  ** back color
                                          Label(top,text="Id",width=10,font=('',12),justify='center',height=2,background='gray').place(y=200,x=5)
                                          Label(top,text="name",width=20,font=('',12),justify='center',height=2,background='gray').place(y=200,x=100)
                                          Label(top,text="Blood",width=10,font=('',12),justify='center',height=2,background='gray').place(y=200,x=285)
                                          Label(top,text="Department",width=23,font=('',12),justify='center',height=2,background='gray').place(y=200,x=380)
                                          Label(top,text="Designition",width=19,font=('',12),justify='center',height=2,background='gray').place(y=200,x=593)
                                          Label(top,text="Emp Type",width=12,font=('',12),justify='center',height=2,background='gray').place(y=200,x=769)
                                          Label(top,text="Salary",width=12,font=('',12),justify='center',height=2,background='gray').place(y=200,x=882)
                                          Label(top,text="Country",width=15,font=('',12),justify='center',height=2,background='gray').place(y=200,x=995)
                                          Label(top,text="Phone No",width=14,font=('',12),justify='center',height=2,background='gray').place(y=200,x=1135)


                                          def dataFillter():                                    
                                               
                                               # I'm Created Good Logic to destroy Widgets
                                                i =0
                                                for widget in top.winfo_children():
                                                      if(i < 27):
                                                            pass
                                                      else:
                                                            widget.destroy()
                                                      i = i+1

                                                salaryDict = dict()                                                                                                                                                                                                             
                              
                                                if(getCondition.get() != 'select' ):
                                                      if(getSalary.get() != ''):
                                                            try:
                                                                  intSalary = getSalary.get()
                                                                  intSalary = int(intSalary)
                                                            except:
                                                                  return messagebox.showerror(title="not intiger Value",parent=top,message="Please Eneter Ientiger Value")
                                                                                                                   

                                                            if(getCondition.get() == 'Equel =='):
                                                                 salaryDict = {'$eq':intSalary}
                                                            
                                                            if(getCondition.get() == 'Less <'):
                                                                  salaryDict = {'$lt':intSalary}

                                                            if(getCondition.get() == 'Greater >'):
                                                                  salaryDict = {'$gt':intSalary}

                                                      else:
                                                            return messagebox.showerror(title="Not entered salary",message="Please Enter Salary your selected salary condition but not Entered Salary  Amol Shinde",parent=top)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                # Make Query
                                                query = {'bloodGroup':getBloodGroup.get(),'gender':getGender.get(),'country':getCountry.get(), \
                                                         'designition':getDesignition.get(), 'employeeType':getEmployeetype .get(),'departmentName':getDepartmentName.get(),'salary':salaryDict}
                                                
                                                # Remove Empty fields

                                                if(query['bloodGroup'] == 'select'):
                                                       del query['bloodGroup']
                                                
                                                if(query['gender'] == 'select'):
                                                       del query['gender']

                                                if(query['country'] == 'select'):
                                                       del query['country']

                                                if(query['designition'] == 'select'):
                                                       del query['designition']

                                                if(query['employeeType'] == 'select'):
                                                       del query['employeeType']
                                                       
                                                if(query['departmentName'] == 'select'):
                                                       del query['departmentName']

                                                if(query['salary'] == {} ):
                                                       del query['salary']
                                                                                                                                                
                                                # counting how many documents found through this query
                                                totalDocument = coll.count_documents(query) 
                                                Label(top,text=f"Found Recoreds : {totalDocument}",width=20,font=('',13)).place(y=150,x=5)

                                                # show Message if data not found according to query
                                                if(totalDocument == 0):
                                                      Label(top,text=f"Sorry ! Recored not found...",width=30,font=('',13,'bold')).place(y=350,x=450)                                                                                                    
                                                
                                                try:
                                                      allData = coll.find(query).sort('id',pymongo.ASCENDING) #sort('id',pymongo.ASCENDING) for data show in asecnding order                                                    
                                                      v = 250
                                                      h = 0
                                                      for e in allData:                                                
                                                            id = Label(top,text=e['id'],width=10,font=('',11),background='pink').place(y=v,x=h+5)
                                                            Label(top,text=e['name'],width=20,font=('',11),background='orange').place(y=v,x=h+100)
                                                            Label(top,text=e['bloodGroup'],width=10,font=('',11),background='pink').place(y=v,x=h+285)
                                                            Label(top,text=e['departmentName'],width=23,font=('',11),background='orange').place(y=v,x=h+380)
                                                            Label(top,text=e['designition'],width=19,font=('',11),background='pink').place(y=v,x=h+593)
                                                            Label(top,text=e['employeeType'],width=12,font=('',11),background='orange').place(y=v,x=h+769)
                                                            Label(top,text=e['salary'],width=12,font=('',11),background='pink').place(y=v,x=h+882)
                                                            Label(top,text=e['country'],width=15, font=('',11),background='orange').place(y=v,x=h+995)
                                                            Label(top,text=e['phone_no'],width=14,font=('',11),background='pink').place(y=v,x=h+1135)

                                                            v = v + 25 

                                                except:
                                                      messagebox.showerror(title="DB Error",message="Sorry ! DB connection or query error",parent=top)
                                                                              
                                                
                                          Button(top,text='Fillter Data...',justify='center',command=dataFillter,width=20,height=1,borderwidth=4,relief='raised',font=('',10,'bold')).place(y=120,x=365)

                                          # Reset Button
                                          Button(top,text='Reset',justify='center',command=clearFiltterFields,width=15,height=1,borderwidth=4,relief='raised',font=('',10,'bold')).place(y=120,x=720)

                                          # If clicked on Fetch All Data button that time show all recoreds of DB
                                          dataFillter()

                                          # Display Size 
                                          top.geometry('1920x1080')
                                          top.maxsize(width=1280,height=650)
                                          top.minsize(width=1280,height=650)

                                          top.mainloop()
                                                                         
                                    Button(em,text='Fetch All Data',justify='center',command=fetchAllData,width=13,height=1,borderwidth=4,relief='raised',font=('',10,'bold')).place(y=450,x=975)
                                                                  
                                    em.mainloop()
           
                  # Registration Admin & Employee
                  def registrationAdminAnEmp():
                        for widget in em.winfo_children():
                              widget.destroy()

                        # Heading Registration 
                        heading = Label(em,text="Registration Form",font=('',15,'bold'),justify='center').place(y=40,x=550)

                        # User Name
                        getUserName =StringVar()
                        Label(em,text="User Name:",font=('',10),fg='black').place(y=100,x=450)
                        username = Entry(em,width=30,textvariable=getUserName,font=('',10),bd='1px',background='white').place(y=100,x=550)

                        # Email Id
                        getEmpId =StringVar()
                        Label(em,text="Emp Id:",font=('',10),fg='black').place(y=140,x=450)
                        EmpId = Entry(em,width=30,textvariable=getEmpId,font=('',10),bd='1px',background='white',state='readonly')
                        EmpId.place(y=140,x=550)

                        # Roll
                        getRoll = StringVar()
                        getRoll.set('Select Roll')
                        Label(em,text="User Roll:",font=('',10),fg='black').place(y=180,x=450)
                        roll = ttk.Combobox(em,width=15,textvariable=getRoll,font=('',10),background='white')
                        roll['state']='readonly'
                        roll['values']=('Admin','Employee')
                        roll.place(y=180,x=550)

                        # Password
                        getPassword =StringVar()
                        Label(em,text="Password :",font=('',10),fg='black').place(y=220,x=450)
                        password = Entry(em,width=30,textvariable=getPassword,font=('',10),bd='1px',background='white').place(y=220,x=550)

                        # confirm Password
                        getconfPassowrd =StringVar()
                        Label(em,text="Re-Passowrd :",font=('',10),fg='black').place(y=260,x=450)
                        confPassword = Entry(em,width=30,textvariable=getconfPassowrd,font=('',10),bd='1px',background='white').place(y=260,x=550)

                         # Generate Uniqe EmpId
                        try:
                              def generetEmpId():
                                    randId = random.randrange(100,1000)
                                    randId = str(randId)
                                    EmpDetail = coll.find()
                                    for e in EmpDetail:                                       
                                          if(e['id'] == randId):
                                                generetEmpId()
                                                break
                                          else:
                                                getEmpId.set(randId)
                              generetEmpId()
                        except:
                              return   messagebox.showerror(title="end limit",message="All Id genereted 100 to 999 not found unique id so conacat to developer and increge limit make 4 digit id ")
                                     
                        # Validating Data
                        def registValidData(): 

                              # UserName
                              nameLenValid = len(getUserName.get())
                              if( nameLenValid < 5):
                                    return   messagebox.showinfo(title="Error",message="please Enter Name At least 5 char")
                              if(nameLenValid > 30):
                                    return   messagebox.showinfo(title="Error",message="not allow above 30 char in Name")
                                                                                                                                                                                          
                              # Roll 
                              rollValid = getRoll.get()
                              if(rollValid == ''):
                                    return   messagebox.showinfo(title="Error",message="Please Select Roll")
                  
                              # Password
                              passwordValid = len(getPassword.get())
                              if(passwordValid < 8):
                                    return   messagebox.showinfo(title="Error",message="Please Enter Strong Password")
                              if(passwordValid > 16):
                                    return   messagebox.showinfo(title="Error",message="Maxmimum 16 characters Allowed check Pssword lenght")
                  
                              # confirm passowrd
                              if(getPassword.get() != getconfPassowrd.get()):
                                    return   messagebox.showinfo(title="Error",message="conf Password and password not matched please check")
                                                                                                      
                              # Inert Data in DB
                              try:
                                    collReg.insert_one({
                                                'userName':getUserName.get(),
                                                'empId':getEmpId.get(),
                                                'roll':getRoll.get(),
                                                'password':getPassword.get()
                                          })
                              except:
                                    return   messagebox.showerror(title="Error",message="Sorry ! User Not Register Internal Problem may be DB connection problem")
                            
                              if(getRoll.get() == 'Admin'):
                                    return fun(0)
                              else:
                                    return   messagebox.showinfo(title="Register success",message="Employee register successfully NOTE :- note Emp ID ")
                                                                                     
                        # Sing Up Button
                        Button(em,text='Sing Up',font=('',11),fg='black',justify='center',width=15,command=registValidData).place(y=320,x=550)
                                                     
                        # Drawing Horizontal Line 
                        hLine = Canvas(em,width=100,height=100)
                        hLine.place(y=500,x=100)
                        hLine.create_line(50,100,500,100)
                        em.mainloop()                                                                                 
                
                  # Screen Size 
                  em.geometry('1920x1080')
                  em.maxsize(width=1280,height=650)
                  em.minsize(width=1280,height=650)

                  Label(em,text="Employee Management System",font=('',15,'bold'),fg='black').place(y=10,x=500)
                  Label(em,text="New Employee ? ",font=('',10),fg='black').place(y=350,x=570)

                  # shows created by Amol shinde
                  Label(em,text="Created By :",font=('',8),fg='black').place(y=10,x=5)
                  Label(em,text=" Amol Shinde",font=('',10),fg='black',justify='left').place(y=10,x=70)

                  # Login Heading
                  heading = Label(em,text="Login Form",font=('',12,'bold'),justify='center').place(y=80,x=550)

                  # user Name
                  getUserName =StringVar()
                  Label(em,text="User Name:",font=('',10),fg='black').place(y=140,x=450)
                  username = Entry(em,width=30,textvariable=getUserName,font=('',10),bd='1px',background='white').place(y=140,x=550)

                  # Password
                  getPassword =StringVar()
                  Label(em,text="Password :",font=('',10),fg='black').place(y=180,x=450)
                  password = Entry(em,width=30,textvariable=getPassword,font=('',10),bd='1px',background='white').place(y=180,x=550)

                  # Roll
                  getRoll = StringVar()
                  getRoll.set('Select Roll')
                  Label(em,text="User Roll:",font=('',10),fg='black').place(y=220,x=450)
                  roll = ttk.Combobox(em,width=15,textvariable=getRoll,font=('',10),background='white')
                  roll['state']='readonly'
                  roll['values']=('Admin','Employee')
                  roll.place(y=220,x=550)


                  # Fetching Data from DB using Id - above login Data Match in DB, user valid show Data otherwise show Error Message
                  def loginMatchData():
                        userNameValid = getUserName.get()
                        if(userNameValid == ''):
                              return   messagebox.showinfo(title="Error",message="Please Enter User Name")
                        
                        password = getPassword.get()
                        if(password == ''):
                              return   messagebox.showinfo(title="Error",message="Please Enter Password")
                        
                        roll = getRoll.get()
                        if(roll == ''):
                              return   messagebox.showinfo(title="Error",message="Please Select Roll")
                        
                        allData=collReg.find()
                        for e in allData:

                              if(userNameValid == e['userName'] and password == e['password'] and roll == e['roll'] ):

                                    if(e['roll']  == 'Employee'):
                                          empId = e['empId']
                                          return fun(empId)
                                    
                                    if(e['roll']  == 'Admin'):
                                          return fun(0)
                        else:
                              messagebox.showerror(title="Invalid User",message="Invalid User ! not Machted Given Data")

                  # Login and Sing-up in Button
                  Button(em,text='Login',font=('',11),fg='black',justify='center',width=15,command=loginMatchData).place(y=280,x=550)
                  Button(em,text='Sing Up',font=('',11),fg='black',justify='center',width=15,command=registrationAdminAnEmp).place(y=380,x=550)
                  
                  # Screen Size 
                  em.geometry('1920x1080')
                  em.maxsize(width=1280,height=650)
                  em.minsize(width=1280,height=650)

                  # main loop
                  em.mainloop()  

obj = Employee()
obj.loginAdminAnEmp()


# Project Completed 
# Thank You 

# Once a task is just begun, never leave it till it's done. 
# Be the labor great or small, do it well or not at all
