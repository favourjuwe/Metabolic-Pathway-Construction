

def transcription(parent_strand, output_form=0, case='upper'):

    
    conversion_dict = {'T':'U','A':'A','C':'C','G':'G'}
    replicated_strand = ''
    parent_strand = parent_strand.replace(' ','').upper()
    
    if output_form == 0:
        for char in parent_strand:
            if char in conversion_dict.keys():
                replicated_strand += conversion_dict[char]
            else:
                return 'ERROR: Invalid parent_strand input (raw ATCG-base DNA sequence required).'    
        if case == 'upper':
            return replicated_strand.strip()
        if case == 'lower':
            return replicated_strand.lower().strip()
            
    if output_form == 1:
        for char in parent_strand:
            if char in conversion_dict.keys():
                replicated_strand += conversion_dict[char]
            else:
                return 'ERROR: Invalid parent_strand input (raw ATCG-base DNA sequence required).'

        temp_list = [replicated_strand[i:i+3] for i in range(0, len(replicated_strand), 3)] #storing codons as elements of temp_list
        codon_strand = ' '.join(temp_list)

        if case == 'upper':
            return codon_strand.strip()
        if case == 'lower':
            return codon_strand.lower().strip()

    if output_form == 2:
        for char in parent_strand:
            if char in conversion_dict.keys():
                replicated_strand += conversion_dict[char] + ' '
            else:
              return 'ERROR: Invalid parent_strand input (raw ATCG-base DNA sequence required).'

        if case == 'upper':
            return replicated_strand.strip()
        if case == 'lower':
            return replicated_strand.lower().strip()
