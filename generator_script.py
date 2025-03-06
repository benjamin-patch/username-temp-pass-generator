# generate username
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

# generate password
def password_generator(user_name):
  last_char = user_name[-1]
  remaining_chars = user_name[:-1]
  password = last_char + remaining_chars
  return password

# inputs
print(username_generator('Pepper', 'Jack'))
print(password_generator('PepJack'))

print(username_generator('Dr', 'Wei'))
print(password_generator('DrWei'))

print(username_generator('Abe', 'Simpson'))
print(password_generator('AbeSimp'))