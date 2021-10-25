from __future__ import annotations
from typing import Any, Optional


class BinaryTree:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.parent: Optional[BinaryTree] = None
        self.left: Optional[BinaryTree] = None
        self.right: Optional[BinaryTree] = None

    def insert_left(self, t: BinaryTree):
        if self.left is None:
            t.parent = self
            self.left = t

    def insert_right(self, t: BinaryTree):
        if self.right is None:
            t.parent = self
            self.right = t

    def delete_left(self):
        if self.left is not None:
            self.left.delete_left()
            self.left.delete_right()
            self.left = None

    def delete_right(self):
        if self.right is not None:
            self.right.delete_right()
            self.right.delete_right()
            self.right = None
