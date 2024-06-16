from .base import Base
class Forts(Base, table=True):
    __tablename__ = "forts"
    name: str

    def __repr__(self):
        return f"<Fort {self.name!r}>"