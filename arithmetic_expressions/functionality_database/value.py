from abc import ABC
from typing import Optional

class Value(ABC):
    """A base class for different types of values"""
    def get_approximate_value(self) -> Optional['Value']:
        """Returns an approximate value. Returns None if none exists"""
        return None