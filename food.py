import csv
food=[
          ['Vegan Thali','Spicy Hot',340],
          ['NonVeg Thali','Spicy Chilli',450],
          ['South Thali','Spicy/Sour',420],
          ['Maharaja Thali','Spicy Chilli',670],
          ['Lemon Tart','Sour/Sweet',190],
          ['Belgian Waffle','Sweet Sugared',230],
          ['JellyOroll','Sweet Candied',200],
          ['CreamOIce','Sweet Sugared',240],
          ['Aqua Vitae','Sour/Sweet',170]]

           
with open('food.csv',mode='w') as csvfile:
          mywriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
          for r in food:
                    mywriter.writerow(r)
