from neuralNetworkClass import NeuralNetwork as nNetwork
import numpy

inputNodes = 6
hiddenNodes = 6
outputNodes = 6
learningRate = 0.4

n = nNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

print("n interaface-inputNodes : " + str(n.get_inodes()))
print("n interaface-hiddenNodes : " + str(n.get_hnodes()))
print("n interaface-outputNodes : " + str(n.get_onodes()))
print("n interaface-learningRate : " + str(n.get_lr()))

numpy.random.rand(3,3)