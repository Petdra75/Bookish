from sqlalchemy import Column, Integer, String

from app.helpers.database import Base

class Example(Base):
    # This sets the name of the table in the database
    __tablename__ = "Test"

    # Here we outline what columns we want in our database
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    example_field_1 = Column(String)
    example_field_2 = Column(Integer)

    def __init__(self, example_field_1, example_field_2):
        self.example_field_1 = example_field_1
        self.example_field_2 = example_field_2

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "example_field_1": self.example_field_1,
            "example_field_2": self.example_field_2
        }