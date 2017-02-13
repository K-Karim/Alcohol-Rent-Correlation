#KARIM KHAIRAT
#Combines the cleaned Alcohol and Median Rent CSVs

import csv

#open and transpose files
inpt2= 'AlcoholC.csv'
csvopen1= open( inpt2,"r") 
alcohol= csv.reader(csvopen1)
alcoholT= list(zip(*alcohol))

inpt1= 'MedrentCleaner.csv'
csvopen1= open( inpt1,"r") 
medrent= csv.reader(csvopen1)
medrentT= list(zip(*medrent))

#create output file
output = open("combined.csv",'w')


LGA = []
alcohol_buy = []
vicave = []
rent = [] 

#Alcohol column copy over
for i in range(len(alcoholT)):
	
	if"numeric" in alcoholT[i]:
		alcohol_buy = alcoholT[i]
	elif"vic_ave" in alcoholT[i]:
		vicave= alcoholT[i]
#Median Rent column copy over.
for i in range(len(medrentT)):
	if i == 0:
		LGA = medrentT[i][1:]

	elif i== 2:
		rent = medrentT[i][1:]

#place elements into list in order of column.
listy = [LGA, rent, alcohol_buy, vicave]
listy = zip(*listy) 

#write to combined
for row in listy:
	for column in row:
		output.write('{},'.format(column))
	output.write('\n')
output.close()
