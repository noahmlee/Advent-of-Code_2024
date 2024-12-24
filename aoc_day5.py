from functools import cmp_to_key

p1,p2 = open('input.txt').read().split('\n\n')
rules = {}
for line in p1.splitlines():
    a,b = line.split('|')
    rules.setdefault(int(a),set()).add(int(b))
updates = [[*eval(line)] for line in p2.splitlines()]

def incorrect(r):
    return any(rules.get(n, set()).intersection(r[:i]) for i,n in enumerate(r))

print('part 1:', sum(r[len(r)//2] for r in updates if not incorrect(r)))
print('part 2:', sum(sorted(r, key=cmp_to_key(lambda a,b: (a in rules.get(b))-1))[len(r)//2]
                     for r in filter(incorrect, updates)))