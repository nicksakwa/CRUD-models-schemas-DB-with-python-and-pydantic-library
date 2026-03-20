from sqlalchemy import create_engine
from  .database import Base
class ItemModel(Base):
    __tablename__ =="items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)