import numpy as np

class LinearRegression:

    def __init__(self):
        self.train_dataset = None
        self.train_labels = None
        self.test_dataset = None
        self.test_labels = None
        self.theta = None

    def fit(self, train_dataset, train_labels):

        assert type(train_dataset) == np.ndarray, "train_dataset must be numpy array"
        assert type(train_labels) == np.ndarray, "train_labels must be numpy array"
        assert train_dataset.ndim == 1, "train_dataset must be 1 dimensional array"
        assert train_labels.ndim == 1, "train_labels must be 1 dimensional array"

        self.train_dataset = train_dataset
        self.train_labels = train_labels
        self.theta = np.random.random(train_dataset.shape)






