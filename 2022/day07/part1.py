puzzle_input = [line.strip() for line in open('input.in').readlines()]

class File:
    def __init__(self, name, _size):
        self.name = name
        self._size = _size
    
    def size(self):
        # so i dont need to type check
        return self._size

class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = dict()
    
    def get(self, child):
        return self.children[child]
    
    def walk(self):
        total = 0
        for child in self.children.values():
            if isinstance(child, Folder):
                if child.size() <= 100000:
                    total += child.size()
                total += child.walk()
        return total

    def size(self):
        return sum(child.size() for child in self.children.values())

root = Folder('/', None)
curr = root

def process_cmd(args, output):
    global curr, root
    cmd = args[0]
    print(args, output)
    if cmd == "ls":
        for f in output:
            info, name = f.split(' ')
            if info == 'dir':
                curr.children[name] = Folder(name, curr)
            else:
                curr.children[name] = File(name, int(info))
    elif cmd == "cd":
        target = args[1]
        if target == '..':
            curr = curr.parent
        elif target == '/':
            curr = root
        else:
            curr = curr.get(target)

i = 1
while i < len(puzzle_input):
    line = puzzle_input[i]
    if line.startswith('$'):
        args = line[2:].split(' ')
        i += 1
        output = []
        while i < len(puzzle_input) and not puzzle_input[i].startswith('$'):
            output.append(puzzle_input[i])
            i += 1
        i -= 1
        process_cmd(args, output)

    i += 1

print(root.walk())