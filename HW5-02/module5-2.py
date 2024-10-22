import sys
import matplotlib.pyplot as plt
import numpy as np
from mnist_data import MnistData

def show_image_and_label(data_type, index):
    """
    Display an MNIST image and its corresponding label based on the dataset type and index.

    Args:
        data_type (str): The dataset type, either 'train' or 'test'.
        index (int): The index of the image and label to display.

    Raises:
        ValueError: If an invalid dataset type is provided.
        IndexError: If the index is out of range.
    """
    mnist_data = MnistData()
    (train_images, train_labels), (test_images, test_labels) = mnist_data.load()

    # Select the appropriate dataset
    if data_type == 'train':
        images = train_images
        labels = train_labels
    elif data_type == 'test':
        images = test_images
        labels = test_labels
    else:
        raise ValueError("Invalid dataset type. Please specify 'train' or 'test'.")

    # Ensure the index is valid
    if index < 0 or index >= len(images):
        raise IndexError(f"Index out of range. Please select a valid index between 0 and {len(images) - 1}.")

    # Get the image and label at the specified index
    image = images[index].reshape(28, 28)
    label = labels[index]
    label_number = np.argmax(label)

    # Print the one-hot encoded label and the corresponding digit
    print(f'Label (one-hot): {label}')
    print(f'Label: {label_number}')

    # Display the image
    plt.imshow(image, cmap='gray')
    plt.title(f'Label: {label_number}')
    plt.show()

if __name__ == '__main__':
    """
    Command-line interface for displaying MNIST images and labels.
    
    Usage:
        python module5-2.py [train/test] [index]
    
    Args:
        train/test: Specify which dataset to use (train or test).
        index: The index of the image and label to display.
    """
    if len(sys.argv) != 3:
        print("Usage: python module5-2.py [train/test] [index]")
        sys.exit(1)

    data_type = sys.argv[1]
    index = int(sys.argv[2])

    show_image_and_label(data_type, index)
