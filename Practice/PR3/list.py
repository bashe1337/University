import random

with open('words.txt', encoding="utf-8") as file:
   words = file.read().split()
def whatWord():
   if len(words) != 0:
      choose = random.choice(words)
      words.remove(choose)
      return(choose)
   else:
      return('stop')