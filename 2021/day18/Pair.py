from math import floor, ceil
class Pair:
    def __init__(self):
        self.left = None
        self.right = None
        self.pairent = None
    
    def explode(self, in_order = None, depth=0):
        if depth == 0:
            in_order = self.in_order([])
        if depth < 4:
            if isinstance(self.left, Pair):
                if self.left.explode(in_order, depth+1):
                    return True
            if isinstance(self.right, Pair):
                if self.right.explode(in_order, depth+1):
                    return True
            return False
        elif depth == 4:
            i = in_order.index(self)
            j = i-1
            while j >= 0:
                pair = in_order[j]
                if isinstance(pair.right, int):
                    pair.right += self.left
                    break
                elif isinstance(pair.left, int):
                    pair.left += self.left
                    break
                j-=1
            j = i+1
            while j < len(in_order):
                pair = in_order[j]
                if isinstance(pair.left, int):
                    pair.left += self.right
                    break
                elif isinstance(pair.right, int):
                    pair.right += self.right
                    break
                j+=1
            if self == self.pairent.left:
                self.pairent.left = 0
            elif self == self.pairent.right:
                self.pairent.right = 0
            else: print('what')
            return True

    def split(self):
        if isinstance(self.left, Pair):
            if self.left.split():
                return True
        if isinstance(self.left, int):
            if self.left > 9:
                i = self.left
                self.left = Pair()
                self.left.pairent = self
                self.left.left = floor(i/2)
                self.left.right = ceil(i/2)
                return True
        if isinstance(self.right, int):
            if self.right > 9:
                i = self.right
                self.right = Pair()
                self.right.pairent = self
                self.right.left = floor(i/2)
                self.right.right = ceil(i/2)
                return True
        if isinstance(self.right, Pair):
            if self.right.split():
                return True
        return False

    def in_order(self, pairs):
        if isinstance(self.left, Pair):
            self.left.in_order(pairs)
        pairs.append(self)
        if isinstance(self.right, Pair):
            self.right.in_order(pairs)
        return pairs

    def magnitude(self):
        if isinstance(self.left, int):
            l = self.left
        elif isinstance(self.left, Pair):
            l = self.left.magnitude()
        if isinstance(self.right, int):
            r = self.right
        elif isinstance(self.right, Pair):
            r = self.right.magnitude()
        return 3*l+2*r
        
    def __str__(self) -> str:
        s = '['
        #if isinstance(self.left, int): 
        s += self.left.__str__()
        s += ','
        #if isinstance(self.right, int): 
        s += self.right.__str__()
        return s + ']'
    def __repr__(self) -> str:
        return self.__str__()