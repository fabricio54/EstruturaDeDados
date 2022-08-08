class BSTnode:
    def __init__(self, value=None):
        self.data = value
        self.left = self.right = None

    def insert(self, value):
        if not self.data:
            self.data = value
        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTnode(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTnode(value)

    def sheets(self):
        sheets_left = 0
        sheets_right = 0
        if not self.data:
            return 0
        elif self.data and not self.left and not self.right:
            return 1
        else:
            if self.left:
                sheets_left = self.left.sheets()
            if self.right:
                sheets_right = self.right.sheets()
        return sheets_left + sheets_right

    def grade(self):
        e = d = 0
        if not self.data:
            return 0
        elif not self.left and not self.right:
            return 1
        else:
            if self.left:
                e = self.left.grade() + 1
                if self.right:
                    e -= 1
            if self.right:
                d = self.right.grade() + 1
                if self.left:
                    d -= 1
        return e + d


root = BSTnode()
root.insert(10)
root.insert(32)
root.insert(2)
print(root.sheets())