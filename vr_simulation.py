from simulator import Simulator
from visualizer import Visualizer
from cloud import Cloud
from device import Device
from network import Network
import random

print networks
print "Tufts download speed is " + str(networks['tufts'].download) + " Mbps."

# Initialize devices
DEVICE_OPTS = { OculusRift, HTCVive, PlayStationVR, LG360VR, GearVR, VisusVR }
devices = []
for i in xrange(1, 11):
    device = random.choice(DEVICE_OPTS)
    loc = Location() # Select at random
    devices.append(device(i, loc))

# Initialize cloud
traffic_level = 0
cloud_loc = Location()
timeout = 2000 # 2 seconds
num_players = len(devices)
cloud = Cloud(traffic_level, cloud_loc, timeout, num_players)

# Initialize network
network = TCP();

sim_length = 30 * 60 * 1000     # 30 minutes
sim = Simulator(cloud, network, devices, sim_length)

sim.run()
results = sim.getResults()

viz = Visualizer(results, map(str, range(1,11)))
viz.plotAverageLatency()

# TODO: Be run with passed configurations, create simulator, and produce results
