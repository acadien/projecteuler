#!/usr/bin/python

from numpy import *
import itertools

dice_side_count = 6
dice_count = 2
dice_rolls = [sum(n) for n in itertools.product(range(1,dice_side_count+1), repeat=dice_count)]

roll_probabilities = dict((dice_roll,dice_rolls.count(dice_roll)/float(len(dice_rolls))) for dice_roll in set(dice_rolls))

square_names = "GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2".split()

adj_matrix = matrix(zeros((len(square_names), len(square_names))))

# Step through and set the 
for square_index, square_name in enumerate(square_names):
  for roll_number, roll_probability in roll_probabilities.iteritems():
    adj_matrix[square_index, (square_index+roll_number) % len(square_names)] = roll_probability

# Iterate through Chance spaces
for cc_index in [square_names.index(cc) for cc in [square for square in square_names if square[:2]=='CC']]:
  adj_matrix[cc_index, :] *= 14/16.0
  adj_matrix[cc_index, square_names.index('GO')] += 1/16.0
  adj_matrix[cc_index, square_names.index('JAIL')] += 1/16.0

# Iterate through Community Chest spaces
for ch_index in [square_names.index(ch) for ch in [square for square in square_names if square[:2]=='CH']]:
  adj_matrix[ch_index, :] *= 6/16.0
  adj_matrix[ch_index, square_names.index('GO')] += 1/16.0
  adj_matrix[ch_index, square_names.index('JAIL')] += 1/16.0
  adj_matrix[ch_index, square_names.index('C1')] += 1/16.0
  adj_matrix[ch_index, square_names.index('E3')] += 1/16.0
  adj_matrix[ch_index, square_names.index('H2')] += 1/16.0
  adj_matrix[ch_index, square_names.index('R1')] += 1/16.0
  adj_matrix[ch_index, ([square_name[:1] for square_name in square_names]*2)[ch_index:].index('R')] += 2/16.0
  adj_matrix[ch_index, ([square_name[:1] for square_name in square_names]*2)[ch_index:].index('U')] += 1/16.0
  adj_matrix[ch_index, (ch_index-3) % len(square_names)] += 1/16.0

# Set the initial state to be equally spread out across the board
initial_state = 1.0/len(square_names)*matrix(ones((len(square_names), 1)))

# Calculate the steady state probabilities and sort.
steady_state = sorted([(i,float(v)) for i,v in enumerate(adj_matrix.T**5000 * initial_state)], key=lambda x: x[1], reverse=True)

print steady_state
