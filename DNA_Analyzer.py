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

def complementary_strand(dna_sequence):
    if True:
        complementary_strand = str.maketrans("ATCG", "TAGC")
        complementary_sequence = dna_sequence.translate(complementary_strand)
        return complementary_sequence
print(f"Complementary Sequence: {complementary_strand(dna_sequence)}")

def transcribe_to_rna(dna_sequence):
    if True:
        rna_sequence = dna_sequence.replace("T", "U") 
        return rna_sequence
print(f"RNA Sequence: {transcribe_to_rna(dna_sequence)}")

def calculate_gc_content(dna_sequence):
    count = 0
    for char in dna_sequence:
        if char == "C" or char == "G":
            count += 1
        if len(dna_sequence) == 0:
            return 0.0
    gc_content_percentage = count / len(dna_sequence) * 100
    return round(gc_content_percentage, 2)
print(f"GC Content: {calculate_gc_content(dna_sequence)}%")

def calculate_at_content(dna_sequence):
    count = 0
    for char in dna_sequence:
        if char == "A" or char == "T":
            count += 1
        if len(dna_sequence) == 0:
            return 0.0
    at_content_percentage = count / len(dna_sequence) * 100
    return round(at_content_percentage, 2)
print(f"AT Content: {calculate_at_content(dna_sequence)}%")


