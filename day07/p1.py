class Node:
    def __init__(self, name="/", root=None, size = 0, typ = None) -> None:
        self.root = root
        self.name = name
        self.child = set()
        self.size = size
        self.type = typ

    def add_child(self, Node):
        self.child.add(Node)
        # self.size += Node.size

    def print(self, indent=0):
        print(f"{indent*' '} - {self.name} ({self.type}, size={self.size})")
        for c in self.child:
            c.print(indent=indent+2)

    def add_size(self, size):
        self.size += size

    def get_node(self, name):
        if name == self.name:
            return self
        
        for c in self.child:
            return c.get_node(c, name)

    def calc_dir_size(self):
        sum = 0
        
        if self.type == 'file':
            sum += self.size

        for c in self.child:
            sum += c.calc_dir_size()
            
        self.size = sum
        return sum


    def query_1(self):
        """
        Find all of the directories with a total size of at most 100000,
        then calculate the sum of their total sizes.
        """

        sum = 0
        
        if self.type == 'dir' and self.size <= 100000:
            sum += self.size

        for c in self.child:
            sum += c.query_1()

        return sum



root = None
curr_path = None
with open('in.txt', 'r') as f:
    for line in f.readlines():
        # check if command or output
        if line.startswith("$"):

            # remove $ in start
            command = line.replace("$ ", "")

            # check if cd
            if command.startswith("cd"):

                # get path
                _, path = command.split()

                # create a new node if not ..
                if path == "..":
                    curr_path = curr_path.root
                else:
                    node = Node(root=curr_path, name = path, typ="dir")

                    # special case for root node
                    if path == "/":
                        root = node                        
                    else:
                        curr_path.add_child(node)

                    # update current path
                    curr_path = node

            # else ls, skip for now
            else:
                pass
        
        # output
        else:
            # if listing dir, skip for now
            if line.startswith("dir"):
                pass

            else:
                size, name = line.split()
                node = Node(name=name, size = int(size), root=curr_path, typ = "file")
                curr_path.add_child(node)

            
root.calc_dir_size()
root.print()
print(root.query_1())