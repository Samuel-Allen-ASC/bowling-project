'''

  _                   _ _                                             _               _   
 | |                 | (_)                                           | |             | |  
 | |__   _____      _| |_ _ __   __ _     ___  ___ ___  _ __ ___  ___| |__   ___  ___| |_ 
 | '_ \ / _ \ \ /\ / / | | '_ \ / _` |   / __|/ __/ _ \| '__/ _ \/ __| '_ \ / _ \/ _ \ __|
 | |_) | (_) \ V  V /| | | | | | (_| |   \__ \ (_| (_) | | |  __/\__ \ | | |  __/  __/ |_ 
 |_.__/ \___/ \_/\_/ |_|_|_| |_|\__, |___|___/\___\___/|_|  \___||___/_| |_|\___|\___|\__|
                                 __/ |_____|                                               
                                |___/                                              
'''
frame_scores = [] #} Establish variables
firstbowls = []
secondbowls = []
thirdbowls = []
bowls = []


def get_firstbowl():  #} this function queries user for an input for the first bowl of a frame and returns it
  first_bowl = 0
  first_try = True
  while error_check(first_bowl, 10) == True or first_try == True:
    first_bowl = input("How many pins did you knock?")
    first_try = False
  first_bowl = int(first_bowl)
  return first_bowl

def get_secondbowl(pins): #} this function queries user for an input for the second bowl of a frame and returns it
  second_bowl = 0
  first_try = True
  while error_check(second_bowl, pins) == True or first_try == True:
    second_bowl = input("How many more pins did you knock?")
    first_try = False
  second_bowl = int(second_bowl)
  return second_bowl

def error_check(user_input, pins):  #} checks for human made errors when getting input
  try:
    user_inputint = int(user_input)
    if user_inputint < 0 or user_inputint > pins: 
      print("Invalid input, please enter a whole number between 0 and " + str(pins))
      user_inputint = 0
    else:
      return False
  except:
    print("invalid input, please enter a number")
  return True

def check_phase(frame_num): #} checks how many frames into the game you are and returns what phase (frame 1-9 or 10) you are on
  if frame_num < 9:
    return 1
  elif frame_num == 9:
    return 2
  else:
    return 0

def record_score(firstbowl, secondbowl, thirdbowl=0): #} appends all values to corresponding lists. thirdbowl arg is supposed to be optional but doesnt work on repl.it
  firstbowls.append(firstbowl)
  secondbowls.append(secondbowl)
  frame_scores.append(firstbowl + secondbowl + thirdbowl)
  thirdbowls.append(thirdbowl)


def record_ball(pins_down): #} record_ball function - returns wether or not another frame is to be bowled
  bowls.append(pins_down)
  if len(bowls) >= 20:
    return False
  else:
    return True

def calc_strike(frame_num, first_bowl, second_bowl): #} calculates and edits a previous frames score if you got a strike
  if first_bowl != 10:
    frame_scores[frame_num] = frame_scores[frame_num] + first_bowl + second_bowl
  else:
    frame_scores[frame_num] = frame_scores[frame_num] + first_bowl #} if next frame is also strike the second bowl will not be added to the frame and the next first bowl will (in calc_strike2)

def calc_spare(frame_num, first_bowl): #} calculates and edits previous frame for spares
  frame_scores[frame_num] = frame_scores[frame_num] + first_bowl

def calc_strike2(frame_num, first_bowl): #} in case user bowled 2 strikes in a row
  frame_scores[frame_num] = frame_scores[frame_num] + first_bowl

def print_scoresheet(): #} this module prints a bowling scoresheet frame by frame
  total_score = 0
  for index, bowl in enumerate(firstbowls):
    if index == 9: #} the following changes are in case of last frame circumstances. they change 10s to Xs etc
      if firstbowls[index] == 10 and secondbowls[index] + thirdbowls[index] == 10:
        thirdbowls[index] = '/'
      if thirdbowls[index] == 10:
        thirdbowls[index] = 'X'
      if firstbowls[index] + secondbowls[index] == 10 and firstbowls[index] != 10:
          secondbowls[index] = '/'
      elif secondbowls[index] == 10 and firstbowls[index] == 10:
          secondbowls[index] = 'X'
      if firstbowls[index] == 10:
        firstbowls[index] = 'X'
      if firstbowls[index] == 0:
        firstbowls[index] = '-'
      if secondbowls[index] == 0:
        secondbowls[index] = '-'
      if thirdbowls[index] == 0:
        thirdbowls[index] = '-'
    else: #} these are for changes in frames 1-10
      if firstbowls[index] == 10:
        firstbowls[index] = ' '
        secondbowls[index] = 'X'
      try:
        if firstbowls[index] + secondbowls[index] == 10:
          secondbowls[index] = '/'
      except:
        pass
      if secondbowls[index] == 0:
        secondbowls[index] = '-'
      if firstbowls[index] == 0:
        firstbowls[index] = '-'
  for i, score in enumerate(frame_scores): #} this is the part of the module that prints score cards for frames
    total_score = total_score + score
    if i == 9: #} the last frame requires an extra bowl slot
      if total_score >= 100:
        print("_____________")
        print("| " + str(total_score) + " |" + str(firstbowls[i]) + "|" + str(secondbowls[i]) + "|" + str(thirdbowls[i]) + '|' + " frame: " + str(i+1))
        print("|___________|")
      elif total_score >= 10:
        print("____________")
        print("| " + str(total_score) + " |" + str(firstbowls[i]) + "|" + str(secondbowls[i]) + "|" + str(thirdbowls[i]) + '|' + " frame: " + str(i+1))
        print("|__________|")
    elif total_score >= 100:
      print("___________")
      print("| " + str(total_score) + " |" + str(firstbowls[i]) + "|" + str(secondbowls[i]) + "|" + " frame: " + str(i+1))
      print("|_________|")
    elif total_score >= 10:
      print("__________")
      print("| " + str(total_score) + " |" + str(firstbowls[i]) + "|" + str(secondbowls[i]) + "|" + " frame: " + str(i+1))
      print("|________|")
    else:
      print("_________")
      print("| " + str(total_score) + " |" + str(firstbowls[i]) + "|" + str(secondbowls[i]) + "|" + " frame: " + str(i+1))
      print("|_______|")

