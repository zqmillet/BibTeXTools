import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foo')
parser.add_argument('bar')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')
parameters = '-v'
args = parser.parse_args(parameters.split())
print(args)

# ref: http://python.usyiyi.cn/python_278/library/argparse.html