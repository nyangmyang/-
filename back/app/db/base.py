import sys, os
base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(base_dir + "/..")
from sqlalchemy.orm import declarative_base

Base = declarative_base() 