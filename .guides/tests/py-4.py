
maze = False
player = False
monsterCount = 0
energyCount = 0
wallCount = 0

def createEmptyMaze():
  global maze
  maze = True

def addPlayer():
  global player
  player = True

def addGoal():
  global goal
  goal = True  
  
def addMonster(x, y):
  global monsterCount
  
  if x == 6 and y == 5:
    monsterCount += 1

def addEnergy(x, y):
  global energyCount
  
  if (x == 5 and y == 3) or (x == 7 and y == 4):
    energyCount += 1

def addWall(x, y):
  global wallCount
  
  if x == 2 and y == 2:
    wallCount += 1

try:
  execfile('/home/codio/workspace/public/content/py/py-4.py')

  if maze == True and player == True and goal == True and monsterCount == 1 and energyCount == 2 and wallCount == 1:
    print 'well done'
    exit(0)
except (IOError, SyntaxError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
