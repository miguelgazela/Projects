class Matrix(object):

    def __init__(self, n, m, init=True):
        self.n = n
        self.m = m
        if init:
            self.rows = [[0]*n for i in range(m)]
        else:
            self.rows = []


def main():
    m1 = Matrix(3, 3)
    print m1.matrix

if __name__ == "__main__":
    main()