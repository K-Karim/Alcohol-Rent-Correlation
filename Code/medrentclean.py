#Karim Khairat
#This was made specifically for alcohol.csv and will not work correctly with other files!
# Removes all dates other than Dec 2011 (corresponds to Alcohol csv)
import csv

#Open and transpose file
inpt= 'Medrent.csv'
csvopen= open( inpt,"r") 
medrent= csv.reader(csvopen)
medrentT= list(zip(*medrent))

#create new file (Or overwrite if already created)
output = open("MedrentC.csv",'w')

#store LGA name, number of surveyed prices(count), median rent
namelist = []
count = []
rent = []
counter= 0
for i in range(len(medrentT)):

	#grabs LGA names
	if i == 0:
		namelist = medrentT[i]

	#grabs med rent and count for dec 2011 :) 
	elif "Dec 2011" in medrentT[i]:

		#if there's a comma strip it to avoid number splitting into multiple cells
		for cell in medrentT[i]:
		
			if  ',' in cell:
				count.append(cell.replace(',',''))
			elif '-' in cell:
				count.append(cell.replace('-','0'))

			#otherwise just copy cell over
			else:
				count.append(cell)
		#iterate over median cost column to copy into rent list, if no data use average group number
		for cell2 in medrentT[i+1]:
			j=0
			if '-' in cell2:
				while medrentT[0][counter+j] != 'Group Total':
					j+=1
					
				rent.append(cell2.replace('-',medrentT[i+1][counter+j]))
			else:
				rent.append(cell2)
			counter+=1

			
#combine together into an array and transpose it to original format
listy = [namelist, count, rent]
listy = zip(*listy)
#write to file :) 
for row in listy:
	for column in row:
		output.write('{},'.format(column))
	output.write('\n')
output.close()
