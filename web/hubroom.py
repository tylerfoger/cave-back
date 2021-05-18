def genReturn(status, msg, room_name, room_details, room_options, looked = False, trap = True):
  retJson = {
    "status": status,
    "msg": msg,
    "data": {
      "room_name": room_name,
      "room_details": room_details,
      "room_options": room_options,
      "looked" : looked,
      "trap": trap
    }
  }
  return retJson

def hub(choice, looked, trap):
  room_name = 'hubroom'
  if trap == True and ("straight" in choice or "left" in choice or "right" in choice or "on" in choice):
    room_details = "The floor gives away and you are impaled on spikes 20 feet below."
    room_options = ["You died. Press the reset button to try again."]
    
    return genReturn(302, "Fell into trap", room_name, room_details, room_options)

  if "look" in choice:
    room_details = "You see a large plate in the middle of the room."
    room_options = [
      "Step Around the plate.",
      "Step on the plate.",
      "Left.",
      "Right.",
      "Straight."
    ]
    if looked == True: 
      room_options = [
        "You've already looked around.",
        "Step around the plate.",
        "Step on the plate",
        "Left.",
        "Right.",
        "Straight."
      ]
    looked = True

    return genReturn(200, "Looked", room_name, room_details, room_options, looked, trap)
            
  if "around" in choice:
    room_details = "You step around the strange pattern, do you go Left, Right, or Straight?"
    trap = False
    room_options = ["Left.", "Right.", "Straight."]

    return genReturn(200, "Disabled Trap", room_name, room_details, room_options, looked, trap)

  if trap == False and "left" in choice:
    retJson = {
      "status": 200,
      "msg": "Enter Imp Room",
      "data": {
        "room_name": "improom",
        "room_details": "You enter a very large room. The sound of splashing water echoes faintly in the distance.",
        "room_options": [
          "Look.",
          "Move towards the sound.",
        ],
        "looked": False,
        "hp": 20,
        "stick": False,
        "approach": 4              
      },
    }
    return retJson  

  if trap == False and "right" in choice:
    retJson = {
      "status": 200,
      "msg": "Enter Jar Room",
      "data": {
        "room_name": "jarroom",
        "room_details": "On the right side of the room there is a fissure that splits the cave in two, barely large enough for you to fit through. You have to take your armor off in order to squeeze through the gap. As you reach the other side, you hear a swirling rattle. On your left you see a large purple jar, it's billowing smoke. On the ground beside the jar, you see an ornate cork. In the center of the room swirls a pile of bones, a skeleton looks to be forming in the middle.",
        "room_options": [
          "Kick over the jar.",
          "Plug the jar.",
          "Try and disrupt the bones."],
        "looked": False
      },
    }
    return retJson  

  if trap == False and "straight" in choice:
    retJson = {
      "status": 200,
      "msg": "Die of starvation in the Boss Room",
      "data": {
        "room_name": "bossroom",
        "room_details": "It's completely dark, you can't see anything! You wander around in the dark until you starve.",
        "room_options": ["Click the Reset button to try again."],
        "looked": False,
        "stick": False,
        "hp": 20,
      },
    }
    return retJson  

  else:
    room_details = "I dont understand what you're trying to do."
    room_options = [
        "Left.",
        "Right.",
        "Straight."
      ]
    if looked == True:
       room_options = [
        "Step around the plate.",
        "Step on the plate.",
        "Left.",
        "Right.",
        "Straight."
      ]
    
    return genReturn(301, "Invalid Choice", room_name, room_details, room_options)   

            