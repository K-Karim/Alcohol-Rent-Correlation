#KARIM KHAIRAT
#Creates scatter plot with greatear area values

import matplotlib.pyplot as plt #import matplotlib's pyplot for plotting purposes
import csv #import to open csv files

#open and read file
inpt= 'AREASAVE.csv'
csvopen= open( inpt,"r") 
area= csv.reader(csvopen)
areaT= list(zip(*area))

#counter to help append
counter =0

#lists to store values
medianlist=[]
alcohollist=[]

#find and append list.
for i in range(len(areaT)):
    for cell in areaT[i]:
        if i == 1:
            medianlist.append(float(cell))
        elif i == 2:
            alcohollist.append(float(cell))
            
#ploting adapted from Joe Kington's answer at:
#http://stackoverflow.com/questions/7376330/axis-range-in-scatter-graphs

fig, something=plt.subplots()
something.set_title("Alcohol/Price Greater Areas")
something.set_xlabel("Median Price by LGA")
something.set_ylabel("Alcohol consumption")
something.grid(True,linestyle='-')
something.plot(medianlist,alcohollist,'o')
fig.savefig('scatterAREAS.png', dpi=100)
