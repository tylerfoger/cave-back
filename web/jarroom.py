def genReturn(status, msg, room_name, room_details, room_options):
  retJson = {
    "status": status,
    "msg": msg,
    "data": {
      "room_name": room_name,
      "room_details": room_details,
      "room_options": room_options,
      "looked": False
    }
  }
  return retJson

def jar(choice):
  room_name = "jarroom"

  if "kick" in choice:
    room_details = "You kick the jar over - it shatters! Smoke starts to come out even faster.You see your life flash before your eyes on the reflection of the shards as dozens of skeletons appear. Your flesh gets ripped from your bones, as your rise against your will as an animated skeleton."
    room_options = ["You're dead, click reset to try again."]

    return genReturn(301, "Kicked Jar", room_name, room_details, room_options) 

  elif "plug" in choice:
    retJson = {
    "status": 205,
    "msg": "go to improom",
    "data": {
      "room_name": "bossroom",
      "room_details": "You plug the jar with the ornate cork. The smoke stops coming out of the jar. The unfinished skeleton in the center of the room crawls towards you. You're easily able to rekt the skeleton and it collapses to the floor. There's yet another door inside this room. You grab a torch laying on the ground - light it, then enter the room. The door slams behind you! The torch you found in the previous room comes in handy, this room would be pitch black without it.",
      "room_options": [
   "Look."],
      "looked": False,
      "stick": True,
      "hp": 20
      }
    }
    return retJson 

  elif ("bones" or "disrupt") in choice:
    room_details = "You can't pull the bones from the skeleton fast enough, it keep building up.The thick smoke is suffocating!"
    room_options = [
      "Kick over the jar.",
      "Plug the jar."]

    return genReturn(301, "messed with the bones", room_name, room_details, room_options)

  elif "consume" in choice:
    room_details = "You eat the bones, but they keep forming faster than you can keep up. The thick smoke is suffocating!"
    room_options = [
      "Kick over the jar.",
      "Plug the jar.",
      "Try and disrupt the bones."]

    return genReturn(301, "Consumed bones", room_name, room_details, room_options)
    
  else:
    room_details = "I dont understand what you're trying to do."
    room_options = [
      "Kick over the jar.",
      "Plug the jar.",
      "Try and disrupt the bones."]
    
    return genReturn(301, "Invalid Choice", room_name, room_details, room_options) 