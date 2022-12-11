monkeys = {}
test = []
import math
with open('in.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith('Monkey'):
            _, m = line.strip().split()
            m = int(m.strip(":"))
            monkeys[m] = {}
            monkeys[m]['count'] = 0
        elif line.strip().startswith("Starting"):
            starts = map(int, line.split(":")[1].split(","))
            monkeys[m]['starting'] = list(starts)
        elif line.strip().startswith("Operation"):
            old, op, num = line.split("=")[1].strip().split()
            monkeys[m]['op'] = op
            monkeys[m]['num'] = num
        elif line.strip().startswith("Test"):
            num = line.strip().split()[-1]
            monkeys[m]['test_div_by'] = int(num)
            test.append(int(num))
        elif line.strip().startswith("If"):
            num = line.strip().split()[-1]
            if 'true' in line:
                monkeys[m]['true_to_monkey'] = int(num)
            if 'false' in line:
                monkeys[m]['false_to_monkey'] = int(num)
    
 
for _ in range(10000):
    for m in monkeys.keys():
        for worry_level in monkeys[m]['starting']:
            num = monkeys[m]['num']
            op = monkeys[m]['op']

            monkeys[m]['count'] += 1

            num = int(num) if num != 'old' else worry_level

            if op == '*':
                    worry_level *= num
            if op == '+':
                    worry_level += num

            worry_level %= math.prod(test)

            if worry_level % monkeys[m]['test_div_by'] == 0:
                monkeys[monkeys[m]['true_to_monkey']]['starting'].append(worry_level)
            else:
                monkeys[monkeys[m]['false_to_monkey']]['starting'].append(worry_level)            

        monkeys[m]['starting'] = []

counts = []
for m in monkeys.keys():
    counts.append(monkeys[m]['count'])

a, b  = sorted(counts, reverse=True)[:2]
print(a*b)