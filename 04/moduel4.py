import numpy as np
import multilayer_perceptron as mp

# Initialize the MultiLayerPerceptron class
mlp = mp.MultiLayerPerceptron()

def display_result(input_data):
    """
    Function to perform a forward pass and display the results.
    
    Parameters:
    -----------
    input_data : np.array
        Input data array for the perceptron network.
    
    Returns:
    --------
    np.array
        Output probabilities from the network.
    """
    # Perform forward pass through the network
    y = mlp.forward(input_data)
    
    # Print formatted results
    
    print(f">>> Input Data: {input_data}")
    print(f">>> Output Probabilities: {y}")
    print("End of forward pass.\n")
    
    return y

# Main code to test the MultiLayerPerceptron
if __name__ == '__main__':
    print("MultiLayer Perceptron Neural Network Outputs:\n")

    # Example 1
    input_data1 = np.array([0.45321, 0.68482])
    display_result(input_data1)

    # Example 2
    input_data2 = np.array([0.10193, 0.34812])
    display_result(input_data2)

    # Example 3
    input_data3 = np.array([0.86243, 0.27834])
    display_result(input_data3)
