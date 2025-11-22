# stack.py

class Stack:
    """
    Simple stack ADT implemented using a Python list.
    Used by the BinaryExpressionTree to build trees from postfix expressions.
    """

    def __init__(self) -> None:
        self._data: list = []

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, item) -> None:
        """Push an item on top of the stack."""
        self._data.append(item)

    def pop(self):
        """
        Pop and return the top item from the stack.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self):
        """
        Return the top item from the stack without removing it.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._data[-1]
