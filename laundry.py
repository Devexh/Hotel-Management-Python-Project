import csv
laundry=[
          ['Shirt/Blouse',246,291,195,732],
          ['Trousers/Jeans',237,316,171,724],
          ['Saree(Silk/Cotton)',307,375,190,872],
          ['Suit / Blazer',0,525,315,840],
          ['Short/ Hot Pant',145,125,75,345],
          ['Skirt / Frock',205,200,160,565],
          ['Socks/Stockings',72,0,0,72]]
          
          
          
with open('laundry.csv',mode='w') as csvfile:
          mywriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
          for r in laundry:
                    mywriter.writerow(r)
