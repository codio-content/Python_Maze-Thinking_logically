Here are the Python function names available to you

- `createEmptyMaze()`
- `addPlayer()`
- `addGoal()`
- `addWall()`
- `addEnergy()`
- `addMonster()`

{Check It!|assessment}(test-2553177547)

|||guidance
## Solution

The ordering of the various "Add" functions is not essential, as long as they come after `createEmptyMaze`.

```python
createEmptyMaze()
addWall(2, 2)
addMonster(6, 5)
addEnergy(5, 3)
addEnergy(7, 4)
addPlayer()
addGoal()
```

|||
