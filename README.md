# Game Of Life Problem

* The "game" is a zero-player game, meaning that its evolution is determined by its initial state,
requiring no further input. One interacts with the Game of Life by creating an initial configuration
and observing how it evolves.

* See the complete problem statement in problem.pdf

## Points To Note

* For simplicity sake, the universe generation is started from cell (0,0) and goes till cell (n,n).
* The user inputs the size of the universe and number of generations to run.
* The user inputs the initial seed system/genesis universe.
* Numpy library is used to pretty print the Matrix/universe.
* A live cell is denoted by '*'
* A dead cell is denoted by '0'

## Getting Started
Run the code using ```python3 gameOfLife.py```

## Example Input/Output

```
----- Welcome To The Game Of Life -----
Please Enter Size of The Universe/Matrix/Grid:
10
Please Enter the values in the Universe/Matrix where you want a cell to live (rest all cells would be empty/dead):
Enter 'done' to start generation!
5 5
[['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']]
5 6
.
.
.
0 5
[['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '*' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']]
done
Please Enter number of generations:
100


---Initial Universe/seed system---
[['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '*' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']]


Matrix After Generation 1:
[['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '*' '0' '0' '0']
 ['0' '0' '0' '0' '*' '0' '*' '0' '0' '0']
 ['0' '0' '0' '0' '0' '*' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' '0' '0']]
.
.
.
continues till Generation 100
```

