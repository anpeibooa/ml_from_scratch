import numpy as np


def mean_squared_error(y_true, y_pred):
    """
    Returns the mean squared error between y_true and y_pred
    """
    mse = np.mean(np.power(y_true - y_pred, 2))
    return mse


def shuffle_data(X, y, seed=None):
    """
    Random shuffle of the samples in X and y
    """
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]


def train_test_split(X, y, test_size=0.5, shuffle=True, seed=None):
    """
    Split the data into train and test sets
    """
    if shuffle:
        X, y = shuffle_data(X, y, seed)
    # Split the training data from test data in the ratio of test_size
    split_i = len(y) - int(len(y) // (1 / test_size))
    X_train, X_test = X[:split_i], X[split_i:]
    y_train, y_test = y[:split_i], y[split_i:]

    return X_train, X_test, y_train, y_test


def standardize(X):
    """ Standardize the dataset X """
    return (X - X.mean(axis=0)) / X.std(axis=0)


def normalize(X, axis=-1, order=2):
    """ Normalize the dataset X """
    l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    l2[l2 == 0] = 1
    return X / np.expand_dims(l2, axis)
