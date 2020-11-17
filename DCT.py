# import matplotlib.pyplot as plt
import scipy
import sys


def dct(data):
    return scipy.fftpack.dct(data)


def idct(data):
    return scipy.fftpack.idct(data)


print(dct(sys.argv[1]))
