from __future__ import annotations
from typing import Any, Optional, Union

class BinarySearchTree(BinaryTree):
    def __init__(self, key: Union[int, float], value: Any) -> None:
        super().__init__(value)
        self.key = key
