from tree import Tree

tree = Tree()

tree.set('c', 'C')
tree.set('h', 'H')
tree.set('a', 'A')
tree.set('e', 'E')
tree.set('f', 'F')
tree.set('d', 'D')
tree.set('b', 'B')
tree.set('j', 'J')
tree.set('g', 'G')
tree.set('i', 'I')
tree.set('k', 'K')

tree.debug_print()

print tree.get('d')
