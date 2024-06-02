from sqlalchemy import Column, Integer, String, Text
from database import Base

class CodeSubmissionModel(Base):
    __tablename__ = "code_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
