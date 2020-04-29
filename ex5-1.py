from pyknp import KNP

knp = KNP(jumanpp=True)
result = knp.parse("望遠鏡で泳いでいる女の子を見た。")

for bnst in result.bnst_list():
    parent = bnst.parent
    if parent is not None:
        child_rep = " ".join(mrph.repname for mrph in bnst.mrph_list())
        parent_rep = " ".join(mrph.repname for mrph in parent.mrph_list())
        print(child_rep, "->", parent_rep,parent.bnst_id-bnst.bnst_id-1)