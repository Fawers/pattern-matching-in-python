list_ = [1, 2, 3, 4, 5]
[head, neck, torso, *tail] = list_
print(dict(head=head, neck=neck, torso=torso, tail=tail))
