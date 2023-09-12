import csv
misc=[
          ['Video GameZone',1000],
          ['Billiards & Carrom ',2000],
          ['Bar & Grill',2500],
          ['CinematoFlix',1700]]

           
with open('misc.csv',mode='w') as csvfile:
          mywriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
          for r in misc:
                    mywriter.writerow(r)
