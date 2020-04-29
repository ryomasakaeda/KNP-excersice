from pyknp import KNP
import sys

knp=KNP()
data=""

flag_noun=False #直前が名詞であったことを示すフラグ
flag_no=False #直前が助詞”の”であったことを示すフラグ
flag_b=False #現在のbnstが”AのB”のBであることを示すフラグ
flag_anob=False #文にAのBの形が含まれていることを示すフラグ

for line in iter(sys.stdin.readline,""):
    data+=line
    if line.strip()=="EOS":
        flag_anob=False
        result=knp.result(data)
        for bnst in result.bnst_list(): #文節ごとのループ
            for mrph in bnst.mrph_list(): #形態素ごとのループ
                if mrph.hinsi=="名詞" and not flag_no: #名詞で、直前が”の”じゃなかったら
                    flag_noun=True
                elif mrph.midasi=="の" and flag_noun: #”の”で、直前が名詞だったら
                    flag_no=True
                    flag_noun=False
                elif mrph.hinsi=="名詞" and flag_no: #"名詞"で、直前が”の”だったら
                    flag_b=True
                    flag_noun=False
                    flag_no=False
                else:
                    flag_no=False
                    flag_noun=False
            if flag_b: #今見ている文節がBだったら
                flag_anob=True
                A=result.bnst_list()[result.bnst_list().index(bnst)-1] #今みているbnstの一個前の文節がAになる
                B=bnst
                parent=A.parent
                if parent is not None:
                    distance=A.parent.bnst_id-A.bnst_id
            flag_b=False
        if flag_anob:　#今見ている文にAのBの形があって
            if distance!=1: #Aの修飾先がBでなかったら
                print("distance",distance)
                print("A",A.midasi)
                print("B",B.midasi)
                print("parent",parent.midasi)
                for bnst in result.bnst_list():　#今見ている文を表示
                    print(bnst.midasi,end="")
                print()
                print()
        data=""
        

        
        