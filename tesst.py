import argparse

def addXY():
    return x + y

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='テスト')
    parser.add_argument('--x', type=int,default=3)
    args = parser.parse_args()

    x = args.x
    y = 7
    z = addXY()
    print(x,y,z)