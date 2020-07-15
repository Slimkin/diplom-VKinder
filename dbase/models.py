from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


def create_all(engine):
    Base.metadata.create_all(engine)


class VkinderDB(Base):
    __tablename__ = 'Vkinder database'

    user = Column(String(50), primary_key=True)
    search_data = Column(JSONB, default=list, nullable=False)

    def __str__(self):
        return f'< {self.user} | {self.search_data} >'
