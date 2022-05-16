import torch

amino_n_to_a = [c for c in 'ARNDCQEGHILKMFPSTWYVBZXJ*']
amino_a_to_n = {c: i for i, c in enumerate('ARNDCQEGHILKMFPSTWYVBZXJ*')}
amino_frequencies = torch.tensor([0.074,
                                  0.042,
                                  0.044,
                                  0.059,
                                  0.033,
                                  0.058,
                                  0.037,
                                  0.074,
                                  0.029,
                                  0.038,
                                  0.076,
                                  0.072,
                                  0.018,
                                  0.040,
                                  0.050,
                                  0.081,
                                  0.062,
                                  0.013,
                                  0.033,
                                  0.068])


amino_n_to_v = torch.zeros(len(amino_n_to_a), 20)
for i in range(20):
    amino_n_to_v[i,i] = 1.0

amino_n_to_v[amino_a_to_n['B'],amino_a_to_n['D']] = 0.5
amino_n_to_v[amino_a_to_n['B'],amino_a_to_n['N']] = 0.5

amino_n_to_v[amino_a_to_n['Z'],amino_a_to_n['Q']] = 0.5
amino_n_to_v[amino_a_to_n['Z'],amino_a_to_n['E']] = 0.5

amino_n_to_v[amino_a_to_n['J'],amino_a_to_n['I']] = 0.5
amino_n_to_v[amino_a_to_n['J'],amino_a_to_n['L']] = 0.5

amino_n_to_v[amino_a_to_n['X']] = amino_frequencies
amino_n_to_v[amino_a_to_n['*']] = amino_frequencies