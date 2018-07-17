# Neural network
from random import random
from math import e

class Neuron:
    def __init__(self,w = []):
        # Value of neiron in iteration
        self.value = 0.0
        # Weights
        self.w = w
        self.foult = 0.0


class Network:
    # Takes numbers - the number of neurons in the layer
    def __init__(self,net = [1]):
        self.net = []

        for i in range(0,net.__len__()):
            layer = []

            for j in range(0,net[i]):
                layer.append( Neuron() )

            self.net.append(layer)

        self.set_rand_weights()

    # Weights are in range from -0.5 to +0.5
    def set_rand_weights(self):
        for i in range(1,self.net.__len__()):
            for neuron in self.net[i]:
                neuron.w = self.generate_weights(self.net[i-1].__len__())

    # Take the answers from network
    def __work(self,inputs = []):
        # Set first layer
        for i in range(0,self.net[0].__len__()):
            self.net[0][i].value = inputs[i]

        # Set inner and last layers
        for i in range(1,self.net.__len__()):
            for neuron in self.net[i]:
                for j in range(0,neuron.w.__len__()):
                    neuron.value += neuron.w[j] * self.net[i-1][j].value

        # Get last layer
        answers = []
        for neuron in self.net[-1]:
            answers.append(neuron.value)

        return answers


    # Method for using
    def compute(self,inputs = []):
        answers = self.work(inputs)
        self.normalize()
        return answers

    # Method for learning
    def learn(self,inputs = [],answers = []):
        outputs = self.work(inputs)

        # Learning

        self.learning_algorithm(answers)

        # End learning

        self.normalize()
        return outputs

    # Learning algorithm - reverse error recognition
    def __learning_algorithm(self,answers = []):
        # Last layer foults
        for i in range(0,answers.__len__()):
            self.net[-1][i].foult = answers[i] - self.net[-1][i].value

        # Other layers foults
        for i in range(self.net.__len__() - 2,0,-1):
            for j in range(0,self.net[i].__len__()):
                for k in range(0,self.net[i+1].__len__()):
                    self.net[i][j].foult += self.net[i+1][k].foult * self.net[i+1][k].w[j]

        # Correction
        for i in range(0,self.net.__len__() - 1):
            for j in range(0,self.net[i+1].__len__()):
                for k in range(0,self.net[i].__len__()):
                    self.net[i+1][j].w[k] += self.net[i+1][j].foult * self.func(self.net[i+1][j].value) \
                                             * self.net[i][k].value

    # Activate function
    def __func(self,x):
        k = 0.1
        num = (1.0/(1.0 + (e**(-1.0 * x))))
        return k * num * (1.0 - num)

    # Generate numbers int range from -0.5 to +0.5
    def __generate_weights(self,size = 1):
        weights = []
        for i in range(0,size):
            weights.append(random() - 0.5)

        return weights

    # Set neurons values on 0
    def __normalize(self):
        for arr in self.net:
            for neuron in arr:
                neuron.value = 0
                neuron.foult = 0

