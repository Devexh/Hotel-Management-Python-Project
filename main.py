import csv #importing csv module
import math 
import os
import datetime  #importing datetime module
def ShowMenu(): #to show the menu of the hotel
          print()
          print('+'*40 ,'WELCOME TO HOTEL GENEVA', '+'*45)
          print("\t 1. CHECK-IN ")
          print("\t 2. CHECK-OUT ")
          print("\t 3. ALL ROOM STATUS ")
          print("\t 4. OTHER EXPENSES ")
          print("\t 5. ROOM ENQUIRY ")
          print("\t 6. VISITORS LIST")
          print("\t 0. LOG OUT ")
          print('+'*108)
          print()
def ShowAllRoomStatus(): #user defined module to show the status of all room provided by the hotel
          with open('rooms.csv','r') as csvfile:
                    myreader = csv.reader(csvfile)
                    print("="*78)
                    print("FLOOR\t","ROOM NUMBER\t","ROOM TYPE\t","ROOM STATUS\t",'RATE')
                    print("="*78)
                    for row in myreader:
                              if row[2]=="D":
                                        rtype="PURE-DELUXE"
                              elif row[2]=="SD":
                                        rtype="SEMI-DELUXE"
                              elif row[2]=="SDX":
                                        rtype="SUPER DELUXE"
                              elif row[2]=="E":
                                        rtype="EXECUTIVE"
                              if row[3]=="V":
                                        status="  VACANT"
                              else:
                                        status ="OCCUPIED"
                              print(row[0],'\t',row[1],'\t\t',rtype,'\t',status,'\t',row[4]+' INR')
                    print("="*78)
          input('Press any key to continue...')
def CheckRoomVacant(roomno): #user defined module to display the vacancy of the room
          with open('rooms.csv','r') as csvfile:
                    myreader = csv.reader(csvfile)
                    found=False
                    for row in myreader:
                              if len(row)>0:
                                        if str(row[1])==str(roomno):
                                                  found=True
                                                  return row[3],row[4]
                    if not found:
                              return 'INVALID!'
                    
          input('Press any key...')         
def CheckIn(): #User defined module to checkin
          print('\n\n','='*43,'NEW VISITOR ARRIVAL','='*40)
          Visitor_Number=None
          if os.path.exists('Visitor.csv'):
                    with open('Visitor.csv','r') as csvfile:
                              myreader = csv.reader(csvfile)
                              l = len(list(myreader))
                              Visitor_Number = l + 1                        
          else:
                    Visitor_Number = 1
          dt = datetime.datetime.now()
          today = str(dt.day)+'/'+str(dt.month)+'/'+str(dt.year)+' '+str(dt.hour)+':'+str(dt.minute)+':'+str(dt.second)
          print('\n\t\t\t\t\t\t\t\t\t Today is: '+today)
          print('\t Visitor Number:',Visitor_Number)
          print()
          name = input('\tEnter Visitor Name :')
          TV = int(input('\tEnter Total Members:'))
          age = int(input('\tEnter Age :'))
          gender = input('\tChoose gender 1(Male), 2(Female):')
          coming_from = input('\tEnter the Place from where person is coming:')
          purpose = input('\tEnter purpose of Visit:')
          mobile = int(input('\tEnter Mobile Number:'))
          c='go'
          roomno=0
          while c=='go':
                    roomno = int(input('\tEnter Room Number :'))
                    status = CheckRoomVacant(roomno)
                    if status[0]=='INVALID!':
                              print('Enter Valid Room Number:')
                    elif status[0]=='V':
                              c='OK'
                    else:
                              print('The Selected Room Number is not Vacant!')
          print('='*110)
          print('\t\t\tCheck in Date & Time: ',today)
          print('\t\t\tRoom Rent @'+str(status[1])+'/Day')
          print('\t\t\tAdvance To Pay: '+str(status[1]))
          ans = input('\n\t\t\tDo you want to confirm your booking?(y/n):')
          if ans.lower()=='y':
                    visitors=[Visitor_Number,name,TV,age,gender,coming_from,purpose,roomno,today,status[1],mobile]
                    with open('Visitor.csv','a') as vfile:
                              mywriter = csv.writer(vfile,lineterminator='\n')
                              mywriter.writerow(visitors)
                    print('\n\t\t\t Checked In Successfully!')
                    room=[]
                    with open('rooms.csv','r') as rcsv:
                              myreader = csv.reader(rcsv)
                              for row in myreader:
                                        if len(row)>0:
                                                  room.append(row)
                                                  #print(row)

                    with open('rooms.csv','w') as rcsv:
                              mywriter = csv.writer(rcsv,lineterminator='\n')
                              for i in range(len(list(room))):
                                        if room[i][1]==str(roomno):
                                                  room[i][3]='O'
                                        #print(room[i])
                                        mywriter.writerow(room[i])
def OtherExpense(): #User defined module for other expense by the customer
          print("="*30," OTHER EXPENSE SCREEN ", "="*30)
          visitors=[]
          with open('Visitor.csv','r') as csvroom:
                    myreader = csv.reader(csvroom)
                    for row in myreader:
                              visitors.append(row)
          vno = input('\n\t\t ENTER VISITOR ID/NO :')
          found=False
          for rs in visitors:
                    if rs[0]==vno:
                              print()
                              print('='*55)
                              print("DISH/DESSERTS\t","THEME\t\t\t","PRICE")
                              print('='*55)
                              with open('food.csv','r') as csvfood:
                                  myreader = csv.reader(csvfood)
                                  for r in myreader:
                                      print(r[0],'\t',r[1],'\t\t',r[2])
                              print('='*55)
                              print()
                              food = int(input('Enter Food Expense (0 if no expense):'))
                              print()
                              print('='*53)
                              print("Dress/Material\t","Laundry\t","D.Clean\t","Press\t",'Total')
                              print('='*53)
                              with open('laundry.csv','r') as csvlaundry:
                                  myreader = csv.reader(csvlaundry)
                                  for r in myreader:
                                      print(r[0],'\t',r[1],'\t',r[2],'\t',r[3],'\t',r[4])
                              print('='*53)
                              print()
                              laundry = int(input('Enter Laundry Expense (0 if no expense) :'))
                              print()
                              print('='*37)
                              print("ENTMT Centres\t\t","PRICE")
                              print('='*37)
                              with open('misc.csv','r') as csvmisc:
                                  myreader = csv.reader(csvmisc)
                                  for r in myreader:
                                      print(r[0],'\t\t',r[1])
                              print('='*37)
                              print()
                              misc = int(input('Enter any other expense (0 if no expense) :'))
                              with open('expense.csv','a') as expcsv:
                                        mywriter = csv.writer(expcsv,lineterminator='\n')
                                        today = datetime.datetime.now()
                                        today = str(today.day)+'/'+str(today.month)+'/'+str(today.year)
                                        exp = [vno,food,laundry,misc,today]
                                        mywriter.writerow(exp)
                              found=True
          if not found:
                    print("\n### SORRY ROOM NUMBER NOT OCCUPIED ###")
def CheckOut(): #User defined module to checkout from the hotel
          print('\n\n')
          print('='*44,' CHECK OUT SCREEN ' , '='*40)
          roomstatus=[]
          with open('rooms.csv','r') as csvroom:
                    myreader = csv.reader(csvroom)
                    for row in myreader:
                              roomstatus.append(row)
          rno = input('\n\tENTER ROOM NO :')
          found=False
          vis=[]
          fexp=0
          lexp=0
          mexp=0
          total=0
          oexp=0
          for rs in roomstatus:                    
                    if rs[1]==rno and rs[3]=='O':
                              total=total + int(rs[4])
                              print('Checking for the details of the Visitor....')
                              with open('Visitor.csv','r') as vcsv:
                                        myreader = csv.reader(vcsv)
                                        for row in myreader:
                                                  if rno == row[7]:
                                                            vis = row
                                                            print(vis[0])
                                                            print("Checked Successfully!")
                              
                              with open('expense.csv','r') as ecsv:
                                        myreader = csv.reader(ecsv)
                                        for row in myreader:
                                                  if row[0] == vis[0]:
                                                            fexp = fexp + int(row[1])
                                                            lexp = lexp + int(row[2])
                                                            mexp = mexp + int(row[3])
                                                  '''else:
                                                      fexp=0;lexp=0;mexp=0'''
                              oexp = fexp + lexp + mexp
                              found=True
          if not found:
                    print('\t\t\tTHE ROOM IS NOT BOOKED')
          else:
                    today = datetime.datetime.now()
                    today = str(today.day)+'/'+str(today.month)+'/'+str(today.year)+' '+str(today.hour)+':'+str(today.minute)+':'+str(today.second)
                    print('\n\n')
                    print('='*44,'CHECK OUT (BILL)','='*40)
                    print()
                    print('\t\t\t\t CHECK IN DATE : ',vis[8])
                    print('\t\t\t\t CHECK OUT DATE :',today)
                    print('-'*110)
                    print('\t\tVISITOR DETAILS:')
                    print()
                    print('\t\t\t\t Visitor Number : ',vis[0])
                    print('\t\t\t\t Visitor Name    : ',vis[1])
                    print('\t\t\t\t Visitor Age        : ',vis[3])
                    g=''
                    if vis[4]=='1':
                              g='Male'
                    else:
                              g='Female'
                              
                    print('\t\t\t\t Visitor Gender   : ',g)
                    
                    print('\t\t\t\t Coming From     : ',vis[5])
                    print('\t\t\t\t Purpose of Visit  : ',vis[6])
                    print('-'*110)

                    d1 = datetime.datetime.strptime(vis[8],"%d/%m/%Y %H:%M:%S")
                    d2 = datetime.datetime.strptime(today,"%d/%m/%Y %H:%M:%S")
                    d3 = d2-d1
                    day=0
                    if d3.days<=1:
                              day=1
                    else:
                              day = math.ceil(d3.days)
                    print('\t\tEXPENSE DETAILS:')
                    print('\n\t\t\t\t Total days          :',day)
                    print('\t\t\t\t Room Rent         :Rs.',total*day)
                    print('\t\t\t\t Food Expense        :Rs.',fexp)
                    print('\t\t\t\t Laundry Expense     :Rs.',lexp)
                    print('\t\t\t\t Misc. Expense       :Rs.',mexp)
                    print('-'*110)
                    print('\t\t\t\t GRAND TOTAL : Rs.',(total+oexp))
                    print('='*110)
                    print()
                    room=[]
                    with open('rooms.csv','r') as rcsv:
                              myreader = csv.reader(rcsv)
                              for row in myreader:
                                        if len(row)>0:
                                                  room.append(row)
                                                  #print(row)

                    with open('rooms.csv','w') as rcsv:
                              mywriter = csv.writer(rcsv,lineterminator='\n')
                              for i in range(len(list(room))):
                                        if room[i][1]==str(rno):
                                                  room[i][3]='V'
                                        #print(room[i])
                                        mywriter.writerow(room[i])

                    with open('vis.csv','a') as wcsv:
                             mywriter = csv.writer(wcsv,lineterminator='\n')
                             vi = [vis[0],vis[1],vis[2],vis[3],vis[4],vis[5],vis[6],vis[7],vis[8],total+oexp,vis[9],vis[10]]
                             mywriter.writerow(vi)

                                                 
def RoomEnquiry(): #User defined module for Enquiry of room
          print('\n\n')
          print('='*30,' VISITOR ENQUIRY SCREEN ' , '='*30)
          vn = input("\n\t\t ENTER VISITOR NAME : ")
          print()
          print("="*113)
          print("VID\t","VISITOR NAME\t","AGE\t","GENDER\t","CAME FROM\t","PURPOSE\t","ROOMNO\t","CHECKIN DATE\t")
          print("="*113)
          found=False
          gender=''
          with open('Visitor.csv','r') as vcsv:
                    myreader = csv.reader(vcsv)
                    for row in myreader:
                              if row[1].lower()==vn.lower():
                                        if row[4]=='1':
                                                  gender='Male'
                                        else:
                                                  gender='Female'
                                        print(row[0],'\t',row[1],'\t',row[3],'\t',gender,'\t',row[5],'\t',row[6],'\t\t',row[7],'\t',row[8])
                                        found=True
          print("="*113)
          if not found:
                    print("\n\t\t\t VISITOR NAME NOT FOUND ")
def VisList(): #User defined module to display the visitor's list
    print()
    print('='*120)
    print("VID\t","VISITOR NAME\t","AGE\t","CAME FROM\t","ROOMNO\t","CHECKIN DATE\t","EXPENSES\t","M.NO")
    print('='*120)
    with open('vis.csv','r') as csvis:
        myreader = csv.reader(csvis)
        for r in myreader:
            print(r[0],'\t',r[1],'\t',r[3],'\t',r[5],'\t',r[7],'\t',r[8],'\t',r[9],'\t\t',r[11])
    print('='*120)
choice=0
while choice!=None:
          ShowMenu()
          choice = int(input('\t\t\t\t\tENTER YOUR CHOICE :'))
          if choice==1:
                    CheckIn()
          elif choice==2:
                    CheckOut()
          elif choice==3:
                    ShowAllRoomStatus()
          elif choice==4:
                    OtherExpense()
          elif choice==5:
                    RoomEnquiry()
          elif choice==6:
                    VisList()
          elif choice==0:
                    choice=None
                    print('LOGGED OUT SUCCESSFULLY!')
          else:
                    print('\n\t\t\t ~~~~~~~~ERROR: INVALID CHOICE!~~~~~~~~')
          
