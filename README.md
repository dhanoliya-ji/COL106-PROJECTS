### 🟡 Pac-Man in Maze World
### Project | August 5, 2024

Welcome to the Pac-Man in Maze World project, where we help our favorite yellow hero navigate through a haunted maze filled with ghosts using the power of stacks! This project brings together concepts of 2D grid modeling, stacks, and algorithmic thinking to guide Pac-Man safely to his destination.
<br>
<br>
### 🎮 About the Project<br>

Pac-Man is trapped in a haunted maze with ghosts lurking at every turn. Your task is to design a navigation system that finds a safe path for Pac-Man to his favorite destination while avoiding ghosts.<br>
&#8226; The maze is represented as a 2D grid of cells.<br>
&#8226; Vacant cells are marked as 0, and cells with ghosts are marked as 1.<br>
&#8226; Pac-Man can only move through vacant cells and cannot revisit any cell along his path.<br>

### 🔧 Features<br>
### 🏞️ Maze<br>

The Maze class represents the haunted maze with the following functionalities:<br>
&#8226; Add Ghosts: Place ghosts in the maze.<br>
&#8226; Remove Ghosts: Remove ghosts from specific cells.<br>
&#8226; Check Cells: Verify whether a specific cell contains a ghost.<br>
&#8226; Print Grid: Visualize the maze layout as a grid.<br>

<p align="center" style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://github.com/user-attachments/assets/9b287dcc-54a0-4758-8bc0-667b36eb884e" alt="Image 1" width="400"/>
  <img src="https://github.com/user-attachments/assets/c332495e-b0b9-4d34-96d2-a993690e244f" alt="Image 2" width="400"/>
</p>



### 🧭 Navigator<br>


The Navigator class calculates the safest path for Pac-Man:
&#8226; Pathfinding Algorithm: Uses stack-based navigation to find the path from the start to the end cell.<br>
&#8226; Path Validity: Ensures Pac-Man doesn’t revisit cells or walk into ghosts.<br>
&#8226; Efficient Search: Guarantees a time complexity of O(n × m) for an n × m maze.<br>
&#8226; Exception Handling: Raises a PathNotFoundException if no valid path exists.<br>

### 📦 Stack<br>

A custom Stack implementation forms the backbone of this project:<br>
&#8226; Dynamic Growth: Built using growable arrays.<br>
&#8226; Intuitive Operations: Push, pop, and peek functionalities to track Pac-Man's moves in the maze.<br>

### 🚀 How It Works<br>

1.Maze Setup:<br>
&#8226; Define the maze dimensions.<br>
&#8226; Add or remove ghosts using the Maze class.<br>

2.Pathfinding:<br>
&#8226; Use the Navigator to find a path from Pac-Man's starting position to his destination.<br>
&#8226; Handle edge cases such as invalid start or end cells.<br>

3.Visualization:<br>
&#8226; Print the maze layout and the path taken by Pac-Man.<br>

### 📝 Sample Maze & Path<br>

Maze Grid:
0 1 0 0  
0 0 0 0  
0 0 1 0  
0 1 0 0  

Start: (2, 0)  
End: (2, 3)  

Valid Path: [(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3)]<br>
<br>
### 🛠️ Technologies Used<br>

&#8226; Python (for implementation)<br>
&#8226; Object-Oriented Programming<br>
&#8226; Stack Data Structure<br>

### 📁 File Structure<br>

&#8226; maze.py<br>
Implements the Maze class, managing the maze layout and operations like adding or removing ghosts.

&#8226; stack.py<br>
Defines a custom Stack class used for the maze navigation algorithm.

&#8226; navigator.py<br>
Contains the Navigator class, which implements the pathfinding logic using stacks.

&#8226; exception.py<br>
Provides the PathNotFoundException. (This file should not be modified.)

&#8226; main.py<br>
Serves as the main entry point for testing and debugging the code.




