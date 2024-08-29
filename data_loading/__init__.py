"""A package for loading data from the folder data/"""

from .functionality_loader import load_functionality
from .exceptions import FunctionalityLoadingException

__all__ = ['load_functionality', 'FunctionalityLoadingException']