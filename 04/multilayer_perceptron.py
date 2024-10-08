import numpy as np

class MultiLayerPerceptron():
    """
    A class representing a 3-layer perceptron neural network.

    Attributes:
    -----------
    network : dict
        A dictionary storing the weights and biases for each layer of the network.

    Methods:
    --------
    sigmoid(s: float) -> float:
        Applies the sigmoid activation function to a given input.
    
    identity_function(s: float) -> float:
        Applies the identity function (returns the input as is).

    softmax(y: np.array) -> np.array:
        Applies the softmax function to obtain probability distributions for multi-class classification.

    forward(x: np.array) -> np.array:
        Performs a forward pass through the network using predefined weights and biases.
    """
    
    def __init__(self):
        """
        Initializes the weights and biases for a 3-layer neural network.
        The weights and biases are predefined, matching those used by the professor during class.
        """
        self.network = {}
        
        # Layer 1 weights and biases (input to hidden)
        self.network['w1'] = np.array([[0.7, 0.9, 0.3], [0.5, 0.4, 0.1]])  # 2x3 weight matrix
        self.network['b1'] = np.array([1, 1, 1])  # Bias for each neuron in the 1st hidden layer

        # Layer 2 weights and biases (hidden to hidden)
        self.network['w2'] = np.array([[0.2, 0.3], [0.4, 0.5], [0.22, 0.1234]])  # 3x2 weight matrix
        self.network['b2'] = np.array([0.5, 0.5])  # Bias for each neuron in the 2nd hidden layer

        # Layer 3 weights and biases (hidden to output)
        self.network['w3'] = np.array([[0.7, 0.1], [0.123, 0.134]])  # 2x2 weight matrix
        self.network['b3'] = np.array([0.1, 0.2])  # Bias for each output neuron

    def sigmoid(self, s):
        """
        Sigmoid activation function.

        Parameters:
        -----------
        s : float
            The input value.

        Returns:
        --------
        float
            The output after applying the sigmoid function, with values squashed between 0 and 1.
        """
        return 1 / (1 + np.exp(-s))
    
    def identity_function(self, s):
        """
        Identity function that returns the input as is (used in regression).

        Parameters:
        -----------
        s : float
            The input value.

        Returns:
        --------
        float
            The same input value (useful for regression-based output).
        """
        return s
    
    def softmax(self, y):
        """
        Softmax activation function for multi-class classification, with numerical stabilization.

        Parameters:
        -----------
        y : np.array
            The raw output values from the final layer.

        Returns:
        --------
        np.array
            Probability distributions for each class after applying softmax.
        """
        m = np.max(y)  # Numerical stability by subtracting max value
        a = np.exp(y - m)  # Exponentiate adjusted values
        s = np.sum(a)  # Sum of all exponentiated values

        return a / s  # Return normalized probabilities

    def forward(self, x):
        """
        Forward pass through the neural network.

        Parameters:
        -----------
        x : np.array
            Input data for the network.

        Returns:
        --------
        np.array
            The output after passing through all layers and applying activations.
        """
        # Layer 1: Input to hidden
        w1, b1 = self.network['w1'], self.network['b1']
        a1 = np.dot(x, w1) + b1  # Weighted sum for the first hidden layer
        z1 = self.sigmoid(a1)  # Sigmoid activation for the first hidden layer

        # Layer 2: Hidden to hidden
        w2, b2 = self.network['w2'], self.network['b2']
        a2 = np.dot(z1, w2) + b2  # Weighted sum for the second hidden layer
        z2 = self.sigmoid(a2)  # Sigmoid activation for the second hidden layer

        # Layer 3: Hidden to output
        w3, b3 = self.network['w3'], self.network['b3']
        a3 = np.dot(z2, w3) + b3  # Weighted sum for the output layer

        # Softmax activation for multi-class classification
        y = self.softmax(a3) 
        # I use softmax in here insted of using identity function which professor use during the class 
        # because Softmax is better than identity in the last layer when you need to produce probabilities for multi-class classification,
        # as it normalizes the output into a probability distribution, whereas identity simply returns raw values.

        return y  # Return the final output (probability distribution)

if __name__ == '__main__':
    print("""
    Welcome to the MultiLayerPerceptron Class!

    This is a simple implementation of a 3-layer neural network designed for multi-class classification tasks.

    Key Features:
    --------------
    1. **Activation Functions**:
       - Sigmoid: Adds non-linearity to the network, outputting values between 0 and 1.
       - Softmax: Converts raw output values into a probability distribution, useful for classification tasks.
       - Identity: Returns inputs as-is, suitable for regression tasks.

    2. **Forward Propagation**:
       - Input data is passed through 3 layers: 
         1st and 2nd layers use Sigmoid activation, 
         and the final layer applies Softmax for classification.

    How to Use:
    ------------
    1. Instantiate the model: `mlp = MultiLayerPerceptron()`
    2. Provide input data (ensure the shape aligns with the network's weights): `output = mlp.forward(input_data)`
    3. Get the network's output, which will be a probability distribution for classification tasks.

    
    """)
