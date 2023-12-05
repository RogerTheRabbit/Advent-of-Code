
import os

input = ""
print("Current directory:", os.getcwd())
with open("./2023/Day 2/input.txt", "r") as f:
  input = f.readlines()


allowedR = 12
allowedG = 13
allowedB = 14

class Round:
  r=0
  g=0
  b=0

  def __init__(self, line):
    for color in line.split(","):
      match color.strip().split()[1]:
        case 'red':
          self.r = self.r + int(color.strip().split()[0])
        case 'green':
          self.g = self.g + int(color.strip().split()[0])
        case 'blue':
          self.b = self.b + int(color.strip().split()[0])
        case _:
          print("ERROR")


class Game:
  id=0
  rounds = None

  def __init__(self, line):
    self.id=int(line.split(" ")[1].strip(":"))
    self.rounds=[Round(round) for round in line.split(":")[1].split(";")]
  
  def getPower(self):
    maxR = 0
    maxG = 0
    maxB = 0
    for round in self.rounds:
      maxR = max(maxR, round.r)
      maxG = max(maxG, round.g)
      maxB = max(maxB, round.b)
    return maxR * maxG * maxB

def isValid(game: Game):
  return all([round.r <= allowedR and round.g <= allowedG and round.b <= allowedB for round in game.rounds])

games = [Game(game) for game in input]

# Part 1
print(sum([game.id if isValid(game) else 0 for game in games]))

# Part 2
print(sum([game.getPower() for game in games]))
