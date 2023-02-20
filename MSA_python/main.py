from msa_unizar import download_pdb, read_sequence, blast_alignment, consensus_sequence

pdb_id = "1ftg"
pdb_chain = "A"

download_pdb(pdb_id)

seq = read_sequence(pdb_id, pdb_chain)
for i in range(len(seq)):
    print(i, seq[i])

blast_alignment(seq, pdb_id, pdb_chain)
consensus_sequence(pdb_id, pdb_chain, seq, "muscle.exe")
