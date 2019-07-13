import rdkit.Chem as Chem
import rdkit.Chem.Draw as Draw
from PIL import Image

def mark(SMILES:str,Hlight:str,filepath:str):
    mol = Chem.MolFromSmarts(SMILES)
    smart_mol = Chem.MolFromSmarts(Hlight)#'[X4;H3][X3;H0]'
    highlightAtomLists = [atom[0] for atom in mol.GetSubstructMatches(smart_mol)]
    im = Draw._MolsToGridImage([mol], highlightAtomLists=[highlightAtomLists])

    im.save(filepath,'png')

