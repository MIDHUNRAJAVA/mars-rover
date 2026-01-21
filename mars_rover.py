import sys

class MarsRover:
    """
    Mars Rover controller that operates on a rectangular grid.
    """
    def __init__(self, width, height, start_x, start_y):
        """
        Initialize the rover with grid dimensions and starting position.
        
        Args:
            width (int): Width of the grid (x-axis size)
            height (int): Height of the grid (y-axis size)
            start_x (int): Starting x coordinate
            start_y (int): Starting y coordinate
        """
        self.width = width
        self.height = height
        self.x = start_x
        self.y = start_y

    def execute(self, commands):
        """
        Execute a sequence of commands.
        
        Args:
            commands (str): String containing commands 'U', 'D', 'L', 'R'
        """
        print("\nExecution:\n")
        for command in commands:
            self._move(command.upper())
        print(f"\nFinal Position: ({self.x},{self.y})")

    def _move(self, command):
        """
        Process a single move command.
        
        Args:
            command (char): The command character
        """
        new_x, new_y = self.x, self.y
        
        if command == 'U':
            new_y += 1
        elif command == 'D':
            new_y -= 1
        elif command == 'R':
            new_x += 1
        elif command == 'L':
            new_x -= 1
        else:
            # Ignore invalid characters or handle them if needed
            return

        # Check boundary conditions
        if self._is_valid(new_x, new_y):
            self.x, self.y = new_x, new_y
            print(f"Executing {command} -> ({self.x},{self.y})")
        else:
            print(f"Executing {command} -> ({self.x},{self.y}) [Blocked - boundary]")

    def _is_valid(self, x, y):
        """
        Check if the coordinates are within the grid boundaries.
        
        Args:
            x (int): x coordinate
            y (int): y coordinate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Assuming 0-indexed grid: 0 <= x < width, 0 <= y < height
        return 0 <= x < self.width and 0 <= y < self.height

def parse_input():
    """
    Helper function to parse input from console.
    Supports inputs with or without labels (e.g., "Grid size: 10 x 8" or "10 x 8")
    """
    try:
        print("Enter inputs (you can paste the lines from the example):")
        
        # 1. Grid Size
        # Example input: "Grid size: 10 x 8" or just "10 x 8"
        raw_grid = input("Enter grid size (n x m): ")
        # Handle case where user pastes "Grid size: ..."
        if ':' in raw_grid:
            grid_val = raw_grid.split(':')[-1].strip()
        else:
            grid_val = raw_grid.strip()
            
        width, height = map(int, grid_val.lower().split('x'))

        # 2. Starting Position
        # Example input: "Starting position: (0, 0)" or "(0, 0)"
        raw_pos = input("Enter starting position (x, y): ")
        if ':' in raw_pos:
            pos_val = raw_pos.split(':')[-1].strip()
        else:
            pos_val = raw_pos.strip()
            
        pos_val = pos_val.replace('(', '').replace(')', '')
        start_x, start_y = map(int, pos_val.split(','))

        # 3. Commands
        # Example input: "Commands: RRUURL" or "RRUURL"
        raw_cmd = input("Enter commands: ")
        if ':' in raw_cmd:
            commands = raw_cmd.split(':')[-1].strip()
        else:
            commands = raw_cmd.strip()
        
        return width, height, start_x, start_y, commands

    except ValueError as e:
        print(f"\nError parsing input: {e}")
        print("Please ensure format is correct (e.g., '10 x 8', '(0, 0)', 'RRUURL')")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Main driver code
    width, height, start_x, start_y, commands = parse_input()
    
    rover = MarsRover(width, height, start_x, start_y)
    rover.execute(commands)
