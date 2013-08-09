import sys
import importlib
"""
To do: Need to add script to calculate our food and reputation after each hunt. 

"""
def run_tests(script_name):
    user_module = importlib.import_module(script_name[:-3])
    user_module= user_module.Player()
    test_all_no_rep(user_module)
    test_reps(user_module)

def test_all_no_rep(module):
     decisions = module.hunt_choices(1, 0, 0, 5, [0,0,0,0,0,0,0,0,0,0,0,0])
     print decisions

def test_reps(module):
     decisions = module.hunt_choices(1, 0, 0, 5, [100,50,50,50,60,40,100,100,100,0,70,90])
     print decisions

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print ("\nYou must include the filename that contains your code "
               "as the only argument to this script.\n\n"
               "Example: python tester.py filename_of_your_script.py\n")
        raise
    else:
        run_tests(filename)