import sys
from pyknp import KNP

knp=KNP(jumanpp=True)

line=sys.stdin.readline()
result=knp.parse(line)

for bnst in result.bnst_list():
    print("".join(mrph.midasi for mrph in bnst.mrph_list()),end=" ")
print()