import pandas, ggplot

class Visualizer(object):
	# data should be a list of Data, where each list element corresponds to
	# the results of a device
	def __init__(self, data, labels):
		self.data = data
		self.labels = labels

	def plotAverageLatency(self):
		averages = [d.averageLatency() for d in self.data]
		dat = { "device" : range(1, len(averages) + 1), "average" : averages }
		dataframe = pandas.DataFrame(dat)
		chart = ggplot.ggplot(ggplot.aes(x="device", weight="average"), dataframe) \
				+ ggplot.labs(title="Average Latency Per Device") + \
				ggplot.ylab("Average Latency (ms)") + \
				ggplot.xlab("Device Number")  + \
				ggplot.geom_bar(stat="identity")
		chart.show()
