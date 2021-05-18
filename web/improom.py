def genReturn(status, msg, room_name, room_details, room_options, looked, hp, stick, approach):
  retJson = {
    "status": status,
    "msg": msg,
    "data": {
      "room_name": room_name,
      "room_details": room_details,
      "room_options": room_options,
      "looked" : looked,
      "hp": hp,
      "stick": stick,
      "approach": approach 
    }
  }
  return retJson

def impCheck(approach):
      # Returns true to see if you can see the imp
      if approach >= 10:
          return True
      else:
          return False

def imp(choice, looked, stick, hp, approach):
  if hp <= 0: 
    retJson = {
      "status": 302,
      "msg": "dead from imp",
      "data": {
        "room_name": "improom",
        "room_details": "The imp's attacks are too much, and you succumb to it. You died :(",
        "room_options": ["Hit the reset button to try again"],
        "looked": False,
        "stick": False,
        }
      }
    return retJson   
  # Imp Movement
  approach += 2

  if ((stick == True) and (impCheck(approach) == True)):
    retJson = {
    "status": 200,
    "msg": "Enter the Boss Room",
    "data": {
      "room_name": "bossroom",
      "room_details": "You smash the imp in the jaw. It recoils in horror and flies through the crack in the ceiling. You make a torch out of your root and step into into a tiny room at the end of the chamber. The door slams behind you. The torch you crafted in the previous room comes in handy, this room would be pitch black without it.",
      "room_options": [
   "Look."],
      "looked": False,
      "stick": True,
      "hp": hp
      }
    }
    return retJson  

  room_name = 'improom'

  if "look" in choice:
    room_details = "You are in a large room. It is dimly lit by a crack in the ceiling that is letting some sunlight in through the trees above. You see an imp in front of you, it seems to have been approaching since you entered the room. Roots of the trees are poking through the roof, it looks like you could break one off to defend yourself."
    room_options = [     
        "Move away from the imp.",
        "Grab a root."]
    
    if impCheck(approach) == True:
      room_details += " It swings at you and draws blood!"
      hp -= 10
    if looked == True: 
      room_options = ["Move away from the imp.",
        "Grab a root."]
    looked = True

    return genReturn(200, "Already looked", room_name, room_details, room_options, looked, hp, stick, approach)
  
  if looked == True and "move" in choice:
    if impCheck(approach) == True:
      room_details = "The imp is too close now! It scratches you!"
      hp -= 10
    else:
        approach += -1
        room_details = "You scramble away from the imp, but its moving too fast to escape from."

    room_options = [     
        "Move away from the imp.",
        "Grab a root."]

    return genReturn(200, "Moved in the imp room", room_name, room_details, room_options, looked, hp, stick, approach)     

  elif looked == True and "root" in choice:
      stick = True
      room_details = "You grab an old, dry root, looks like you can use it as a spear."
      room_options = ["Move away from the imp!"]

      return genReturn(200, "Moved in the imp room", room_name, room_details, room_options, looked, hp, stick, approach) 

  
  elif looked == False and impCheck(approach) == False and "move" in choice:
      approach += 1
      if approach >= 10:
        room_details = "An imp appears in front of you! It swings at you and draws blood!"
        hp -= 10
        room_options = ["Look."]

      else: 
        room_details= "You move further into the room, staring at the ceiling. The splashing shound gets louder, it sounds like footsteps.\n"
        room_options = ["Look.",
            "Move towards the sound."]

      return genReturn(200, "Moved in the imp room", room_name, room_details, room_options, looked, hp, stick, approach) 
  
  else:
    room_details = "I dont understand what you're trying to do."
    room_options = ["Look.", "Move towards the sound."]
    
    return genReturn(301, "Invalid Choice", room_name, room_details, room_options, looked, hp, stick, approach) 

