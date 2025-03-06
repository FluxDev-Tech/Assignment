def movie_ticket_price(age):
  if age < 12:
    return 100
  elif 13 <= age <= 19:
    return 150
  elif 20 <= age <= 59:
    return 200
  else:
    return 120
