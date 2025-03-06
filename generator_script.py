def username_generator(first_name, last_name):
  if len(first_name) >= 3:
    user_fname = first_name[0:3]
  else:
    user_fname = first_name
  if len(last_name) >= 4:
    user_lname = last_name[0:4]
  else:
    user_lname = last_name
  user_name = user_fname + user_lname
  return user_name

def password_generator():
  pass

# output
print(username_generator('Pepper', 'Jack'))
print(username_generator('Dr', 'Wei'))