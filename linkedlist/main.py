from linkedlist import LinkedList, Node 
        
with open('data_example.csv') as f:
    i = 0
    for line in f:
        line = line.rstrip()
        cmd = line.split(',')
        print('{}:{}'.format(i, ','.join(cmd)))
        if cmd[0] == 'CREATE':
            arr = LinkedList()
        elif cmd[0] == 'DEBUG':
            arr.debug_print()
        elif cmd[0] == 'ADD':
            arr.add(cmd[1])
        elif cmd[0] == 'INSERT':
            arr.insert(int(cmd[1]),cmd[2])
        elif cmd[0] == 'SET':
            arr.set(int(cmd[1]),cmd[2])
        elif cmd[0] == 'GET':
            arr.get(int(cmd[1]))
        elif cmd[0] == 'DELETE':
            arr.delete(int(cmd[1]))
        elif cmd[0] == 'SWAP':
            arr.swap(int(cmd[1]),int(cmd[2]))
        i += 1