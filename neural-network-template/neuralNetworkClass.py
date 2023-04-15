# neural network class definition
class NeuralNetwork:
    
    # initialize the neural network
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
    # Set number of nodes in each type
        self.inodes = inputNodes
        self.hnodes = hiddenNodes
        self.onodes = outputNodes
        self.lr = learningRate
        pass
    
    # Getters and Setters
    def get_inodes(self):
        return self.inodes

    def set_inodes(self, value):
        self.inodes = value

    def get_hnodes(self):
        return self.hnodes

    def set_hnodes(self, value):
        self.hnodes = value

    def get_onodes(self):
        return self.onodes

    def set_onodes(self, value):
        self.onodes = value
        
    def get_lr(self):
        return self.lr

    def set_lr(self, value):
        self.lr = value
        
    # train the neural network
    def train():
        pass
    
    # query the neural network
    def query():
        pass
    
inputNodes = 3
hiddenNodes = 3
outputNodes = 3
learningRate = 0.3

n = NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

n.set_hnodes(hiddenNodes)

print("H Nodes : " + n.get_hnodes())

# print(nnV_Beta)