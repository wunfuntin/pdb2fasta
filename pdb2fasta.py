import sys
from Bio import SeqIO

PDBFile = 'design_233.pdb'
with open(PDBFile, 'r') as pdb_file:
    for record in SeqIO.parse(pdb_file, 'pdb-atom'):
        print('>' + record.id)
        print(record.seq)
