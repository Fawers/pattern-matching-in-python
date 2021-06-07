# Pattern Matching finally makes it into Python 3.10. So what?

_"Pattern matching"_: Some people know it; most of those love it. Understandable, as pattern matching offers a concise, elegant way to check and validate values and objects in our programs.  
Because it is a functionality that was practically born alongside functional programming languages, pattern matching could already be found in languages such as Haskell, Scala, Elixir, OCaml, and F# (among others). It became so popular, and so consistently appreciated by the vast majority of programmers that languages that aren't primarily functional started to adopt it. Rust, and now Python, are two examples of these languages.

OK so, why all the fuss when pattern matching is the topic? What's with the hype? After all, some people would say that...

## It's like a switch/case statement, right?
Well, yes and no. While it can be used almost exactly like it, it goes way beyond a _simple_ switch/case instruction.
As an illustration, we will be revisiting some switch/case examples in a similarly popular language: JavaScript.  
For the sake of simplicity, we'll also try to keep the examples simple enough so that no extra learning of the language is needed.

> All the JavaScript examples were tested on the console of the Google Chrome browser, version 90.0.4430.212

Let's suppose that we want to implement a simple, recursive factorial in JavaScript using a switch/case statement. We need to:
- receive a whole number as argument,
- check its value:
  - if it's 0 or 1, we return 1.
  - for any other n we return n * factorial(n-1).

We get the following as a first draft:
```js
function factorial(n) {
    switch (n) {
        case 0:
            return 1;

        case 1:
            return 1;

        default:
            return n * factorial(n-1);
    }
}
```

The equivalent using pattern matching in Python would be:
```python
def factorial(n):
    match n:
        case 0:
            return 1
        
        case 1:
            return 1
        
        case _:
            return n * factorial(n-1)
```

The very first thing we notice is the word `match`: we use it for pattern matching instead of `switch` in switch/case languages. We also have `case _` as the catch-all pattern instead of `default`. Pythonists already know and use the undescore (`_`) when a value is supposed to be ignored; it serves the exact same purpose in match statements.

Right, so in both cases we have two `return 1`s. It's easy to correct this matter in JS: we just have to use fall-through, a.k.a. the cascading effect present in `switch` statements:

```js
function factorial(n) {
    switch (n) {
        case 0:
        case 1:
            return 1;

        default:
            return n * factorial(n-1);
    }
}
```

Comparably, Python's `match` gives us the _or_ operator. With it, we can capture one _or_ another pattern.


```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1

        case _:
            return n * factorial(n-1)
```

And just as we can glue `case`s together in a single cascading effect in a `switch`, we can capture multiple patterns in a `match` with the _or_ operator:

```js
function factorial(n) {
    switch (n) {
        case -2:
        case -1:
        case 0:
        case 1:
            return 1;

        default:
            return n * factorial(n-1);
    }
}
```

```python
def factorial(n):
    match n:
        case -2 | -1 | 0 | 1:
            return 1

        case _:
            return n * factorial(n-1)
```

Cool, eh? We can capture many patterns in a row and execute a single block of code associated to them. But this example raises a question: usually, when one programs factorial, one needs to check whether the passed number is greater than or equal to zero. In both statements we can nest an `if` statement as follows:

```js
function factorial(n) {
    switch (n) {
        case 0:
        case 1:
            return 1;

        default:
            return (n < 0) ? null : n * factorial(n - 1);
            // or
            if (n < 0) {
                return null;
            }
            else {
                return n * factorial(n-1);
            }
    }
}
```

```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1

        case _:
            return None if n < 0 else n * factorial(n-1)
            # or
            if n < 0:
                return None

            else:
                return n * factorial(n-1)
```

And this is where pattern matching starts to outshine the zany switch/case statement. We can use something called guards here.

## Guards? What'chu mean guards?
![guard](./assets/img/guard.jpg)

Yes, guards. And they do exactly what the meme suggests: they "allow" the execution of the code block below when a certain condition is true. Adapting the code above to use guards leaves us with

```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1

        case _ if n > 1:
            return n * factorial(n-1)

        case _:
            return None
```

There are two things we should highlight here:
1. Unlike the meme, we wrote `case _` instead of `case n`. This is because `n` is already defined. We'll be seeing instances where the guard checks variables defined in the respective `case` soon.
2. While it's true that we write more than the one-liner in the previous example, one must consider that this is not only more readable, but also applies for the whole block. The one-liner covers only an expression.

Let us change the example, move on from factorials and see how we can deal with lists and tuples within the context of pattern matching. We already know that both Python and JavaScript offer us a way to separate the first element(s) of a list from the rest of it.

> Due to how tuples are implemented in Python, all the examples regarding lists also apply to tuples.

If we write:

```js
let list = [1, 2, 3, 4, 5];
let [head, ...tail] = list;
console.log(head);
console.log(tail);
```

we'll see that JavaScript assigns `1` to `head` and `[2, 3, 4, 5]` to `tail`, and prints them in the console. Python does the same similarly:

```python
list_ = [1, 2, 3, 4, 5]
[head, *tail] = list_
print(head)
print(tail)
```

And of course, we can use as many variables as we want or need between `head` and `tail` as long as the list has enough elements:

```js
let list = [1, 2, 3, 4, 5];
let [head, neck, torso, ...tail] = list;
console.log({head, neck, torso, tail});
```

```python
list_ = [1, 2, 3, 4, 5]
[head, neck, torso, *tail] = list_
print(dict(head=head, neck=neck, torso=torso, tail=tail))
```

Should we try to capture more values than it is actually possible, Python will show us an error message. Not surprisingly!

```python
>>> [head, neck, *tail] = [1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected at least 2, got 1)
```

That is, we do manage to put `1` into `head`, but there aren't any more values that can be assigned to the variable `neck`. The error message is clear: _expected at least 2 [vaues], got 1_. Usually this would require us to check the length of the list before assigning the values.
(`neck` receives `undefined` in JavaScript).

All this takes us to the next topic, in which we find how `match` deals with this kind of problem automatically.

## Disassembling objects
"Destructuring" is the original term. I chose "disassembling" as a synonym because, well, that's exactly what happens! Have you gone through that childhood phase when you always wanted to disassemble your toys? Break them down into tiny pieces in order to see and understand how they look on the inside, or how they function? `match` can do much the same as that. Not only that: it also checks things for us, having us write less and do more.

Back to the lists. We can write:

```python
def match_list(the_list):
    match the_list:
        case []:
            print('the list is empty')

        case [x]:
            print(f'the list has one single element: {x}')

        case [x, y]:
            print(f'the list has two elements: {x} e {y}')

        case _:
            print('the list has more than two elements')

match_list([])
match_list([10])
match_list([3, 7])
match_list([1, 2, 3, 4, 5])
```

and its execution:

```
$ python py-06-match-list-destructuring.py 
the list is empty
the list has one single element: 10
the list has two elements: 3 e 7
the list has more than two elements
```

Whoa, wait a second! So `match` knows what to do with lists of different lengths? Yes! `match` verifies everything implicitly when we write each case. In this example, it verifies:

* if the list is empty (`len(the_list) == 0`),
* if the list has one element (`len(the_list) == 1`), e
* if the list has two elements (`len(the_list) == 2`).

If the list consists of one element, it is assigned to the variable `x`. If they are two elements, both are assigned to their own variables, `x` and `y`.

But this is not the end; it's also possible to do the same with dictionaries, and capture only the keys that are of interest:

```python
def match_dict(the_dict):
    match the_dict:
        case _ if len(the_dict) == 0:
            print('the dictionary is empty')

        case {'name': nome}:
            print(f'the key "name" has the value {nome}')

        case {'date': date, 'article': {'title': title}}:
            print(f'the article {title} was published on {date}')

        case _:
            print("there ain't any interesting keys")

match_dict({})
match_dict({'name': 'Fabricio', 'age': 29})
match_dict({'date': '05/06/2021', 'time': '00:30', 'article': {'title': 'Pattern Matching in Python'}})
match_dict({'what is love': "baby don't hurt me"})
```

Execution:

```
$ python py-07-match-dict-destructuring.py 
the dictionary is empty
the key "name" has the value Fabricio
the article Pattern Matching do Python was published on 05/06/2021
there ain't any interesting keys
```

Note that we shouldn't try and capture the empty dictionary (`{}`) because `match` captures the dictionary with the least number of valid keys. And the empty dictionary is the one with the least number of valid keys: zero.

```python
>>> match {'key': 'value'}:
...     case {}:
...         print('empty')
...     case {'key': v}:
...         print(v)
... 
empty
```

As opposed to switch/case, we don't have to write any `break`s after each `case`; `match` works similarly to chained `if`s, breaking off as soon as it finds a match and executes its block.

Let's step up the game and climb some trees. Watch your step and don't fall!

One way of implementing a binary tree type and a tree height function in JavaScript is:

```js
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
```

    2

Obviously, this isn't the kind of code we see on a daily basis - if we were to use classes like this, then we'd also override some `height` method provided by `Tree` in both `Branch` and `Leaf`. The point here is to observe how `treeHeight` is implemented, how it uses `if instanceof` and `[left, right] = [tree.left, tree.right]`, because `match` covers these things, too.

```python
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
```

    $ python py-08-match-object-destructuring.py 
    2

That's right - `match` not only validates the correct type, but it also assigns attribute values to variables so that we can use them. And we can nest patterns just as we can nest dicts. This means it's possible to capture a "final" branch like this:

```python
case Branch(v, Leaf(), Leaf()):
    # isinstance(left, Leaf) and isinstance(right, Leaf) == True
    # do something with v, e.g.:
    return v
```

The full example:

```python
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
```

    $ python py-08b-match-object-destructuring.py 
    4

* Case `a` leads us to what we want: a `Branch` with two `Leaf`s. We can just return the value.
* Case `b` has us deal with a `Branch` that has another `Branch` on its left; we go left recursively.
* Case `c` is the same as `b`, but to the right.
* Finally, case `d`, if it ever happens, means that the initial tree is a `Leaf` itself. Return `None`.

Hold on a moment. Doesn't that mean we can actually validate values directly in our patterns? What if...

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_age_major(self):
        match self:
            case Person(name=n, age=18):  # 18 is the age majority in the majority of countries
                print(f'{n} has just reached majority!')
                return True

            case Person(age=a) if a > 18:
                return True

            case _:
                return False


print(Person('Philip', 18).is_age_major())
print(Person('Fabrício', 29).is_age_major())
print(Person('Anna', 15).is_age_major())
```

    $ python py-08c-match-object-destructuring.py 
    Philip has just reached majority!
    True
    True
    False

## What if no patterns match the object?
Some languages adopted different behaviors when it comes to case checking. Rust is by far the stricter one: it yields a compile time error if there is at least one case that wasn't checked. F# preferred to follow the warning path, by just warning the programmer should some case be missing; it throws a runtime error if the matching fails.

Python is a bit more lax regarding that; if no pattern matches the value, then the program just follows execution normally. Just like chained `if`s and `elif`s without an `else` when no conditions evaluate to true and it just goes on to the next instruction.

```python
def exhaustive_matching(number):
    match number:
        case -1:
            return '<'

        case 0:
            return '='

        case 1:
            return '>'

        case _:
            return 'dunno'


def non_exhaustive_matching(number):
    match number:
        case -1:
            return '<'

        case 0:
            return '='

        case 1:
            return '>'


print(exhaustive_matching(10))
print(non_exhaustive_matching(-10))
```

    $ python py-09-match-exhaustive.py
    dunno
    None

A function that doesn't explicitly return anything implicitly returns `None`.

## Conclusion
We witnessed in this extended article a number of ways to use `match`, how it compares to what already exists in languages like JavaScript - `switch/case`, `if instanceof` -, and how extravagantly superior it is to these constructs. Pythonists will soon be able to use it to its full extent and create more powerful, more incredible applications. To wrap this all up, can you find out what the function below does?

```python
def m(f, xs):
    match xs:
        case x, *xs_:
            yield f(x)
            yield from m(f, xs_)

        case []:
            pass
```

***

- Based on [PEP 636](https://www.python.org/dev/peps/pep-0636/);
- Tested with the `python:3.10-rc-alpine` docker image
