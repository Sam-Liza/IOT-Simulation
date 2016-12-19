from simulator import Simulator
from visualizer import Visualizer
from cloud import Cloud
import device
import network as net
import random
from location import Location

# Initialize devices
DEVICE_OPTS = [ device.OculusRift, device.HTCVive, device.PlayStationVR,
        device.LG360VR, device.GearVR, device.VisusVR ]
devices = []
for i in xrange(1, 11):
    device = random.choice(DEVICE_OPTS)
    loc = Location() # Select at random
    devices.append(device(loc))

# Initialize cloud
traffic_level = 'low'
cloud_loc = Location()
timeout = 10000 # 10 seconds
num_players = len(devices)
cloud = Cloud(traffic_level, cloud_loc, timeout, num_players)

# Initialize network
packet_loss_probability = 0 # % chance of network-related dropped packet
network = net.TCP(packet_loss_probability);

sim = Simulator(cloud, network, devices)

sim.runFor(20 * 60 * 1000) # Number of milliseconds

results = sim.getResults()

viz = Visualizer(results, map(lambda n: "Device " + str(n), range(1,11)))
viz.plotAverageLatency()

# TODO: Be run with passed configurations, create simulator, and produce results
