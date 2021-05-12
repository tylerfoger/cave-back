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