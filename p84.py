#!/usr/bin/python

import itertools
from numpy import *
from scipy.linalg import eig

dice_side_count = 6
dice_count = 2
dice_rolls = [sum(n) for n in itertools.product(range(1,dice_side_count+1), repeat=dice_count)]

standard_roll = dict((dice_roll,dice_rolls.count(dice_roll)/float(len(dice_rolls))) for dice_roll in set(dice_rolls))

square_names = "GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2".split()

adj_matrix = zeros((len(square_names), len(square_names)))

def chance(position):
  index = square_names.index(position)

  def next_square_by_name(square_name, position):
    return ([name[0] for name in square_names*2][position+1:].index(square_name[0])+position+1)%len(square_names)
  
  move = {}
  move['GO'] = 1/16.
  move['JAIL'] = 1/16.
  move['C1'] = 1/16.
  move['E3'] = 1/16.
  move['H2'] = 1/16.
  move['R1'] = 1/16.
  move[square_names[next_square_by_name('R', index)]] = 2/16.
  move[square_names[next_square_by_name('U', index)]] = 1/16.
  move[square_names[index-3]] = 1/16.

  for roll_count, roll_freq in standard_roll.iteritems():
    square_name = square_names[(index+roll_count)%len(square_names)]
    move[square_name] = move.get(square_name, 0.0) + roll_freq * 6/16.

  return move

def community_chest(position):
  index = square_names.index(position)

  move = {}
  move['GO'] = 1/16.
  move['JAIL'] = 1/16.
  
  for roll_count, roll_freq in standard_roll.iteritems():
    square_name = square_names[(index+roll_count)%len(square_names)]
    move[square_name] = move.get(square_name, 0.0) + roll_freq * 14/16.

  return move

def make_roll(position):

  if position[:2]=='CC':
    return community_chest(position)

  if position[:2]=='CH':
    return chance(position)

  roll = {}
  index = square_names.index(position)

  for square, freq in [(square_names[(index+roll_count)%len(square_names)],roll_freq) for roll_count,roll_freq in standard_roll.iteritems()]: 
    roll[square] = freq 
  
  return roll

for square_name in square_names:
  roll = make_roll(square_name)

  for square,freq in roll.iteritems():
    adj_matrix[square_names.index(square_name), square_names.index(square)] = freq

eigenvalue = eig(adj_matrix)
print eigenvalue
