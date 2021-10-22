import importlib.util
import logging
from typing import Optional, Tuple, Union, Any

_torch_available = importlib.util.find_spec("torch") is not None
_spacy_available = importlib.util.find_spec("spacy") is not None


def is_torch_available():
    return _torch_available


def is_spacy_available():
    return _spacy_available


if is_torch_available():
    import torch
    from torch import Tensor


def get_logger(name: str) -> logging.Logger:
    """
    Return the logger of the given name.
    :param name: name of the logger to return
    :return: the logger
    """
    return logging.getLogger(name)
