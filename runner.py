import sys
import importlib.util

def run_solution(problem_file_path):
    """
    Dynamically loads and runs the solution from a given Python file.

    Args:
        problem_file_path (str): The full path to the Python file
                                 containing the Solution class.
    """
    try:
        # Create a module spec from the problem file path.
        spec = importlib.util.spec_from_file_location("solution_module", problem_file_path)
        solution_module = importlib.util.module_from_spec(spec)
        
        # Load the module.
        spec.loader.exec_module(solution_module)

        # Check if the Solution class exists in the module.
        if hasattr(solution_module, 'Solution'):
            # Create an instance of the Solution class.
            solution = solution_module.Solution()
            
            # Read a single line of input from stdin.
            # The shell redirection from tasks.json handles this.
            input_values = sys.stdin.readline().split()
            
            if len(input_values) == 3:
                x = int(input_values[0])
                y = int(input_values[1])
                z = int(input_values[2])
                
                # Call the findClosest method from the dynamically loaded class.
                result = solution.findClosest(x, y, z)
                
                # Print the result to stdout, which is redirected to output.txt.
                print(result)
            else:
                print("Error: Expected exactly three integer inputs.", file=sys.stderr)
        else:
            print("Error: The file does not contain a 'Solution' class.", file=sys.stderr)

    except (IOError, ValueError) as e:
        print(f"An error occurred: {e}", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: The file '{problem_file_path}' was not found.", file=sys.stderr)

if __name__ == "__main__":
    # The runner script expects the problem file path as a command-line argument.
    if len(sys.argv) > 1:
        problem_file = sys.argv[1]
        # Construct the full path using the current working directory.
        full_path = sys.path[0] + '/' + problem_file
        run_solution(full_path)
    else:
        print("Usage: python runner.py <problem_file.py>", file=sys.stderr)
