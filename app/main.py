from db import engine
from models import metadata

metadata.create_all(engine)

