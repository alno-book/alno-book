class Tree:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.parent: Optional[Tree] = None
        self.left: Optional[Tree] = None
        self.right: Optional[Tree] = None

    def insert_left(self, t: Tree):
        if self.left is  None:
            t.parent = self
            self.left = t

    def insert_right(self, t: Tree):
        if self.right is  None:
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
