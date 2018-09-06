'''

  _            _     _                                    
 | |          | |   | |                                   
 | |_ ___  ___| |_  | |__   __ _ _ __ _ __   ___  ___ ___ 
 | __/ _ \/ __| __| | '_ \ / _` | '__| '_ \ / _ \/ __/ __|
 | ||  __/\__ \ |_  | | | | (_| | |  | | | |  __/\__ \__ \
  \__\___||___/\__|_|_| |_|\__,_|_|  |_| |_|\___||___/___/
               |______|                                                                       
'''

import bowling_scoresheet as bs
from random import randint


randomgame_phase = 0
usergame_phase = 0
strike = False
spare = False
strike2 = False
gamebool = True

while gamebool == True:
  game_type = int(input("for user input press 1. for random input press 2"))  #} this decides wether
  if game_type == 1:                                #  the bowls are decided by user or by computer
    usergame_phase = 1  #} while in development (before doing the last frame) this gave a boolean
  elif game_type == 2:  #  value
    randomgame_phase = 1
  currframe_num =  0

            #------USER INPUT GAME------#
            #___________________________#
  
    #user game phase 1 (frames 1-9)-------------
  while usergame_phase == 1:
    currframe_num = currframe_num + 1 #} to remember what frame we are on

    firstbowl = bs.get_firstbowl()  #} get value for first bowl of frame
    pins = 10 - firstbowl #} so that the program knows how many pins are left for the user to knock
    secondbowl = 0  #} so that if user striked(?) there is a value assigned to secondbowl
    if firstbowl != 10: #} check if user hit a strike (determines if the get second bowl)
      secondbowl = bs.get_secondbowl(pins)  #} get value for second bowl of frame

    prevframe_num = currframe_num - 2 #} finds index of prev frame so it can be changed in the following
    if strike == True:  #} this confirms if a strike was bowled last turn
      bs.calc_strike(prevframe_num, firstbowl, secondbowl)  #} uses values from the current frame to
    if spare == True:                                       #  edit the frame score at the prevframe_num
      bs.calc_spare(prevframe_num, firstbowl)               #  index in the array
    if strike2 == True:
      bs.calc_strike2(prevframe_num - 1, firstbowl) #} -1 because this stub modifies the frame before
      strike2 = False                               #  the last frame
    if strike == True and firstbowl == 10:  #} if they got 2 strikes in a row the first must get their
      strike2 = True                        #  second bowl from the next frame

    strike = False
    spare = False
    if firstbowl == 10: #} checks if a strike occurred this turn to be calculated next turn after
      strike = True     #  bowls are recorded
      print("STRIKE!")
    elif secondbowl == pins:  #}  checks if a spare occurred this turn. because getting a strike makes
      spare = True            #   pins = 0 and secondbowl = 0 i use elif after checking for strike
      print("spare!")
      

    bs.record_score(firstbowl, secondbowl)
    usergame_phase = bs.check_phase(currframe_num)
    gamebool = bs.record_ball(firstbowl)  #} modifies and array which holds number of pins
    gamebool = bs.record_ball(secondbowl) #  knocked down by each bowl and returns bool value
                                          #  that indicates wether another frame needs to be bowled

    #user game phase 2 (frame 10)--------------
  if usergame_phase == 2:
    currframe_num = currframe_num + 1
    extra_bowl = False
    firstbowl = bs.get_firstbowl()
    pins = 10 - firstbowl
    if firstbowl == 10:
      extra_bowl = True
      pins = 10
    secondbowl = bs.get_secondbowl(pins)
    if secondbowl == pins and pins == 10:
      pins = 10
    elif secondbowl == pins and pins != 10:
      extra_bowl = True
      pins = 10
    else:
      pins = pins - secondbowl
    prevframe_num = currframe_num - 2
    if strike == True:
      bs.calc_strike(prevframe_num, firstbowl, secondbowl)
    if spare == True:
      bs.calc_spare(prevframe_num, firstbowl)
    if strike2 == True:
      bs.calc_strike2(prevframe_num - 1, secondbowl)
      strike2 = False
    if strike == True and firstbowl == 10:
      bs.calc_strike2(prevframe_num, secondbowl)
    thirdbowl = 0
    if extra_bowl == True:
      thirdbowl = bs.get_secondbowl(pins)
      gamebool = bs.record_ball(thirdbowl)
    bs.record_score(firstbowl, secondbowl, thirdbowl)
    bs.print_scoresheet()
    gamebool = bs.record_ball(firstbowl)
    gamebool = bs.record_ball(secondbowl)



            #------RANDOM INPUT GAME------#
            #_____________________________#

    #random game phase 1 (frames 1-9)--------------
  while randomgame_phase == 1:
    currframe_num = currframe_num + 1 #} keeps what frame we are on

    firstbowl = randint(0,10)     #}  getting random first bowl value
    pins = 10 - firstbowl         #}  finds how many pins left after first bowl
    secondbowl = randint(0,pins)  #}  gets a value between 0 and the amount of pins left after first
                                  #   bowl (only value left after stike is 0)
    prevframe_num = currframe_num - 2 #} remembers what frame is prev so it can be changed
    if strike == True:
      bs.calc_strike(prevframe_num, firstbowl, secondbowl)
    if spare == True:
      bs.calc_spare(prevframe_num, firstbowl)
    if strike2 == True:
      bs.calc_strike2(prevframe_num - 1, firstbowl) 
      strike2 = False
    if strike == True and firstbowl == 10: 
      strike2 = True
    strike = False
    spare = False
    if firstbowl == 10: 
      strike = True     
    elif secondbowl == pins:  #} checks if a spare occurred to be calced next turn
      spare = True            #} 
    bs.record_score(firstbowl, secondbowl,0)
    randomgame_phase = bs.check_phase(currframe_num)
    gamebool = bs.record_ball(firstbowl)
    gamebool = bs.record_ball(secondbowl)
    

    #random game phase 2 (frame 10)--------------
  if randomgame_phase == 2:
    currframe_num = currframe_num + 1
    extra_bowl = False
    firstbowl = randint(0,10)
    pins = 10 - firstbowl
    if firstbowl == 10:
      extra_bowl = True
      pins = 10
    secondbowl = randint(0,pins)
    if secondbowl == pins and pins == 10:
      pins = 10
    elif secondbowl == pins and pins != 10:
      extra_bowl = True
      pins = 10
    else:
      pins = pins - secondbowl
    prevframe_num = currframe_num - 2 #} remembers what frame is prev so it can be changed
    if strike == True:
      bs.calc_strike(prevframe_num, firstbowl, secondbowl)
    if spare == True:
      bs.calc_spare(prevframe_num, firstbowl)
    if strike2 == True:
      bs.calc_strike2(prevframe_num - 1, secondbowl)
      strike2 = False
    if strike == True and firstbowl == 10:
      bs.calc_strike2(prevframe_num, secondbowl)
    thirdbowl = 0
    if extra_bowl == True:
      thirdbowl = randint(0, pins)
      gamebool = bs.record_ball(thirdbowl)
    bs.record_score(firstbowl, secondbowl, thirdbowl)
    bs.print_scoresheet()
    gamebool = bs.record_ball(firstbowl)
    gamebool = bs.record_ball(secondbowl)
