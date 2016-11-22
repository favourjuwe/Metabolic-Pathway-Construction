

from sequence_manipulation import nucleotide_count

def nucleotide_composition(sequence, base):
    
    module = nucleotide_count
    A = module.nucleotide_count(sequence, 'A')
    T = module.nucleotide_count(sequence, 'T')
    C = module.nucleotide_count(sequence, 'C')
    G = module.nucleotide_count(sequence, 'G')
    total_bases = A + T + C + G

    if base == 'A':
        return float("%.2f" % ((A/total_bases)*100))
    if base == 'T':
        return float("%.2f" % ((T/total_bases)*100))
    if base == 'C':
        return float("%.2f" % ((C/total_bases)*100))
    if base == 'G':
        return float("%.2f" % ((G/total_bases)*100))
    else:
        return "ERROR: Null or invalid input recieved for base argument. Base value can be 'A', 'T', 'C', or 'G'."
    
def total_nucleotide_composition(sequence):
   
    return {'A':nucleotide_composition(sequence, 'A'), 'T':nucleotide_composition(sequence, 'T'), 'C':nucleotide_composition(sequence, 'C'), 'G':nucleotide_composition(sequence, 'G')}
