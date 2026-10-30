def validate_sequence(dna_sequence):
    for char in dna_sequence:
        if char not in "ATCG":
            return False
    return True

while True:
    dna_sequence = input("DNA sequence: ").strip().upper()
    if validate_sequence(dna_sequence):
        break
    print("Invalid input. Sequence can only consist of 'A', 'T', 'C', or 'G'.")

def reverse_complementary_strand(dna_sequence):
    if True:
        complementary_strand = str.maketrans("ATCG", "TAGC")
        complementary_sequence = dna_sequence.translate(complementary_strand)
        reverse_complementary = complementary_sequence[::-1]
        return reverse_complementary
print(f"Complementary Sequence: {reverse_complementary_strand(dna_sequence)}")

def dna_sequence_length(dna_sequence):
    base_pairs = len(dna_sequence)
    return base_pairs
print(f"Dna Sequence Length: {dna_sequence_length(dna_sequence)}bp")

def transcribe_to_rna(dna_sequence):
    if True:
        rna_sequence = dna_sequence.replace("T", "U") 
        return rna_sequence
print(f"RNA Sequence: {transcribe_to_rna(dna_sequence)}")

def calculate_gc_content(dna_sequence):
    count = 0
    if len(dna_sequence) == 0:
            return 0.0
    for char in dna_sequence:
        if char == "C" or char == "G":
            count += 1
    gc_content_percentage = count / len(dna_sequence) * 100
    return round(gc_content_percentage, 2)
print(f"GC Content: {calculate_gc_content(dna_sequence)}%")

def calculate_at_content(dna_sequence):
    count = 0
    if len(dna_sequence) == 0:
            return 0.0
    for char in dna_sequence:
        if char == "A" or char == "T":
            count += 1
    at_content_percentage = count / len(dna_sequence) * 100
    return round(at_content_percentage, 2)
print(f"AT Content: {calculate_at_content(dna_sequence)}%")

def nucleotide_frequency(dna_sequence):
    counta = 0
    countt = 0
    countc = 0
    countg = 0
    if len(dna_sequence) == 0:
        return 0.0
    for char in dna_sequence:
        if char == "A":
            counta += 1
            nucleotide_a = counta / len(dna_sequence) * 100
        if char == "T":
            countt += 1
            nucleotide_t = countt / len(dna_sequence) * 100
        if char == "C":
            countc += 1
            nucleotide_c = countc / len(dna_sequence) * 100
        if char == "G":
            countg += 1
            nucleotide_g = countg / len(dna_sequence) * 100
    return f"Nucleotide A: {nucleotide_a}%\nNucleotide T: {nucleotide_t}%\nNucleotide C: {nucleotide_c}%\nNucleotide G: {nucleotide_g}%"
print(nucleotide_frequency(dna_sequence))



