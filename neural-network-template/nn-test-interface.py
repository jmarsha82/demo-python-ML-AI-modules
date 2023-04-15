from neuralNetworkClass import NeuralNetwork as nnV_Beta

inputNodes = 3
hiddenNodes = 3
outputNodes = 3
learningRate = 0.3

nnV_Beta.__init__(nnV_Beta, inputNodes, hiddenNodes, outputNodes, learningRate)

print("nnV_Beta inputNodes : " + nnV_Beta.inputNodes)
print("nnV_Beta hiddenNodes : " + nnV_Beta.hiddenNodes)
print("nnV_Beta outputNodes : " + nnV_Beta.outputNodes)
print("nnV_Beta learningRate : " + nnV_Beta.learningRate)
