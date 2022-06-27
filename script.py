def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print(f"Alright, that's a {size} {drink_type}!")
  name = input("Can I get your name please? ")
  print(f"Thanks, {name}! Your drink will be ready shortly.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  print_message = "I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response."
  if res.lower() == "a":
    return "Small"
  elif res.lower() == "b":
    return "Medium"
  elif res.lower() == "c":
    return "Large"
  else:
    print(print_message)
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  print_message = "No, seriously"
  if res.lower() == "a":
    return "Brewed Coffee"
  elif res.lower() == "b":
    return "Mocha"
  elif res.lower() == "c":
    return order_latte() + " Latte"
  else:
    print(print_message)
    return get_drink_type()

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  print_message = "..."
  if res.lower() == "a":
    return "2% milk"
  elif res.lower() == "b":
    return "Non-fat milk"
  elif res.lower() == "c":
    return "Soy milk"
  else:
    print(print_message)
    return order_latte()

coffee_bot()
