class Tree {}

class Branch extends Tree {
    constructor(value, left, right) {
        super();
        [this.value, this.left, this.right] = [value, left, right];
    }
}

class Leaf extends Tree {}

function treeHeight(tree) {
    if (tree instanceof Branch) {
        let [left, right] = [tree.left, tree.right];
        return 1 + Math.max(treeHeight(left), treeHeight(right));
    }
    else if (tree instanceof Leaf) {
        return 0;
    }
}

let tree = new Branch(5,
                      new Branch(3,
                                 new Leaf(), new Leaf()),
                      new Leaf());

console.log(treeHeight(tree));
