# Bridge Builder
Bridge Builder is a simple CLI colored game made in Python. 

## How to win
To win in this game, the valid bridge must be built. The bridge is valid if top line doesn't have spaces, and other lines have at least 3 different types of block.

## Features
 - You have only one attempt
 - You cannot remove placed blocks
 - If you lose, the score will be 0
 - The map is flat, but generated with different elevation
 - Multiple game profiles supported
 - Full keyboard controls, no `input()` function
 - Colored text with [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code)

## Technologies used
 - [Python](https://www.python.org/)
 - [SQLite](https://www.sqlite.org/)
 - [Pynput](https://github.com/moses-palmer/pynput)
 - [Pyinstaller](https://pyinstaller.org/en/stable/)
 - [Colorama](https://github.com/tartley/colorama)
