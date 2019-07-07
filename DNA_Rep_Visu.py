# Python 3 Project - DNA Replication + Visualization

# Created by Animesh Patel
# All rights reserved by Animesh Patel.

# Steps
# 1) -> generate DNA randomly
# 2) -> Create a complementary DNA strand (called DNA replication)
# 3) -> Start counting nucleotides - they form the basic structural unit of
#  nucleic acids
# 4) -> Publish double helix - it is the pair of parallel helices intertwined
# about a common axis
# 5) -> generate visualization

# necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Function to create a random DNA structure
def DNA(nucleotide_len):

    nucleotide_storage = {'1': 'A', '2': 'T', '3': 'C', '4': 'G'}
    DNA = ""

    for index in range(nucleotide_len):
        nucleotide = np.random.randint(1,5)
        DNA += nucleotide_storage[str(nucleotide)]
    return DNA

# Test for DNA function for generating random code_Strand
code_Strand = DNA(2500)
"""
print(code_Strand)
print(len(code_Strand))
"""

# function to return complementary DNA
def complementary_DNA(five_three):

    nucleotide_storage = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    DNA = ""

    for nucleotide in five_three:
        DNA += nucleotide_storage[nucleotide]
    return DNA

# Test for complementary DNA function
"""
template_strand = complementary_DNA(code_Strand)
print(template_strand)
"""

# Function to count nucleotides
def nucleotide_count(DNA_value):
    nucleotide_storage = {'As': 0, 'Ts': 0, 'Cs': 0, 'Gs': 0}

    for nucleotide in DNA_value:
        nucleotide_storage[nucleotide + 's'] += 1
    return nucleotide_storage['As'], nucleotide_storage['Ts'], nucleotide_storage['Cs'], nucleotide_storage['Gs']

# Test for count As, Ts, Cs, and Gs
"""
A_count, T_count, C_count, G_count = nucleotide_count(code_Strand)
print('A', A_count, 'T', T_count, 'C', C_count, 'G', G_count)
"""

# function for printing out double helix
def double_Helix(five_three):
    print("5'", five_three, "3'")
    print("3'", complementary_DNA(five_three), "5'")

# Test for double helix
# double_Helix = double_Helix(code_Strand)

# Visualizing DNA
def visualize(DNA):
    length = np.ceil(np.sqrt(len(DNA)))
    x, y = 1, length + 1
    nucleotide_colors = {'A': 'red', 'T': 'lime','C': 'orange', 'G': 'purple'}

    for i in range(int(np.square(length))):
        color = 'pink' # for debugging purposes

        # for the new row check
        if i%length == 0:
            y, x = y - 1, 1
        else:
            x += 1

        try:
            nucleotide = DNA[i]
            color = nucleotide_colors[nucleotide]
        # fill out the out of index information with black colors
        except IndexError:
            color = 'black'

        plt.scatter(x,y, c=color, marker='s')
    plt.show()

# test for coding strand vs. DNA visualization purposes
print(code_Strand)
visualize(code_Strand)
