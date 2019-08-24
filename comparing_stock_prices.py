import matplotlib.pyplot as plt 
import csv
# Before compiling and running pls download the datasets of this companies..!!!
tesla_open , tdc_open , tcs_open , reliance_open , google_open ,dell_open , brk_open= [],[],[],[],[],[],[]

tesla_date , tdc_date , tcs_date , reliance_date , google_date ,dell_date , brk_date= [],[],[],[],[],[],[]
with open('TSLA2.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		s=""
		if 'Date' not in row:
			tesla_open.append(row[1])
			date = row[0].split('-')
			tesla_date.append(int(date[2]))

with open('TDC.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		if 'Date' not in row:
			tdc_open.append(row[1])
			date = row[0].split('-')
			tdc_date.append(int(date[2]))


with open('TCS.NS.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		if 'Date' not in row:
			tcs_open.append(row[1])
			date = row[0].split('-')
			tcs_date.append(int(date[2]))


with open('RELIANCE.NS.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		if 'Date' not in row:
			reliance_open.append(row[1])
			date = row[0].split('-')
			reliance_date.append(int(date[2]))


with open('GOOGL.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		if 'Date' not in row:
			google_open.append(row[1])
			date = row[0].split('-')
			google_date.append(int(date[2]))


with open('DELL.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		if 'Date' not in row:
			dell_open.append(row[1])
			date = row[0].split('-')
			dell_date.append(int(date[2]))

with open('BRK-B.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		if 'Date' not in row:
			brk_open.append(row[1])
			date = row[0].split('-')
			brk_date.append(int(date[2]))
x1 = [x for x in range(4000)]

plt.plot(tesla_date,tesla_open,label = 'Tesla')

plt.plot(tdc_date,tdc_open,label = 'TDC')
plt.plot(tcs_date,tcs_open,label = 'TCS')
plt.plot(reliance_date,reliance_open,label = 'RELIANCE')

plt.plot(google_date,google_open,label= 'Google')

plt.plot(dell_date,dell_open,label = 'Dell')
plt.plot(brk_date,brk_open,label = 'Berkshire Hathaway Inc.')
plt.legend()
plt.show()
#print(x1)


