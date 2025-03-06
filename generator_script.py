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

# input

# user 1
user1_fname = 'Pepper'
user1_lname = 'Jack'
user1_username = username_generator(user1_fname, user1_lname)
user1_temp_pass = password_generator(user1_username)
# user 2
user2_fname = 'Dr'
user2_lname = 'Wei'
user2_username = username_generator(user2_fname, user2_lname)
user2_temp_pass = password_generator(user2_username)
# user 3
user3_fname = 'Abe'
user3_lname = 'Simpson'
user3_username = username_generator(user3_fname, user3_lname)
user3_temp_pass = password_generator(user3_username)

# output

# user 1
print('Username:', user1_username)
print('Temp Password:', user1_temp_pass)

# user 2
print('Username:', user2_username)
print('Temp Password:', user2_temp_pass)

# user 3
print('Username:', user3_username)
print('Temp Password:', user3_temp_pass)