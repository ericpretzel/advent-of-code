class Packet:
    def __init__(self, version, id):
        self.version = version
        self.id = id
        self.val = 0
        self.subpackets_len = -1
        self.subpackets_rem = -1
        self.subpackets = []
        self.parent = None
    
    def add_subpacket(self, packet):
        self.subpackets.append(packet)
        self.subpackets_rem -= 1
        c = nums_consumed()
        curr = self
        while curr:
            curr.subpackets_len -= c
            curr = curr.parent
    
    def total_version_num(self):
        total = self.version
        for subpacket in self.subpackets:
            total += subpacket.total_version_num()
        return total

    def evaluate(self):
        if self.id == 0: # sum
            return sum([subpacket.evaluate() for subpacket in self.subpackets])
        elif self.id == 1: # product
            product = self.subpackets[0].evaluate()
            for i in range(1, len(self.subpackets)):
                product *= self.subpackets[i].evaluate()
            return product
        elif self.id == 2: # min
            return min([subpacket.evaluate() for subpacket in self.subpackets])
        elif self.id == 3: # max 
            return max([subpacket.evaluate() for subpacket in self.subpackets])
        elif self.id == 4: # literal
            return self.val
        elif self.id == 5: # greater
            return 1 if self.subpackets[0].evaluate() > self.subpackets[1].evaluate() else 0
        elif self.id == 6: # lesser
            return 1 if self.subpackets[0].evaluate() < self.subpackets[1].evaluate() else 0
        elif self.id == 7: # equal
            return 1 if self.subpackets[0].evaluate() == self.subpackets[1].evaluate() else 0

# numbers consumed since this was last called
amt_consumed = 0
def nums_consumed():
    global amt_consumed
    tmp = amt_consumed
    amt_consumed = 0
    return tmp

def consume(num_digits):
    global buffer, hex_code, amt_consumed
    while len(buffer) < num_digits:
        char = hex_code[0]
        hex_code = hex_code[1:]
        buffer += bin(int(char, base=16))[2:].zfill(4)
    consumed = buffer[:num_digits]
    buffer = buffer[num_digits:]
    amt_consumed += num_digits
    return consumed

def read_packet():
    version = int(consume(3), base=2)
    type_id = int(consume(3), base=2)
    packet = Packet(version, type_id)
    if type_id == 4: # literal value packet
        # get the literal value
        group = consume(5)
        digits = group[1:]
        while group[0] == '1':
            group = consume(5)
            digits += group[1:]
        packet.val = int(digits, base=2)
    else: # operator packet
        if consume(1) == '0':
            subpackets_len = int(consume(15), base=2)
            packet.subpackets_len = subpackets_len
        else: 
            subpackets_rem = int(consume(11), base=2)
            packet.subpackets_rem = subpackets_rem

    return packet

with open('testinput.in') as f:
    hex_code = f.readline().strip()
buffer = ''
packet_stack = []

# read first packet
first_packet = read_packet()
packet_stack.append(first_packet)
amt_consumed = 0

while len(packet_stack) > 0:
    packet = read_packet()

    parent_packet = packet_stack[-1]

    packet.parent = parent_packet
    parent_packet.add_subpacket(packet)
        
    if packet.id == 4:
        # check if we need to pop from the stack
        while parent_packet and (parent_packet.subpackets_len == 0 or parent_packet.subpackets_rem == 0):
            packet_stack.pop()
            parent_packet = parent_packet.parent
    else:   
        packet_stack.append(packet)

print('total version no:', first_packet.total_version_num())
print('transmission evaluated:', first_packet.evaluate())