#Karim Khairat
#Creates a Greater Areas only csv
import csv

inpt1= 'LGAPRICES.csv'
csvopen1= open( inpt1,"r") 
orig_prices= csv.reader(csvopen1)
orig_pricesT= list(zip(*orig_prices))

#Open and transpose file
inpt= 'combined.csv'
csvopen= open( inpt,"r") 
comb= csv.reader(csvopen)
combT= list(zip(*comb))

#Greater Area names
AREAS = ['Barwon_SW', 'Grampians','Loddon_Mallee','Hume','Gippsland','North_and_West_Metro','Eastern_Metro','Southern_Metro']

#lists for greater areas.
Barwon_SW = []
Grampians = [] 
Loddon_Mallee = []
Hume = []
Gippsland = []
North_and_West_Metro = []
Eastern_Metro=[]
Southern_Metro =[]
#LGA prices for the Greater areas
Barwon_SW.append(orig_pricesT[1][2:11])
Grampians.append(orig_pricesT[1][12:23]) 
Loddon_Mallee.append(orig_pricesT[1][24:34])
Hume.append(orig_pricesT[1][35:47])
Gippsland.append(orig_pricesT[1][48:54])
North_and_West_Metro.append(orig_pricesT[1][55:69])
Eastern_Metro.append(orig_pricesT[1][70:77])
Southern_Metro.append(orig_pricesT[1][78:88])

#variables to calculate average by LGA 
BSWrent = 0
BSWalcohol = 0.0
Grmpsrent = 0
Grmpsalcohol = 0.0
LMrent = 0
LMalcohol=0.0
Humerent=0
Humealcohol=0.0
gpslndrent=0
gpslndalcohol=0.0
NWMrent=0
NWMalcohol=0.0  
EMrent=0
EMalcohol=0.0
SMrent=0
SMalcohol=0.0

#counter to keep track of place in loop to properly assign values.
counter = 0

# loop to find LGA and increment the variables assigned to it
for i in range(len(combT)):
	for cell in combT[i]:
		if cell in Barwon_SW[0]:
			BSWrent += int(combT[i+1][counter].replace("$",""))
			BSWalcohol += float(combT[i+2][counter])
		elif cell in Grampians[0]:
			Grmpsrent += int(combT[i+1][counter].replace("$",""))
			Grmpsalcohol += float(combT[i+2][counter])
		elif cell in Loddon_Mallee[0]:
			LMrent += int(combT[i+1][counter].replace("$",""))
			LMalcohol += float(combT[i+2][counter])
		elif cell in Hume[0]:
			Humerent += int(combT[i+1][counter].replace("$",""))
			Humealcohol += float(combT[i+2][counter])
		elif cell in Gippsland[0]:
			gpslndrent += int(combT[i+1][counter].replace("$",""))
			gpslndalcohol += float(combT[i+2][counter])
		elif cell in North_and_West_Metro[0]:
			NWMrent += int(combT[i+1][counter].replace("$",""))
			NWMalcohol += float(combT[i+2][counter])
		elif cell in Eastern_Metro[0]:
			EMrent += int(combT[i+1][counter].replace("$",""))
			EMalcohol += float(combT[i+2][counter])
		elif cell in Southern_Metro[0]:
			SMrent += int(combT[i+1][counter].replace("$",""))
			SMalcohol += float(combT[i+2][counter])
		counter+=1

# calculate averages for rent and alcohol by LGA
BSWrent /= len(Barwon_SW[0])
BSWalcohol /= len(Barwon_SW[0])
Grmpsrent /= len(Grampians[0])
Grmpsalcohol /= len(Grampians[0])
LMrent /= len(Loddon_Mallee[0])
LMalcohol/= len(Loddon_Mallee[0])
Humerent/= len(Hume[0])
Humealcohol/= len(Hume[0])
gpslndrent/= len(Gippsland[0])
gpslndalcohol/= len(Gippsland[0])
NWMrent/= len(North_and_West_Metro[0])
NWMalcohol/= len(North_and_West_Metro[0])
EMrent/= len(Eastern_Metro[0])
EMalcohol/= len(Eastern_Metro[0])
SMrent/= len(Southern_Metro[0])
SMalcohol/= len(Southern_Metro[0])

#Place all the data into a list
AREASRENT= [BSWrent,Grmpsrent,LMrent,Humerent,gpslndrent,NWMrent,EMrent,SMrent]
AREASALCOHOL=[BSWalcohol,Grmpsalcohol,LMalcohol,Humealcohol,gpslndalcohol,NWMalcohol,EMalcohol,SMalcohol]
listy = [AREAS, AREASRENT, AREASALCOHOL]
listy= zip(*listy)

#create new csv and write to it. 
output = open("AREASAVE.csv",'w')

for row in listy:
	for column in row:
		output.write('{},'.format(column))
	output.write('\n')
output.close()
