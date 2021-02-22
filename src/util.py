from graphviz import Digraph
import os
from pathlib import Path

def get_db(f):
    path = Path(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(path.parent.parent, "db", f))

def get_map(f):
    path = Path(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(path.parent.parent, "map", f))

def get_images(f):
    path = Path(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(path.parent.parent, "images", f))

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False