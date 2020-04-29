from pyknp import KNP
import sys

knp=KNP(jumanpp=True)

data=""
for line in iter(sys.stdin.readline,""):
    data+=line
    if line.strip()=="EOS":
        result=knp.result(data)
        data=""
        jiritu=""
        for bnst in result.bnst_list():
            count=0
            for mrph in bnst.mrph_list():
                if "<自立>" in mrph.fstring:
                    count+=1
                    jiritu+=mrph.midasi
                elif count>=2:
                    print(jiritu)
                    count=0
                    jiritu=""
                else:
                    count=0
                    jiritu=""
                    continue
                
                
