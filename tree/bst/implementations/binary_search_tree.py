from __future__ import annotations
import sys
sys.path.append('../../binary/implementations')
from tree import BinaryTree
from typing import Any, Optional, Union


class BinarySearchTree(BinaryTree):
    def __init__(self, key: Union[int, float], value: Any) -> None:
        super().__init__(value)
        self.key = key
