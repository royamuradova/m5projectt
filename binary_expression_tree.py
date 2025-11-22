# binary_expression_tree.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

from stack import Stack


@dataclass
class TreeNode:
    """
    Node in a binary expression tree.

    value: operator ('+', '-', '*', '/') or operand (string number)
    left, right: child nodes (for non-leaf operator nodes)
    """
    value: str
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


class BinaryExpressionTree:
    """
    BinaryExpressionTree ADT.

    - Build from a postfix (RPN) string using a stack.
    - Provide infix and postfix traversals.
    - Evaluate the expression using recursion.
    """

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    # ---- ADT operations -------------------------------------------------

    def is_empty(self) -> bool:
        """Return True if the tree is empty."""
        return self.root is None

    def clear_tree(self) -> None:
        """Remove all nodes from the tree."""
        self.root = None

    def build_from_postfix(self, postfix: str) -> None:
        """
        Build the expression tree from a whitespace-separated postfix string.

        Example:
            "3 2 5 * +"  →  (3 + (2 * 5))

        Rules:
        - Operand (number) → new leaf node, push on stack.
        - Operator (+, -, *, /) → pop right and left, create new node, push.
        - At the end exactly one node (the root) must remain on the stack.
        """
        stack = Stack()
        tokens = postfix.split()

        for token in tokens:
            # Operand → number
            if self._is_number(token):
                node = TreeNode(token)
                stack.push(node)

            # Operator → internal node with two children
            elif token in {"+", "-", "*", "/"}:
                if stack.is_empty():
                    raise ValueError("Insufficient operands for operator")

                right = stack.pop()

                if stack.is_empty():
                    raise ValueError("Insufficient operands for operator")

                left = stack.pop()

                node = TreeNode(token, left, right)
                stack.push(node)

            # Unsupported token
            else:
                raise ValueError(f"Unsupported token: {token}")

        if stack.is_empty():
            raise ValueError("No expression provided")

        self.root = stack.pop()

        # If stack not empty now, expression was invalid
        if not stack.is_empty():
            raise ValueError("Extra tokens remaining after building tree")

    def evaluate_tree(self) -> float:
        """
        Recursively evaluate the expression stored in the tree.

        Raises:
            ValueError if the tree is empty.
            ZeroDivisionError on division by zero.
        """
        if self.root is None:
            raise ValueError("Cannot evaluate an empty tree")
        return self._evaluate(self.root)

    def infix_traversal(self) -> str:
        """
        Return the infix expression as a string.

        Leaf nodes are printed as numbers.
        Internal nodes are printed with parentheses, e.g.:
        (3 + (2 * 5))
        """
        if self.root is None:
            return ""
        return self._inorder_str(self.root)

    def postfix_traversal(self) -> str:
        """
        Return the postfix expression as a string, tokens separated by spaces.
        """
        if self.root is None:
            return ""
        out: List[str] = []
        self._postorder_collect(self.root, out)
        return " ".join(out)

    # ---- Helper methods (private, recursive) ----------------------------

    def _is_number(self, s: str) -> bool:
        """Return True if s can be converted to a float."""
        try:
            float(s)
            return True
        except ValueError:
            return False

    def _evaluate(self, node: TreeNode) -> float:
        """
        Recursively evaluate the subtree rooted at node.

        Leaf node  → operand value.
        Internal node → evaluate left and right, apply operator.
        """
        # Leaf node: no children
        if node.left is None and node.right is None:
            return float(node.value)

        # Internal node: should have two children
        x = self._evaluate(node.left)
        y = self._evaluate(node.right)
        op = node.value

        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            if y == 0:
                raise ZeroDivisionError("Division by zero")
            return x / y
        else:
            raise ValueError(f"Unknown operator: {op}")

    def _inorder_str(self, node: Optional[TreeNode]) -> str:
        """Return an infix string for the subtree rooted at node."""
        if node is None:
            return ""

        # Leaf node → just the value
        if node.left is None and node.right is None:
            return str(node.value)

        # Internal node → (left op right)
        left = self._inorder_str(node.left)
        right = self._inorder_str(node.right)
        return f"({left} {node.value} {right})"

    def _postorder_collect(self, node: Optional[TreeNode], out: List[str]) -> None:
        """Recursively collect tokens in postfix (postorder) order."""
        if node is None:
            return
        self._postorder_collect(node.left, out)
        self._postorder_collect(node.right, out)
        out.append(str(node.value))
