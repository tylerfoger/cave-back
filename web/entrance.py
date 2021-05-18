def genReturn(status, msg, room_name, room_details, room_options, looked = False):
  retJson = {
    "status": status,
    "msg": msg,
    "data": {
      "room_name": room_name,
      "room_details": room_details,
      "room_options": room_options,
      "looked" : looked
    }
  }
  return retJson

def enter(choice, looked):
  room_name = 'entrance'
  
  if "look" in choice:
    room_details = "You are standing in front of a large door hewn from the rock face. There is a loose boulder above it. It doesnt look very inviting."
    room_options = [
      "Push boulder.",
      "Enter."
    ]
    if looked == True:  
      room_options = [
        "You've already looked around.",
        "Push boulder.", 
        "Enter."
      ]
    looked = True
    
    return genReturn(200, "Looked", room_name, room_details, room_options, looked)

  elif "boulder" in choice:
    room_details = "You push the boulder and it blocks the entrance! Your curiosity got the best of you and you sealed the cave forever."
    room_options = ["Press the Reset Button to Start again."]

    return genReturn(302, "Blocked the cave, gg", room_name, room_details, room_options)

  elif choice == "enter":
    retJson = {
      "status": 200,
      "msg": "go to hubroom",
      "data": {
        "room_name": "hubroom",
        "room_details": "You enter the cave. There are three ways before you. What do you do?",
        "room_options": [
          "Look.",
          "Left.",
          "Right.",
          "Straight." 
          ],
        "trap": True,
        "looked": False
      },
    }
    return retJson       

  else:
    room_details = "I dont understand what you're trying to do."
    room_options = ["Look.", "Enter."]
    
    return genReturn(301, "Invalid Choice", room_name, room_details, room_options)