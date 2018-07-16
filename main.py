from net import Network
from math import sin
from time import sleep
from random import random

network = Network([1,5,5,5,5,5,1])
network.set_rand_weights()

a = 0
b = 0
c = 0

while True:
    a = random()
    b = sin(a)
    c = network.learn([a],[b])
    print("correct = " + str(b))
    print("net = " + str(c))
    print("\n/////////////////////////////////////////////\n")
    #sleep(1)

