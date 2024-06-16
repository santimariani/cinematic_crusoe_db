from .base import Base
class Pets(Base, table=True):
    __tablename__ = "pets"
    name: str

    def __repr__(self):
        return f"<Pet {self.name!r}>"
