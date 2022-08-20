import sys

print('script_args melduje sie, przekazane parametry:')
print(sys.argv)

for file in sys.argv[1:]:
    print(open(file).read())
    print('-' * 44 + '\n\n')
