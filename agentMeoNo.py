

@njit()
def DataAgent():
    return np.array([0.])
@njit()
def Test(state,per):
  actions = getValidActions(state)
  actions = np.where(actions == 1)[0]
  see_future = np.where(state[28:67] == 1)[0] % 13
  id_player_max_cards_len = np.argmax(state[87: 91])
  if 7 in actions and state[25] < 20:
    return 7,per
  if 11 + id_player_max_cards_len in actions:
    return 11 + id_player_max_cards_len,per
  if 28 in actions:
    return 28,per
  elif 29 in actions:
    return 29,per
  elif 31 in actions:
    return 31,per
  giveAwayCardActions = actions[(actions > 15) & (actions < 26)]
  if len(giveAwayCardActions) > 0:
      for i in range(21,24):
        if i in actions:
          return i,per
      if 15 in actions:
        return 15,per
      elif 18 in actions:
        return 18,per
      elif 19 in actions:
        return 19,per
      elif 16 in actions:
        return 16,per
      elif 17 in actions:
        return 17,per
      elif 20 in actions:
        return 20,per
  if 3 in actions :
    return 3, per
  if 0 in actions:
    if np.sum(state[72: 82]) > 0 and  state[27] == 1:
      return 0, per
    elif 10 in actions:
      return 10, per
  if state[11] > 0 or state[25] > 15:
    if 6 in actions:
      return 6, per
  if state[25] < 15:
    if 5 in actions:
      return 5,per
  if len(see_future) > 0:
      if see_future[0] == 12:
          if 1 in actions:
              return 1,per
          if 2 in actions:
              return 2,per
          if 4 in actions:
              return 4,per
      elif see_future[1] == 12:
           if state[71] == 1 and 6 in actions:
               return 6,per
           elif state[71] >= 2:
              if 1 in actions:
                return 1,per
              elif 2 in actions:
                return 2,per
              elif 4 in actions:
                return 4,per
      elif see_future[2] == 12:
         if state[71] <= 2 and 6 in actions:
            return 6,per
         elif state[71] >= 3:
            if 1 in actions:
              return 1,per
            elif 2 in actions:
              return 2,per
            elif 4 in actions:
              return 4,per
         else:
          if 6 in actions:
            return 6,per
  if state[26] <= 2:
     if 1 in actions:
       return 1,per
     elif 2 in actions:
       return 2,per
  if len(actions) == 1:
    act = actions[0]
  else:
    act = actions[-1]
  return act,per