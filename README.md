# Mars Rover Navigation System

A console-based Mars Rover navigation program that simulates rover movement on a rectangular grid.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Functional Requirements](#functional-requirements)
- [Constraints](#constraints)
- [Approach and Algorithm](#approach-and-algorithm)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Code Structure](#code-structure)

## Problem Statement

You are controlling a Mars Rover that operates on a flat rectangular grid. The rover receives movement commands and executes them sequentially while respecting grid boundaries.

## Functional Requirements

### 1. Grid System
- **FR-1.1**: The system shall represent the Mars surface as an n × m rectangular grid
- **FR-1.2**: The grid shall use a coordinate system where:
  - x-axis represents horizontal position (0 to n-1)
  - y-axis represents vertical position (0 to m-1)
- **FR-1.3**: The grid shall be zero-indexed (starting from 0, 0)

### 2. Rover Initialization
- **FR-2.1**: The rover shall be initialized with a starting position (x, y)
- **FR-2.2**: The starting position must be within the grid boundaries
- **FR-2.3**: The rover shall accept grid dimensions (width × height)

### 3. Movement Commands
- **FR-3.1**: The rover shall support four directional commands:
  - `U` → Move Up (y + 1)
  - `D` → Move Down (y - 1)
  - `R` → Move Right (x + 1)
  - `L` → Move Left (x - 1)
- **FR-3.2**: Commands shall be provided as a single string (e.g., "RRUURL")
- **FR-3.3**: Commands shall be case-insensitive
- **FR-3.4**: Commands shall be executed sequentially from left to right

### 4. Boundary Handling
- **FR-4.1**: The rover shall not move outside the grid boundaries
- **FR-4.2**: If a command would cause the rover to cross a boundary:
  - The command shall be ignored
  - The rover shall remain in its current position
  - The system shall report the command as "Blocked - boundary"

### 5. Output Requirements
- **FR-5.1**: The system shall print the rover's position after each command execution
- **FR-5.2**: For valid moves, output format: `Executing {command} -> ({x},{y})`
- **FR-5.3**: For blocked moves, output format: `Executing {command} -> ({x},{y}) [Blocked - boundary]`
- **FR-5.4**: The system shall print the final position after all commands: `Final Position: ({x},{y})`

### 6. Input Handling
- **FR-6.1**: The system shall accept input in three parts:
  1. Grid size in format "n x m" or "Grid size: n x m"
  2. Starting position in format "(x, y)" or "Starting position: (x, y)"
  3. Commands in format "COMMANDS" or "Commands: COMMANDS"
- **FR-6.2**: The system shall handle parsing errors gracefully with informative error messages

## Constraints

### Technical Constraints
- **TC-1**: Grid dimensions must be positive integers (n > 0, m > 0)
- **TC-2**: Coordinates must be non-negative integers
- **TC-3**: Starting position must satisfy: 0 ≤ x < width AND 0 ≤ y < height
- **TC-4**: Only valid command characters are U, D, L, R (case-insensitive)
- **TC-5**: Invalid command characters shall be silently ignored

### Boundary Constraints
- **BC-1**: Minimum x-coordinate: 0
- **BC-2**: Maximum x-coordinate: width - 1
- **BC-3**: Minimum y-coordinate: 0
- **BC-4**: Maximum y-coordinate: height - 1

### Performance Constraints
- **PC-1**: The system shall execute commands in O(n) time where n is the number of commands
- **PC-2**: The system shall use O(1) space for rover state

## Approach and Algorithm

### High-Level Architecture

The solution follows an object-oriented design with three main components:

1. **MarsRover Class**: Core rover logic and state management
2. **Input Parser**: User input handling and validation
3. **Main Driver**: Program execution flow

### Algorithm Step-by-Step

#### Initialization Phase

```
1. Read grid dimensions (width, height)
2. Read starting position (start_x, start_y)
3. Validate that starting position is within grid bounds
4. Initialize rover with:
   - grid_width = width
   - grid_height = height
   - current_x = start_x
   - current_y = start_y
5. Read command string
```

#### Command Execution Phase

```
For each command character in the command string:
    1. Convert command to uppercase (for case-insensitivity)
    
    2. Calculate new position based on command:
       - If command == 'U': new_y = current_y + 1
       - If command == 'D': new_y = current_y - 1
       - If command == 'R': new_x = current_x + 1
       - If command == 'L': new_x = current_x - 1
       - Else: Skip invalid command
    
    3. Validate new position:
       - Check if 0 <= new_x < grid_width
       - Check if 0 <= new_y < grid_height
    
    4. If valid:
       - Update rover position: current_x = new_x, current_y = new_y
       - Print: "Executing {command} -> ({current_x},{current_y})"
    
    5. If invalid (boundary violation):
       - Keep current position unchanged
       - Print: "Executing {command} -> ({current_x},{current_y}) [Blocked - boundary]"

After all commands executed:
    Print: "Final Position: ({current_x},{current_y})"
```

#### Boundary Validation Algorithm

```python
def is_valid_position(x, y, width, height):
    """
    Returns True if position is within grid boundaries
    """
    return (0 <= x < width) AND (0 <= y < height)
```

### Design Decisions

1. **Zero-Indexed Grid**: Grid coordinates start from (0, 0) to (width-1, height-1)
2. **Immutability of Invalid Moves**: Position never changes for invalid commands
3. **Command Tolerance**: Invalid characters are ignored rather than causing errors
4. **Flexible Input Parsing**: Supports both raw values and labeled inputs

### Time and Space Complexity

- **Time Complexity**: O(n) where n is the number of commands
  - Each command is processed exactly once
  - Position validation is O(1)
  
- **Space Complexity**: O(1)
  - Only stores rover's current state (x, y, width, height)
  - Does not store command history or path

## Installation

### Prerequisites

- Python 3.6 or higher

### Steps

1. Clone the repository:
```bash
git clone https://github.com/MIDHUNRAJAVA/mars-rover.git
cd mars-rover
```

2. No additional dependencies required (uses only Python standard library)

## Usage

### Running the Program

```bash
python3 mars_rover.py
```

### Input Format

The program accepts input in the following order:

1. **Grid Size**: Enter as "n x m" (e.g., "10 x 8")
2. **Starting Position**: Enter as "(x, y)" (e.g., "(0, 0)")
3. **Commands**: Enter as a string of commands (e.g., "RRUURL")

You can also include labels in your input:
- "Grid size: 10 x 8"
- "Starting position: (0, 0)"
- "Commands: RRUURL"

## Examples

### Example 1: Successful Navigation

**Input:**
```
Grid size: 10 x 8
Starting position: (0, 0)
Commands: RRUURL
```

**Output:**
```
Execution:

Executing R -> (1,0)
Executing R -> (2,0)
Executing U -> (2,1)
Executing U -> (2,2)
Executing R -> (3,2)
Executing L -> (2,2)

Final Position: (2,2)
```

**Explanation:**
- Start at (0,0)
- R: Move right to (1,0)
- R: Move right to (2,0)
- U: Move up to (2,1)
- U: Move up to (2,2)
- R: Move right to (3,2)
- L: Move left to (2,2)

### Example 2: Boundary Blocking

**Input:**
```
Grid size: 5 x 5
Starting position: (0, 0)
Commands: LLD
```

**Output:**
```
Execution:

Executing L -> (0,0) [Blocked - boundary]
Executing L -> (0,0) [Blocked - boundary]
Executing D -> (0,0) [Blocked - boundary]

Final Position: (0,0)
```

**Explanation:**
- Start at (0,0) - bottom-left corner
- L: Cannot move left (x would be -1) - BLOCKED
- L: Cannot move left (x would be -1) - BLOCKED
- D: Cannot move down (y would be -1) - BLOCKED
- Rover stays at (0,0)

### Example 3: Mixed Valid and Invalid Moves

**Input:**
```
Grid size: 3 x 3
Starting position: (1, 1)
Commands: UURRDDD
```

**Output:**
```
Execution:

Executing U -> (1,2)
Executing U -> (1,2) [Blocked - boundary]
Executing R -> (2,2)
Executing R -> (2,2) [Blocked - boundary]
Executing D -> (2,1)
Executing D -> (2,0)
Executing D -> (2,0) [Blocked - boundary]

Final Position: (2,0)
```

## Code Structure

### Classes and Methods

#### `MarsRover` Class

**Attributes:**
- `width`: Grid width (x-axis size)
- `height`: Grid height (y-axis size)
- `x`: Current x-coordinate
- `y`: Current y-coordinate

**Methods:**

1. `__init__(self, width, height, start_x, start_y)`
   - Initializes the rover with grid dimensions and starting position

2. `execute(self, commands)`
   - Executes a sequence of movement commands
   - Prints execution trace and final position

3. `_move(self, command)`
   - Processes a single movement command
   - Updates position if valid, otherwise reports blocked

4. `_is_valid(self, x, y)`
   - Validates if coordinates are within grid boundaries
   - Returns boolean

#### Helper Functions

1. `parse_input()`
   - Parses user input from console
   - Supports flexible input formats with or without labels
   - Returns: (width, height, start_x, start_y, commands)

### Main Execution Flow

```python
if __name__ == "__main__":
    # 1. Parse input
    width, height, start_x, start_y, commands = parse_input()
    
    # 2. Initialize rover
    rover = MarsRover(width, height, start_x, start_y)
    
    # 3. Execute commands
    rover.execute(commands)
```

## Testing

To test the implementation, you can use the provided examples:

```bash
# Test Example 1
echo -e "10 x 8\n(0, 0)\nRRUURL" | python3 mars_rover.py

# Test Example 2
echo -e "5 x 5\n(0, 0)\nLLD" | python3 mars_rover.py
```

## Error Handling

The program handles the following error scenarios:

1. **Invalid Input Format**: Clear error messages guide users to correct format
2. **Invalid Command Characters**: Silently ignored, execution continues
3. **Boundary Violations**: Reported but do not cause program termination
4. **Unexpected Errors**: Caught and reported with helpful messages

## Future Enhancements

Potential improvements to consider:

1. **Obstacle Handling**: Add support for obstacles on the grid
2. **Path History**: Store and display the complete path taken
3. **Visualization**: Add ASCII art or GUI visualization of rover movement
4. **Batch Mode**: Support reading multiple test cases from a file
5. **Direction Tracking**: Track which direction the rover is facing
6. **Advanced Commands**: Add rotation (turn left/right) and multi-step moves
7. **Grid Wrapping**: Optional mode where rover wraps around grid edges
8. **Performance Metrics**: Track statistics like successful moves, blocked moves, etc.

## License

This project is provided as-is for educational purposes.

## Author

MIDHUNRAJAVA

## Contributing

Feel free to submit issues or pull requests for improvements.
