import collections as coll

#1 - Counter
s = 'Ibrahim Musa Suleiman'
print(f'COUNTER RESULT: {coll.Counter(s)}')
print(f'COUNTER ITEMS: {coll.Counter(s).items()}')
print(f'COUNTER KEYS: {coll.Counter(s).keys()}')
print(f'COUNTER VALUES: {coll.Counter(s).values()}')
print(f'COUNTER MOST COMMON: {coll.Counter(s).most_common(2)}')