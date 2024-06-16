from .base import Base
class Items(Base, table=True):
    __tablename__ = "items"
    name: str

    def __repr__(self):
        return f"<Item {self.name!r}>"
