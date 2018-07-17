from net import Network
from time import sleep
from random import random
import math
#
network = Network([1,5,5,1])

a = 0
b = 0
c = 0

while True:
    a = random()
    b = math.sin(a)
    c = network.learn([a],[b])
    print("correct = " + str(b))
    print("net = " + str(c))
    print("\n/////////////////////////////////////////////\n")
    #sleep(0.1)