import sys

Word = input()
F = Word.count('f')
if F == 1:
    Find = Word.find('f')
    print(Find)
if F > 1:
    Find1 = Word.find('f')
    Find2 = Word.rfind('f')
    print(Find1, Find2)
if F == 0:
    sys.exit()
