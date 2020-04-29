from pyknp import KNP
import sys

knp=KNP(jumanpp=True)

data=""
#
for line in iter(sys.stdin.readline,""):
    data+=line
    if line.strip()=="EOS":
        result=knp.result(data)
        data=""
        for bnst in result.bnst_list():
            count=0
            for mrph in bnst.mrph_list():
                if mrph.hinsi=="名詞":
                    count+=1
            if count>=2:
                print(bnst.midasi)