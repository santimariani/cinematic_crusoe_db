from .base import Base

class Characters(Base, table=True):
    __tablename__ = "characters"
    name: str

    def __repr__(self):
        return f"<Character {self.name!r}>"