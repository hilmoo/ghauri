import sys
import builtins
from ghauri.scripts.ghauri import main

builtins.exit = sys.exit

if __name__ == "__main__":
    main()