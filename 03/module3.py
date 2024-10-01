# Import necessary modules
import numpy as np  # Importing NumPy for array handling
import logic_gate as lg  # Importing the custom logic_gates module

# Function to run and display test results for a specific gate
def run_gate_tests(gate_name, gate_function):
    """
    Runs the specified gate function with all possible binary input pairs
    and prints the results in a structured format.

    Args:
        gate_name (str): The name of the logic gate being tested (e.g., AND, OR).
        gate_function (function): The function that implements the logic gate 
                                  (e.g., logic_gate.and_gate).
    """
    # Define a matrix of input pairs for testing all possible binary inputs (0 and 1)
    test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    
    # Print header for gate test results
    print(f"--------------------------")
    print(f"Running {gate_name.upper()} Gate Tests:")
    
    # Iterate through each input pair and apply the gate function
    for inputs in test_inputs:
        x1, x2 = inputs  # Unpack the pair of inputs
        output = gate_function(x1, x2)  # Invoke the appropriate gate function with inputs
        print(f"{gate_name.upper()}({x1}, {x2}) = {output}")  # Print the result
    
    print("--------------------------")

# Main execution block
if __name__ == "__main__":
    """
    Main block that runs tests for each logic gate by invoking the run_gate_tests
    function with the appropriate gate function from the LogicGate class.
    """

    # Create an instance of LogicGate class to use its methods
    logic_gate = lg.LogicGate()

    # Run tests for all gates (AND, NAND, OR, NOR, XOR) using the run_gate_tests function
    run_gate_tests("AND", logic_gate.and_gate)
    run_gate_tests("NAND", logic_gate.nand_gate)
    run_gate_tests("OR", logic_gate.or_gate)
    run_gate_tests("NOR", logic_gate.nor_gate)
    run_gate_tests("XOR", logic_gate.xor_gate)
