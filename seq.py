import torch
import alphabet



def sequence_to_vector(string):
    x = torch.zeros(len(string), dtype=torch.int64)
    for i in range(len(string)):
        x[i] = alphabet.amino_a_to_n[string[i]]
    return x

# class FASTASequence:
#     def __init__(self, header_str, sequence_str, sequence_type='string'):
#         self.header = header_str
#         self.seq = sequence_str
#         self.seq_type = sequence_type
#
#     def convert_to_numeric(self):
#         for i in range(len(self.seq)):
#             #self.seq[i] = alphabet.amino_a_to_n[self.seq[i]]
#
#     def convert_to_tensor(self):
#         seq = torch.zeros(len(self.seq), dtype=torch.int64)
#         for i, c in enumerate(self.seq):
#             seq[i] = alphabet.amino_a_to_n[c]
#
#
#
#
# class FASTADataset:
#     def __init__(self):
#         self.seqs = []
#
#     def read_filepath(self, file_path, sequences=10000000000):
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
#
#             header = ""
#             seq = ""
#             for line in lines:
#                 if line[0] == '>':
#                     if header.size() > 0:
#                         x = 0
#                        # self.seqs.
#
#
