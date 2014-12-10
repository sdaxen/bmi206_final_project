from random import shuffle
import os
import sys

k=10

data_file = sys.argv[1]

with open(data_file, 'rU') as f:
    lines = f.read().splitlines()

data = list(enumerate(lines))

shuffle(data)

test_data = [[] for x in range(k)]
train_data = [[] for x in range(k)]

for i,item in enumerate(data):
    test_ind = i%k
    test_data[test_ind].append(item)
    for j in range(k):
        if j != test_ind:
            train_data[j].append(item)

for i,item in enumerate(test_data):
    item.sort()
    test_file = "%s.test.%d.dat" % (data_file, i)
    with open (test_file, 'w') as f:
        for j,line in item:
            f.write("%s\n" % str(line))

for i,item in enumerate(train_data):
    item.sort()
    train_file = "%s.train.%d.dat" % (data_file, i)
    with open (train_file, 'w') as f:
        for j,line in item:
            f.write("%s\n" % str(line))