# Importing the NumPy library for efficient array operations
import numpy as np

class LogicGate:
    """
    A class to represent various logic gates (AND, OR, NAND, NOR, XOR).
    This class uses weights and thresholds to simulate logic gate behavior.
    
    Attributes:
        w1, w2: Weights for inputs x1 and x2, respectively.
        th: The threshold value that helps determine the gate's output.
        out: Stores the output of the current gate operation.
        x1, x2: Input values for the logic gate operation.
    """
    
    def __init__(self):
        """
        Initializes the LogicGate class with default values for weights, 
        threshold, output, and inputs. These attributes will be updated 
        during the execution of the gate functions.
        """
        self.w1 = self.w2 = None
        self.th = None
        self.out = None
        self.x1 = self.x2 = None

    def _apply_weights(self, x1, x2, w1, w2, threshold):
        """
        Internal method to calculate the weighted sum of the inputs and apply the 
        threshold to determine the output.
        
        Args:
            x1 (int): The first input value (either 0 or 1).
            x2 (int): The second input value (either 0 or 1).
            w1 (float): The weight assigned to the first input.
            w2 (float): The weight assigned to the second input.
            threshold (float): The threshold value for determining the output.
        
        Returns:
            int: The output of the gate, 1 if the weighted sum exceeds the 
                 threshold, otherwise 0.
        """
        # Storing input values for use in print_output function
        self.x1, self.x2 = x1, x2
        
        # Calculating the weighted sum of inputs
        weighted_sum = np.sum(np.array([x1, x2]) * np.array([w1, w2]))
        
        # Return 1 if weighted sum is greater than threshold, otherwise return 0
        return 1 if weighted_sum > threshold else 0

    def and_gate(self, x1, x2):
        """
        AND gate logic: Returns 1 if both inputs are 1, otherwise 0.
        
        Args:
            x1 (int): The first input (0 or 1).
            x2 (int): The second input (0 or 1).
        
        Returns:
            int: The output of the AND gate (1 if both inputs are 1, else 0).
        """
        return self._apply_weights(x1, x2, 0.5, 0.5, 0.9)

    def or_gate(self, x1, x2):
        """
        OR gate logic: Returns 1 if at least one of the inputs is 1, otherwise 0.
        
        Args:
            x1 (int): The first input (0 or 1).
            x2 (int): The second input (0 or 1).
        
        Returns:
            int: The output of the OR gate (1 if at least one input is 1, else 0).
        """
        return self._apply_weights(x1, x2, 1.0, 1.0, 0.9)

    def nand_gate(self, x1, x2):
        """
        NAND gate logic: Returns 1 if the output of an AND gate is 0, 
        otherwise returns 0.
        
        Args:
            x1 (int): The first input (0 or 1).
            x2 (int): The second input (0 or 1).
        
        Returns:
            int: The output of the NAND gate (1 if AND gate outputs 0, else 0).
        """
        return self._apply_weights(x1, x2, -0.5, -0.5, 0.9)

    def nor_gate(self, x1, x2):
        """
        NOR gate logic: Returns 1 if the output of an OR gate is 0, otherwise 0.
        
        Args:
            x1 (int): The first input (0 or 1).
            x2 (int): The second input (0 or 1).
        
        Returns:
            int: The output of the NOR gate (1 if OR gate outputs 0, else 0).
        """
        return self._apply_weights(x1, x2, -1.0, -1.0, -0.9)

    def xor_gate(self, x1, x2):
        """
        XOR gate logic: Returns 1 if the inputs are different, otherwise 0.
        This is implemented using a combination of OR and NAND gates followed 
        by an AND gate.
        
        Args:
            x1 (int): The first input (0 or 1).
            x2 (int): The second input (0 or 1).
        
        Returns:
            int: The output of the XOR gate (1 if inputs are different, else 0).
        """
        # XOR is OR and NAND gate results combined via an AND gate
        or_result = self.or_gate(x1, x2)
        nand_result = self.nand_gate(x1, x2)
        return self.and_gate(or_result, nand_result)

    def print_output(self, gate_type):
        """
        Print the result of a logic gate operation in a formatted way.
        
        Args:
            gate_type (str): The type of logic gate (AND, OR, NAND, NOR, XOR).
        """
        print(f"The result of {gate_type} gate with inputs {self.x1} and {self.x2} is: {self.out}")

if __name__ == "__main__":
    """
    If the script is run directly, show the help message with instructions on how
    to use the LogicGate class.   
    """
     
    print(
        "**** Logic Gate Class Help ****\n"
        "This script contains the LogicGate class, which simulates basic logic gates (AND, OR, NAND, NOR, XOR) using NumPy.\n"
        "Available methods:\n"
        "    - and_gate(x1, x2): Perform AND gate operation.\n"
        "    - or_gate(x1, x2): Perform OR gate operation.\n"
        "    - nand_gate(x1, x2): Perform NAND gate operation.\n"
        "    - nor_gate(x1, x2): Perform NOR gate operation.\n"
        "    - xor_gate(x1, x2): Perform XOR gate operation.\n"
        "\nTo test the gates, run the module3.py file.\n"
    )
    ####################################################################################
    # Please uncommnet the below code to test the above class is working properly or not. 
    ####################################################################################

    # print("**** Logic Gate Operations ****")
    # print("Testing the LogicGate class with different gate operations:")

    # # Instantiate the LogicGate class
    # logic_gate = LogicGate()

    # # Test AND gate with inputs (1, 1)
    # and_result = logic_gate.and_gate(1, 1)
    # logic_gate.out = and_result
    # logic_gate.print_output('AND')

    # # Test NAND gate with inputs (1, 1)
    # nand_result = logic_gate.nand_gate(1, 1)
    # logic_gate.out = nand_result
    # logic_gate.print_output('NAND')

    # # Test OR gate with inputs (1, 1)
    # or_result = logic_gate.or_gate(1, 1)
    # logic_gate.out = or_result
    # logic_gate.print_output('OR')

    # # Test NOR gate with inputs (1, 1)
    # nor_result = logic_gate.nor_gate(1, 1)
    # logic_gate.out = nor_result
    # logic_gate.print_output('NOR')

    # # Test XOR gate with inputs (1, 0)
    # xor_result = logic_gate.xor_gate(1, 0)
    # logic_gate.out = xor_result
    # logic_gate.print_output('XOR')
