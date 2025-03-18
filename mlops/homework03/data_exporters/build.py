from typing import Tuple
from pandas import DataFrame, Series
from scipy.sparse._csr import csr_matrix
from sklearn.base import BaseEstimator

from mlops.utils.data_preparation.encoders import vectorize_features
from mlops.utils.data_preparation.feature_selector import select_features

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@data_exporter
def export_data(
    data: Tuple[DataFrame, DataFrame, DataFrame], *args, **kwargs) ->Tuple[
        csr_matrix,
        csr_matrix,
        csr_matrix,
        Series,
        Series,
        Series,
        BaseEstimator]:
    """
    Exports data to from dataframes into matrices for features, pd.Series for the target values, and a BaseEstimator for the dictionary vectoriser.

    Args:
        data: The output from the upstream parent block, i.e. the three dataframes (df, df_train, and df_val)
        args: The output from any additional upstream blocks (if applicable) - I believe these should be specified as the global variables

    Output (optional):
        X: The combined matrix of X values (both train and val)
        X_test: The matrix of X_train values
        X_val: The combined matrix of X_val values
        y: The series of y values (both train and val)
        y_train: The y values for the train dataframe
        y_val: The y values for the validation dataframe
    """
    df, df_train, df_val = data
    target = kwargs.get('target','duration')

    X, _, _ = vectorize_features(select_features(df))
    y: Series = df[target]

    X_train, X_val, dv = vectorize_features(
        select_features(df_train),
        select_features(df_val)
    )
    y_train = df_train[target]
    y_val = df_val[target]

    return X, X_train, X_val, y, y_train, y_val, dv