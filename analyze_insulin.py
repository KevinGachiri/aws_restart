import re

# Read the content of the file
with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()

# Use regex to remove 'ORIGIN', numbers, slashes, spaces, and line breaks
cleaned_content = re.sub(r'ORIGIN|\d+|\/| |\n|\r', '', content)

# Confirm the length of the cleaned content
if len(cleaned_content) == 110:
    print("The cleaned sequence has 110 characters.")
else:
    print(f"The cleaned sequence has {len(cleaned_content)} characters.")

# Optional: Write the cleaned content to a new file
with open('preproinsulin-seq-clean.txt', 'w') as cleaned_file:
    cleaned_file.write(cleaned_content)
    
    
# Extract the first 24 characters (amino acids 1-24)
amino_acids_1_to_24 = cleaned_content[:24]

# Verify that the sequence has exactly 24 characters
if len(amino_acids_1_to_24) == 24:
    print("The sequence contains 24 characters.")
else:
    print(f"The sequence contains {len(amino_acids_1_to_24)} characters.")

# Save the sequence to lsinsulin-seq-clean.txt
with open('Isinsulin-seq-clean.txt', 'w') as file:
    file.write(amino_acids_1_to_24)
    
    
# Extract amino acids 25-54 (30 characters)
amino_acids_25_to_54 = cleaned_content[24:54]  # 24th to 54th characters (Python index is zero-based)

# Verify that the sequence has exactly 30 characters
if len(amino_acids_25_to_54) == 30:
    print("The sequence contains 30 characters.")
else:
    print(f"The sequence contains {len(amino_acids_25_to_54)} characters.")

# Save the sequence to binsulin-seq-clean.txt
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(amino_acids_25_to_54)
    
# Extract amino acids 55-89 (35 characters)
amino_acids_55_to_89 = cleaned_content[54:89]  # 54th to 89th characters

# Verify that the sequence has exactly 35 characters
if len(amino_acids_55_to_89) == 35:
    print("The sequence contains 35 characters.")
else:
    print(f"The sequence contains {len(amino_acids_55_to_89)} characters.")

# Save the sequence to cinsulin-seq-clean.txt
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(amino_acids_55_to_89)
    
# Extract amino acids 90-110 (21 characters)
amino_acids_90_to_110 = cleaned_content[89:110]  # 89th to 110th characters

# Verify that the sequence has exactly 21 characters
if len(amino_acids_90_to_110) == 21:
    print("The sequence contains 21 characters.")
else:
    print(f"The sequence contains {len(amino_acids_90_to_110)} characters.")

# Save the sequence to ainsulin-seq-clean.txt
with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(amino_acids_90_to_110)
