""" 
 Imports, and Project Structure:

bash; 

touch crystal_codex/__init__.py

It tells Python: “This folder is a package. You can now import from it.”



"""

# crystal_codex/__init__.py

from .gems import recommend_crystal
from .rituals import log_ritual
from .utils import get_timestamp

__version__ = "0.1.0"

