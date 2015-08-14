
import json
  
try:
  with open('/home/codio/workspace/stack.json') as json_file:
    data = json.load(json_file)
    
    if data['wallCount'] == 4 and data['score'] > 10:
      print 'well done'
      exit(0)
      
except (IOError, SyntaxError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
