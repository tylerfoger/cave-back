def genReturn(status, msg, room_name, room_details, room_options, looked, hp, stick):
  retJson = {
    "status": status,
    "msg": msg,
    "data": {
      "room_name": room_name,
      "room_details": room_details,
      "room_options": room_options,
      "looked" : looked,
      "hp": hp,
      "stick": stick
    }
  }
  return retJson

def boss(choice, looked, stick, hp):
  room_name = "bossroom"

  if hp <= 0:
    room_details = "You are killed by the shadow."
    room_options = ["You're dead, hit the reset button to try again."]

    return genReturn(302, "Killed by the Shadow", room_name, room_details, room_options, looked, hp, stick)

  if stick == False:
    room_details = "It's completely dark, you can't see anything! You wander around in the dark until you starve."
    room_options = ["Click the Reset button to try again."]
        
    return genReturn(302, "Die of starvation in boss room", room_name, room_details, room_options, looked, hp, stick) 

  if "look" in choice:
    room_details = "The walls of the room are bare, all that you can see is your shadow reflecting off the walls. You search for an exit for a few hours, but come up with nothing. As you are about to give up hope, you notice that your shadow isn't exactly mirroring your actions. The shadow stops moving completely and appears to grow darker. The wall almost looks like it's covered in ink. First a ripple forms on the surface, then suddenly a pitch black mirror image of yourself pushes itself away from the wall and lunges at you."
    room_options = ["Back up.",
      "Put out your light.",]
    
    if looked == True:
      room_options = ["You've already looked around!",      
      "Back up.",
      "Put out your light."]
    looked = True

    return genReturn(200, "Already looked around the boss room", room_name, room_details, room_options, looked, hp, stick) 

  elif "back" in choice:
    hp -= 10
    room_details =  f"You try and back up, but the room is small and there's nowhere to go, the shadow reaches out and grabs you. The shadow does 10 HP worth of damage, you only have {hp} remaining!"
    room_options = ["Back up.",
      "Put out your light.",]

    return genReturn(200, "Shadow attacks you", room_name, room_details, room_options, looked, hp, stick) 

  if looked == True and "out" in choice:
    room_details = "You put out your torch! 'Hey, I can't see anything!' cries a voice, clearly distressed. 'I want to get out of here, I'm scared!'. The shadow creature begins yelling in an undecipherable dialect and pounding on the walls. In the total darkness you can only cower and cover your head as the ceiling begins to collapse, after a few tense moments, the pounding stops and you are blinded by a brilliant glow - it's the outside! You survived!"
    room_options = ["Congratulations, you win!"]

    return genReturn(200, "You win!", room_name, room_details, room_options, looked, hp, stick) 

  else:
    room_details = "I dont understand what you're trying to do."
    room_options = ["Look."]
    
    return genReturn(301, "Invalid Choice", room_name, room_details, room_options, looked, hp, stick) 
