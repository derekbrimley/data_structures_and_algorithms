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

print 'Initial tree:'

tree.debug_print()

print ''
print 'Lookups:'
#tree.get('f')
#tree.get('b')
#tree.get('i')
print ''
print 'BFS:'
tree.walk_bfs()
print ''
print 'DFS preorder:'
tree.walk_dfs_preorder()
print ''
print 'DFS inorder:'
tree.walk_dfs_inorder()
print ''
print 'DFS postorder:'
tree.walk_dfs_postorder()
print ''
print 'Remove b:'
tree.remove('b')
tree.debug_print()