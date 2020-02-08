import sys

print('the command line argument are: ')
for i in sys.argv:
    print(i, end=' ')
print(sys.path)