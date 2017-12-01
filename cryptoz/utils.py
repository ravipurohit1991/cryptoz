import itertools

import pandas as pd


# DF

def describe_df(df):
    return df.describe().transpose()


def to_df(group, column):
    return pd.DataFrame({pair: df[column] for pair, df in group.items()})


# Combinations

def product(cols):
    """AA AB AC BA BB BC CA CB CC"""
    return list(itertools.product(cols, repeat=2))


def combine(cols):
    """AB AC AD BC BD CD"""
    return list(itertools.combinations(cols, 2))


def combine_rep(cols):
    """AA AB AC BB BC CC"""
    return list(itertools.combinations_with_replacement(cols, 2))


# Apply

def resampled_apply(df, period, func):
    """Apply on resampled data"""
    period_index = pd.Series(df.index, index=df.index).resample(period).first()
    grouper = pd.Series(1, index=period_index.values).reindex(df.index).fillna(0).cumsum()
    res_sr = df.groupby(grouper).apply(func)
    res_sr.index = period_index.index
    return res_sr


def rolling_apply(df, window, func):
    """Apply while rolling through data"""
    return df.rolling(window=window, min_periods=1).apply(func)


def pairwise_apply(df, combi_func, apply_func):
    """Apply on column combinations"""
    colpairs = combi_func(df.columns)
    return pd.DataFrame({col1 + '-' + col2: apply_func(df[col1], df[col2]) for col1, col2 in colpairs})
