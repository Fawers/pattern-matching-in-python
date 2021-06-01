class Tree:
    pass

class Branch(Tree):
    __match_args__ = ('value', 'left', 'right')

    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)

class Leaf(Tree):
    pass


def get_first_double_leaf_branch_value(tree):
    match tree:
        # a
        case Branch(v, Leaf(), Leaf()):
            return v

        # b
        case Branch(_, Branch() as left, _):
            return get_first_double_leaf_branch_value(left)

        # c
        case Branch(_, _, Branch() as right):
            return get_first_double_leaf_branch_value(right)

        # d
        case Leaf():
            return None


tree = Branch(5,
              Branch(3,
                     Leaf(),
                     Branch(4,
                            Leaf(), Leaf())),
              Leaf())


print(get_first_double_leaf_branch_value(tree))
