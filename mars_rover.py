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
            print("Invalid character, please enter U, D, L, R")
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
    Parses simple space-separated console input.

    Expected Input:
    Grid size:        n m
    Starting position: x y
    Commands:         string (U, D, L, R)
    """
    try:
        print("Enter inputs:")

        # 1. Grid size
        n, m = map(int, input("Enter grid size (n m): ").split())

        # 2. Starting position
        start_x, start_y = map(int, input("Enter starting position (x y): ").split())

        # 3. Commands
        commands = input("Enter commands: ").strip().upper()

        return n, m, start_x, start_y, commands

    except ValueError:
        print("\n❌ Invalid input format.")
        print("Expected:")
        print("Grid size      -> n m")
        print("Start position -> x y")
        print("Commands       -> RRUURL")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Main driver code
    width, height, start_x, start_y, commands = parse_input()
    
    rover = MarsRover(width, height, start_x, start_y)
    rover.execute(commands)
