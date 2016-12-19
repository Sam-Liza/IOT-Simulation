from plotly.plotly import iplot as plot
from plotly import graph_objs as graph

import statistics

class Visualizer(object):
	# data should be a list of Data, where each list element corresponds to
	# the results of a device
	def __init__(self, data, labels):
		self.data = data
		self.labels = labels

	def visualize(data, labels, file = 'results/tmp'):
		data = [graph.Bar(
		    x = labels,
		    y = data
		)]
		plot(data, filename=file)

	def plotAverageLatency(self):
		labels = map(str, range(len(self.data)))        # "0", "1", "2", ...
		data = [device.averageLatency() for device in self.data]
		outputFile = 'average_latency'
		visualize(data, labels, outputFile)

