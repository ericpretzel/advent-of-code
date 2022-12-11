import sys
f = 'testinput.in' if len(sys.argv) > 1 else 'input.in'
pi = [line.strip() for line in open(f).readlines()]

class Monkey:
    def __init__(self, items, op, test):
        self.items = items
        self.op = op
        self.test = test
        self.inspections = 0
    
    def __repr__(self):
        return str(self.items)

monkeys: list[Monkey] = []


def generate_op(a, b, operator):
    # wtf is wrong with python
    if operator == '+':
        m_operator = lambda x, y: x + y
    elif operator == '-':
        m_operator = lambda x, y: x - y
    elif operator == '*':
        m_operator = lambda x, y: x * y
    elif operator == '/':
        m_operator = lambda x, y: x // y
    
    return lambda x: m_operator(a if a != 'old' else x, b if b != 'old' else x)
    
def generate_test(t, f, d):
    return lambda x: t if x % d == 0 else f

lcm = 1
for i in range(0, len(pi), 7):
    monkey = pi[i:i+7]
    m_num = int(monkey[0].split(' ')[1][:-1])
    m_items = list(map(int, monkey[1][len('Starting items: '):].split(', ')))
    
    m_ops = monkey[2].split(' ')[-3:]
    
    
    m_opa = int(m_ops[0]) if m_ops[0] != 'old' else 'old'
    m_opb = int(m_ops[2]) if m_ops[2] != 'old' else 'old'
    m_op = generate_op(m_opa, m_opb, m_ops[1])
    

    m_true = int(monkey[4].split(' ')[-1])
    m_false = int(monkey[5].split(' ')[-1])
    m_div = int(monkey[3].split(' ')[-1])
    lcm *= m_div
    m_test = generate_test(m_true, m_false, m_div)
    
    m = Monkey(m_items, m_op, m_test)
    monkeys.append(m)

for _ in range(10000):
    for i in range(len(monkeys)):
        monkey: Monkey = monkeys[i]
        for j in range(len(monkey.items)):
            monkey.inspections += 1
            monkey.items[j] = monkey.op(monkey.items[j]) % lcm
            
            target = monkey.test(monkey.items[j])
            monkeys[target].items.append(monkey.items[j])
        monkey.items = []
            

s = list(sorted(m.inspections for m in monkeys))[-2:]
print(s[0] * s[1])