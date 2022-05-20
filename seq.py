import torch
import alphabet


def FASTASequence:
    def __init__(self, header_str, sequence, sequence_type='string'):
        self.header = header_str
        self.seq = sequence_str
        self.seq_type = sequence_type

    def convert_to_numeric(self):
        for i in range(len(self.seq)):
            self.seq[i] = alphabet.amino_a_to_n[self.seq[i]]

    def convert_to_tensor(self):
        seq = torch.zeros(len(self.seq), dtype=torch.int64)
        for i, c in enumerate(self.seq):
            seq[i] = alphabet.amino_a_to_n[c]




def FASTADataset:
    def __init__(self):
        self.seqs = []

    def read_filepath(self, file_path, sequences=10000000000):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            header = ""
            seq = ""
            for line in lines:
                if line[0] == '>':
                    if header.size() > 0:
                        self.seqs.