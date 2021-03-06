# imports - compatibility packages
from __future__ import absolute_import
from six import string_types

# imports - standard packages
import collections
import numbers

# imports - third-party packages
import pandas as pd

# module imports
from bulbea.exceptions import TYPE_ERROR_STRING

def _raise_type_error(expected_type_name, recieved_type_name):
    raise TypeError(TYPE_ERROR_STRING.format(
        expected_type_name = expected_type_name,
        recieved_type_name = recieved_type_name
    ))

def _get_type_name(o):
    type_ = type(o)
    name  = type_.__name__

    return name

def _check_type(o, type_,  raise_err = False, expected_type_name = None):
    if not isinstance(o, type_):
        if raise_err:
            _raise_type_error(
                expected_type_name = expected_type_name,
                recieved_type_name = _get_type_name(o)
            )
        else:
            return False
    else:
        return True

def _check_str(o, raise_err = False):
    return _check_type(o, string_types, raise_err = raise_err, expected_type_name = 'str')

def _check_int(o, raise_err = False):
    return _check_type(o, numbers.Integral, raise_err = raise_err, expected_type_name = 'int')

def _check_real(o, raise_err = False):
    return _check_type(o, numbers.Real, raise_err = raise_err, expected_type_name = '(int, float)')

def _check_pandas_series(data, raise_err = False):
    return _check_type(data, pd.Series, raise_err = raise_err, expected_type_name = 'pandas.Series')

def _check_iterable(o, raise_err = False):
    return _check_type(o, collections.Iterable, raise_err = raise_err, expected_type_name = '(str, list, tuple)')

def _check_in_range(value, low, high, raise_err = False):
    if not low <= value <= high:
        if raise_err:
            raise ValueError('{value} out of bounds, must be in range [{low}, {high}].'.format(
                value = value,
                low   = low,
                high  = high
            ))
        else:
            return False
    else:
        return True

def _assign_if_none(a, b):
    return b if a is None else a
