

def nucleotide_count(sequence, base):

    counter = 0
    sequence = sequence.replace(' ','').upper()
    if base == 'A':
        for char in sequence:
            if char == 'A': counter += 1
    elif base == 'T':
        for char in sequence:
            if char == 'T': counter += 1
    elif base == 'C':
        for char in sequence:
            if char == 'C': counter += 1
    elif base == 'G':
        for char in sequence:
            if char == 'G': counter += 1
    else:
        return "ERROR: Null or invalid input recieved for base argument. Base value can be 'A', 'T', 'C', or 'G'."
    return counter
    
def total_nucleotide_count(sequence):
 
    return {'A':nucleotide_count(sequence, 'A'), 'T':nucleotide_count(sequence, 'T'), 'C':nucleotide_count(sequence, 'C'), 'G':nucleotide_count(sequence, 'G')}
