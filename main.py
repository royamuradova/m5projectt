# main_expression_tree.py
# If this is a separate Replit project, rename this file to main.py

from binary_expression_tree import BinaryExpressionTree


def main():
    # Same test set as in the project instructions / previous module
    postfix_expressions = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -",
    ]

    print("----- Binary Expression Tree -----\n")

    for expr in postfix_expressions:
        tree = BinaryExpressionTree()
        tree.build_from_postfix(expr)

        infix = tree.infix_traversal()
        postfix = tree.postfix_traversal()
        result = tree.evaluate_tree()

        print(f"Postfix Input:      {expr}")
        print(f"Infix Expression:   {infix}")
        print(f"Postfix Expression: {postfix}")
        print(f"Evaluated Result:   {result}\n")


if __name__ == "__main__":
    main()
