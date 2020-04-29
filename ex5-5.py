from pyknp import KNP
import sys

knp=KNP(jumanpp=True)

def examineBunsetsu(bnst,depth):
    print(depth,bnst.repname)
    for child_bnst in bnst.children:
        examineBunsetsu(child_bnst,depth+1)

data=""
for line in iter(sys.stdin.readline,""):
    data+=line
    if line.strip()=="EOS":
        result=knp.result(data)
        data=""
        root=result.bnst_list()[-1]
        examineBunsetsu(root,0)