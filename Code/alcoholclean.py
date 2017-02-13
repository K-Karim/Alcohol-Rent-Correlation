#Karim Khairat
#clean Alcohol CSV
#This was made specifically for alcohol.csv and will not work correctly with other files
import csv 

inptA= 'Alcohol.csv' 
csvopen= open( inptA,"r") 
alcohol= csv.reader(csvopen)
alcoholT= list(zip(*alcohol)) #transpose to make it easier to iterate over

#create new file to output to 
output= open("AlcoholC.csv", 'w')

Name=[]
local_avg=[]
vic_ave=[]

#iterate, find and keep only what is needed
for i in range(len(alcoholT)):
	if "lga_name06" in alcoholT[i]:
		Name = alcoholT[i]
	elif"numeric" in alcoholT[i]:
		local_avg = alcoholT[i]
	elif"vic_ave" in alcoholT[i]:
		vic_ave= alcoholT[i]

#place them in order of desired appearance
listy = [Name, local_avg, vic_ave]
listy= zip(*listy) #transpose back to original format


#write to AlcoholC (Alcohol Clean)
for row in listy:
	for column in row:
		output.write('{},'.format(column))
	output.write('\n')
output.close()
