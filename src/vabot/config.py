import os
from pathlib import Path
from os.path import join
from dotenv import load_dotenv

load_dotenv(join(Path(__file__).resolve().parent.parent, ".env"))

class BaseConfig(object):
    API_KEY= os.environ.get("API_KEY")
    BASE_DIR = Path(__file__).resolve().parent.parent


