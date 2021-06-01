class Tree:
    pass

class Branch(Tree):
    __match_args__ = ('value', 'left', 'right')

    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)

class Leaf(Tree):
    pass


def tree_height(tree):
    match tree:
        case Branch(_, left, right):
            return 1 + max(tree_height(left), tree_height(right))

        case Leaf():
            return 0


tree = Branch(5,
              Branch(3,
                     Leaf(), Leaf()),
              Leaf())


print(tree_height(tree))
