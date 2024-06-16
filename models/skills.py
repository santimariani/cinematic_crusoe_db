from .base import Base
class Skills(Base, table=True):
    __tablename__ = "skills"
    name: str

    def __repr__(self):
        return f"<Skill {self.name!r}>"
