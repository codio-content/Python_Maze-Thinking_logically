
Here are the Python function names available to you

- `createEmptyMaze()`
- `addPlayer()`
- `addGoal()`
- `addWall()`
- `addEnergy()`
- `addMonster()`

|||challenge
Using Python again, we want you to create a game that meets the following criteria.

1. At least 4 walls.
1. When you play the game, you need to have achieved a score of at least **10** when you reach the goal.

**Hint:** you will need some extra energy stores in the game to get the score.

When you have played and finished the games, press the button.

{Check It!!|custom}(py-5)
|||


|||guidance
## Solution

The ordering of the various "Add" functions is not essential, as long as they come after `createEmptyMaze`. The solution will need to include enough energy stores to increase the score to meet the requirement when the goal is reached.

```python
createEmptyMaze()
addWall()
addWall()
addWall()
addWall()
addEnergy()
addEnergy()
addEnergy()
addEnergy()
addEnergy()
addEnergy()
addEnergy()
addEnergy()
addEnergy()
addEnergy()
addPlayer()
addGoal()
```