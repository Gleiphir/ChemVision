
import rdkit.Chem as Chem
import rdkit.Chem.Draw as Draw


def genPic(smiles):
    assert isinstance(smiles,str)
    chem = Chem.MolFromSmiles(smiles)
    print("SMILE : %s "%(smiles) )
    Draw.MolToFile(chem,'images/tmp.png')




"""
'CC(=O)Nc1ccc(O)cc1',
'CC(C)NCC(O)COc1ccccc1CC=C',
'CC(N)Cc1ccccc1',
'CC(CS)C(=O)N1CCCC1C(=O)O',
'CN(C)CCCN1c2ccccc2Sc3ccc(Cl)cc13',
'OC(=O)Cc1ccccc1Nc2c(Cl)cccc2Cl',
'NCC1(CC(=O)O)CCCCC1',
'COC(=O)c1ccccc1O',
'Nc1ccc(N=Nc2ccccc2)c(N)n1',
'IC(=O)c1ccccc1',
'CCOP(=S)(OCC)Oc1cc(Cl)cc(Cl)c1',
'c1c(C)c(O)c(N)cc1',
'Oc1c(C)cc(N)cc1',
'Oc1c(C)ccc(N)c1',
'c1c(C)c(N)c(O)cc1',

"""