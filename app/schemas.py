# Correct way:
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import date
from typing import Optional, List, Dict

# Wheel Specification Schemas
class WheelSpecificationCreate(BaseModel):
    form_number: str
    submitted_by: str
    submitted_date: date
    fields: Dict[str, str]

class WheelSpecification(WheelSpecificationCreate):
    status: str
    
    class Config:
        from_attributes = True  # Updated for Pydantic V2

# Bogie Checksheet Schemas
class BogieDetails(BaseModel):
    bogie_no: str
    maker_year_built: str
    incoming_div_and_date: str
    deficit_components: str
    date_of_ioh: str

class BogieChecksheetData(BaseModel):
    bogie_frame_condition: str
    bolster: str
    bolster_suspension_bracket: str
    lower_spring_seat: str
    axle_guide: str

class BmbcChecksheetData(BaseModel):
    cylinder_body: str
    piston_trunnion: str
    adjusting_tube: str
    plunger_spring: str

class BogieChecksheetCreate(BaseModel):
    form_number: str
    inspection_by: str
    inspection_date: date
    bogie_details: BogieDetails
    bogie_checksheet: BogieChecksheetData
    bmbc_checksheet: BmbcChecksheetData

class BogieChecksheet(BogieChecksheetCreate):
    status: str
    
    class Config:
        from_attributes = True  # Updated for Pydantic V2