import scipy
import scipy.fftpack
import sys
import imageio
import numpy as np


# 2d signal dct using scipy
def dct2D(data):
    return scipy.fftpack.dct(scipy.fftpack.dct(data, axis=1, norm='ortho'), axis=1, norm='ortho')


# 2d signal idct using scipy
def idct2D(data):
    return scipy.fftpack.idct(scipy.fftpack.idct(data, axis=1, norm='ortho'), axis=1, norm='ortho')


# reading image with imageio
signal = imageio.imread('Lenna.png')
# image size
size = signal.shape

# computing the dct of the image (of each one of the rgb channels)
X = np.zeros(size)
for k in range(3):
    X[:, :, k] = dct2D(signal[:, :, k])

# reconstructing the image from the compressed dct
y = np.zeros(size)
for k in range(3):
    y[:, :, k] = idct2D(X[:, :, k])

# write reconstructed image to a file
imageio.imwrite('restored_Lenna.png',
                y)  # there will be no change in the image quality since we are not applying compression
