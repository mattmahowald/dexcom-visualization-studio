import matplotlib.pyplot as plt
import datetime

class DexcomEntry: 
	def __init__(self, entry_time, value): 
		self.entry_dt = entry_time 
		self.value = value

def convert_data(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
	dexcom_entry_list = []
	for line in lines:
		words = list(map(int, line.split()))
		t = datetime.datetime(*words[0:4])
		value = words[5]
		entry = DexcomEntry(t, value)
		dexcom_entry_list.append(entry)

	return dexcom_entry_list

def graph_data(entries):
	times = []
	values = []
	x = [datetime.datetime(1,1,1,0,0) + datetime.timedelta(minutes=i*5) for i in range(len(entries))]
	for entry in entries:
		times.append(entry.entry_dt.ctime())
		values.append(entry.value)
	plt.plot(x, values, 'ro')
	plt.ylabel('Blood Sugar (mg/dL)')
	plt.xlabel('Time')
	plt.ylim(50, 300)
	plt.show()

'''Main functionality of the Script'''
dexcom_data_list = convert_data("example_dexcom_data.txt")
graph_data(dexcom_data_list)
