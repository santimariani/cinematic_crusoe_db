from .base import Base
class Enemies(Base, table=True):
    __tablename__ = "enemies"
    name: str

    def __repr__(self):
        return f"<Enemy {self.name!r}>"