#KARIM KHAIRAT
#Creates scatter plot for all areas
import matplotlib.pyplot as plt #mpl used for plotting
import csv
#open and read file
inpt= 'combined.csv'
csvopen= open( inpt,"r") 
comb= csv.reader(csvopen)
combT= list(zip(*comb))

#counter to help append
counter =0

#create lists to store variables
medianlist=[]
alcohollist=[]

#loop and find all variables
for i in range(len(combT)):
    for cell in combT[i][1:]:
        if i == 1:
            medianlist.append(int(cell.replace('$','')))
        elif i == 2:
            alcohollist.append(float(cell))
            

#ploting adapted from Joe Kington's answer at:
#http://stackoverflow.com/questions/7376330/axis-range-in-scatter-graphs
    
fig, something=plt.subplots()
something.set_title("Alcohol/Price")
something.set_xlabel("Median Price by LGA")
something.set_ylabel("Alcohol consumption")
something.grid(True,linestyle='-')
something.plot(medianlist,alcohollist,'o')
fig.savefig('scatter.png', dpi=100)
