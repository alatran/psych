import random

def select(file):
  with open(file, 'r') as f:
    words = f.readlines()
    words = [word.strip for word in words if word.strip()]
  return random.choice(words) if words else None

rand_word = select(exam2.txt)
print(f"Word: {rand_word}")
