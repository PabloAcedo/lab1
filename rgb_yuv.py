import sys  # para entrar parametros por command line


def rgb2yuv(R, G, B):
    # conversion RGB a YCbCr
    y = max(0.299 * R + 0.587 * G + 0.114 * B, 0.0)
    u = max(-0.148 * R - 0.291 * G + 0.439 * B + 128, 0.0)
    v = max(0.439 * R - 0.368 * G - 0.071 * B + 128, 0.0)
    return int(y), int(u), int(v)


def yuv2rgb(Y, U, V):
    # conversion YCbCr a RGB
    b = max(1.164 * (Y - 16) + 2.018 * (U - 128), 0.0)
    g = max(1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128), 0.0)
    r = max(1.164 * (Y - 16) + 1.596 * (V - 128), 0.0)
    r = min(r, 255)
    g = min(g, 255)
    b = min(b, 255)
    return int(r), int(g), int(b)


# function to check if in range
def in_range(p1, p2, p3, min, max):
    if min <= p1 <= max and min <= p2 <= max and min <= p3 <= max:
        return 1

    return 0


# check that the number of arguments are correct
if len(sys.argv) == 5:
    # input parameters
    p1 = int(sys.argv[1])
    p2 = int(sys.argv[2])
    p3 = int(sys.argv[3])
    option = sys.argv[4]
    # if rgb2yuv
    if option == 'rgb2yuv':
        if in_range(p1, p2, p3, 0, 255) == 1:
            YUV = rgb2yuv(p1, p2, p3)
            print('\nRGB:', p1, p2, p3, '--> YUV:', YUV[0], YUV[1], YUV[2], '\n')
        else:
            print('\nERROR: Enter only RGB values, 3 values from 0 to 255.\n')
    # if yuv2rgb
    elif option == 'yuv2rgb':
        RGB = yuv2rgb(p1, p2, p3)
        print('\nYUV:', p1, p2, p3, '--> RGB:', RGB[0], RGB[1], RGB[2], '\n')
    else:
        print('\nERROR: Enter four parameters as: p1 p2 p3 option. '
              'Where "p1", "p2" and "p3" are the values to convert and "option" is '
              'the type of conversion (rgb2yuv or yuv2rgb).\n')
