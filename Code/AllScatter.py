#Karim Khairat
#Create scatter plot for all regions. 

import matplotlib.pyplot as plt #mpl used for plotting
import csv

#open and read file

#insert region name below
region= 'INSERT REGION HERE'

regions = ['BSW', 'EasternMetro', 'Gippsland', 'Grampians', 'Hume', 'LoddonMallee', 'NWMetro','SouthernMetro']
for region in regions:	
	inpt= region+'.csv'
	csvopen= open( inpt,"r") 
	area= csv.reader(csvopen)
	areaT= list(zip(*area))

	#counter to help append
	counter =0

	#create lists to store variables
	medianlist=[]
	alcohollist=[]

	#loop and find all variables
	for i in range(len(areaT)):
	    for cell in areaT[i]:
		if i == 1:
		    medianlist.append(int(cell.replace('$','')))
		elif i == 2:
		    alcohollist.append(float(cell))
		    
	#ploting adapted from Joe Kington's answer at:
	#http://stackoverflow.com/questions/7376330/axis-range-in-scatter-graphs

	fig, something=plt.subplots()
	something.set_title("Alcohol/Price Southern Metro")
	something.set_xlabel("Median Price by LGA")
	something.set_ylabel("Alcohol consumption")
	something.grid(True,linestyle='-')
	something.plot(medianlist,alcohollist,'o')
	fig.savefig('scatter' + region + '.png', dpi=100)
	csvopen.close()
