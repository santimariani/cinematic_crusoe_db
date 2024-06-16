from .base import Base

class Locations(Base, table=True):
    __tablename__ = "locations"
    name: str

    def __repr__(self):
        return f"<Location {self.name!r}>"