import simulator
from cloud import clouds
from device import devices
from game import games
from network import networks

print networks
print "Tufts download speed is " + str(networks['tufts'].download) + " Mbps."

# TODO: Be run with passed configurations, create simulator, and produce results
