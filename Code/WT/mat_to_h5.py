import h5py
import numpy
import sys

if len(sys.argv) == 1:
    print('No file provided as argument')
    exit()

try:
    with h5py.File(sys.argv[1], 'r') as fr:
        with h5py.File(sys.argv[1]+'.h5', 'w') as fw: 
            fr.copy('.', fw, 'data')
except FileNotFoundError:
    print('No such file or directory: ' + sys.argv[1])
