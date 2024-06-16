from .base import Base

class Seasons(Base, table=True):
    __tablename__ = "seasons"
    name: str

    def __repr__(self):
        return f"<Season {self.name!r}>"