import unittest
import numpy as np
from models import linear_regression


class LinearRegressionTest(unittest.TestCase):
    def test_linear_regression(self):
        train_dataset = np.array([1, 1.1, 2.2, 3.1, 3.9, 5])
        print(type(train_dataset))
        train_labels = np.array([1, 1, 2, 3, 4, 5])
        test_dataset = np.array([0.9, 7, 6.2, -0.9])
        test_labels = np.array([1, 7, 6, -1])

        linreg = linear_regression.LinearRegression()
        linreg.fit(train_dataset, train_labels)


        # self.assertEqual(linreg.predict(10), 10)

