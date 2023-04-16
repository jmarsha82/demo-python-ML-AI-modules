import numpy
import scipy

# neural network class definition
class NeuralNetwork:
    
    # initialize the neural network
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
    # Set number of nodes in each type
        self.inodes = inputNodes
        self.hnodes = hiddenNodes
        self.onodes = outputNodes
        self.lr = learningRate
        
        # link weight matrices, wih and who
        # weigths inside the arrays are w_i_j, where link from node i to nod k in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        
        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
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
        # convert inputs list to 2d array
        
        pass

    pass

# inputNodes = 3
# hiddenNodes = 3
# outputNodes = 3
# learningRate = 0.3

# n = NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

# n.set_hnodes(hiddenNodes)

# print("n inputNodes : " + str(n.get_inodes()))
# print("n hiddenNodes : " + str(n.get_hnodes()))
# print("n outputNodes : " + str(n.get_onodes()))
# print("n learningRate : " + str(n.get_lr()))