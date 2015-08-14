
maze = False
player = False
monsterCount = False

def createEmptyMaze():
  global maze
  maze = True

def addRandomMonsters(count):
  global monsterCount
  monsterCount = count

def addPlayer():
  global player
  player = True

try:
  execfile('/home/codio/workspace/public/content/py/py-2.py')
  
  if maze == True and monsterCount == 3:
    print 'well done'
    exit(0)
except (IOError, SyntaxError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
