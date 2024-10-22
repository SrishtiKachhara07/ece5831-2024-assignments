import urllib
import gzip
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt

class MnistData:
    """
    MnistData class is responsible for downloading, processing, 
    and loading the MNIST dataset.
    """

    image_dim = (28, 28) 
    image_size = image_dim[0] * image_dim[1]  
    dataset_dir = 'dataset' 
    dataset_pkl = 'mnist.pkl' 
    url_base = 'http://jrkwon.com/data/ece5831/mnist/'  

    key_file = {
        'train_images': 'train-images-idx3-ubyte.gz',
        'train_labels': 'train-labels-idx1-ubyte.gz',
        'test_images': 't10k-images-idx3-ubyte.gz',
        'test_labels': 't10k-labels-idx1-ubyte.gz'
    }

    def __init__(self):
        """
        Initialize the MnistData class, create dataset directory if needed,
        and prepare the dataset (download or load from pickle).
        """
        self.dataset = {}
        self.dataset_pkl_path = os.path.join(self.dataset_dir, self.dataset_pkl)

        # Create the dataset directory if it doesn't exist
        if not os.path.exists(self.dataset_dir):
            os.mkdir(self.dataset_dir)

        self._init_dataset()

    def _change_one_hot_label(self, y, num_class):
        """
        Convert labels to one-hot encoded format.

        Args:
            y (ndarray): Array of labels.
            num_class (int): The total number of classes (e.g., 10 for MNIST).

        Returns:
            ndarray: One-hot encoded labels.
        """
        t = np.zeros((y.size, num_class))
        for idx, row in enumerate(t):
            row[y[idx]] = 1
        return t

    def _download(self, file_name):
        """
        Download the specified file from the MNIST dataset.

        Args:
            file_name (str): The name of the file to download.
        """
        file_path = os.path.join(self.dataset_dir, file_name)

        if os.path.exists(file_path):
            print(f'File: {file_name} already exists.')
            return

        print(f'Downloading {file_name}...')
        opener = urllib.request.build_opener()
        opener.addheaders = [('Accept', '')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(self.url_base + file_name, file_path)
        print('Download complete.')

    def _download_all(self):
        """
        Download all MNIST dataset files if not already present.
        """
        for file_name in self.key_file.values():
            self._download(file_name)

    def _load_images(self, file_name):
        """
        Load images from a gzip file.

        Args:
            file_name (str): The path to the gzip file containing images.

        Returns:
            ndarray: Loaded images in flat (784 bytes) format.
        """
        with gzip.open(file_name, 'rb') as f:
            images = np.frombuffer(f.read(), np.uint8, offset=16)
        images = images.reshape(-1, self.image_size)
        return images

    def _load_labels(self, file_name):
        """
        Load labels from a gzip file.

        Args:
            file_name (str): The path to the gzip file containing labels.

        Returns:
            ndarray: Loaded labels.
        """
        with gzip.open(file_name, 'rb') as f:
            labels = np.frombuffer(f.read(), np.uint8, offset=8)
        return labels

    def _create_dataset(self):
        """
        Create the dataset by loading images and labels, 
        and save it as a pickle file for future use.
        """
        # Load and save training data
        self.dataset['train_images'] = self._load_images(os.path.join(self.dataset_dir, self.key_file['train_images']))
        self.dataset['train_labels'] = self._load_labels(os.path.join(self.dataset_dir, self.key_file['train_labels']))

        # Load and save testing data
        self.dataset['test_images'] = self._load_images(os.path.join(self.dataset_dir, self.key_file['test_images']))
        self.dataset['test_labels'] = self._load_labels(os.path.join(self.dataset_dir, self.key_file['test_labels']))

        # Save the dataset as a pickle file
        with open(self.dataset_pkl_path, 'wb') as f:
            print(f'Pickle: {self.dataset_pkl_path} is being created.')
            pickle.dump(self.dataset, f)
            print('Pickling complete.')

    def _init_dataset(self):
        """
        Initialize the dataset by downloading the files and creating/loading 
        the dataset from a pickle file if it already exists.
        """
        self._download_all()

        if os.path.exists(self.dataset_pkl_path):
            print(f'Pickle: {self.dataset_pkl_path} already exists. Loading dataset...')
            with open(self.dataset_pkl_path, 'rb') as f:
                self.dataset = pickle.load(f)
            print('Dataset loaded successfully.')
        else:
            self._create_dataset()

    def load(self):
        """
        Load the dataset, normalize the images, and apply one-hot encoding to the labels.

        Returns:
            tuple: A tuple containing:
                - (train_images, train_labels)
                - (test_images, test_labels)
        """
        # Normalize the image datasets
        for key in ('train_images', 'test_images'):
            self.dataset[key] = self.dataset[key].astype(np.float32)
            self.dataset[key] /= 255.0

        # One-hot encode the labels
        for key in ('train_labels', 'test_labels'):
            self.dataset[key] = self._change_one_hot_label(self.dataset[key], 10)

        return (self.dataset['train_images'], self.dataset['train_labels']), \
               (self.dataset['test_images'], self.dataset['test_labels'])


if __name__ == '__main__':
    """
    If this script is run through the command line, it prints basic information 
    about the MnistData class and how to use it.
    """
    print("MnistData class is to load MNIST datasets.")
    print("Use the 'load' function to retrieve (train_images, train_labels) and (test_images, test_labels).")
    print("Each image is flattened to 784 bytes. To display an image, reshaping to (28, 28) is necessary.")
    print("Each label is one-hot-encoded. To get the label number, use argmax to get the index where 1 is located.")
