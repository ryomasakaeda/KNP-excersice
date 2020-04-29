from pyknp import KNP
import sys

knp=KNP(jumanpp=True)

data=""
for line in iter(sys.stdin.readline,""):
    data+=line
    if line.strip()=="EOS":
        result=knp.result(data)
        data=""
        for bnst in result.bnst_list():
            for mrph in bnst.mrph_list():
                if mrph.hinsi=="接頭辞":
                    print(bnst.midasi)
                    continue