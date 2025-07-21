# models.py
from sqlalchemy import Column, Integer, String, JSON, DateTime, Date
from .database import Base  

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheets"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True)
    inspection_by = Column(String)
    inspection_date = Column(Date)
    bogie_details = Column(JSON)
    bogie_checksheet = Column(JSON)
    bmbc_checksheet = Column(JSON)
    status = Column(String, default="Saved")

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True)
    submitted_by = Column(String)
    submitted_date = Column(Date)
    fields = Column(JSON)
    status = Column(String, default="Saved")