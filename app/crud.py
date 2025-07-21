# crud.py
from sqlalchemy.orm import Session
from . import models, schemas

# Bogie Checksheet CRUD
def create_bogie_checksheet(db: Session, checksheet: schemas.BogieChecksheetCreate):
    db_checksheet = models.BogieChecksheet(
        form_number=checksheet.form_number,
        inspection_by=checksheet.inspection_by,
        inspection_date=checksheet.inspection_date,
        bogie_details=checksheet.bogie_details.dict(),
        bogie_checksheet=checksheet.bogie_checksheet.dict(),
        bmbc_checksheet=checksheet.bmbc_checksheet.dict()
    )
    db.add(db_checksheet)
    db.commit()
    db.refresh(db_checksheet)
    return db_checksheet

# Wheel Specification CRUD
def create_wheel_specification(db: Session, spec: schemas.WheelSpecificationCreate):
    db_spec = models.WheelSpecification(
        form_number=spec.form_number,
        submitted_by=spec.submitted_by,
        submitted_date=spec.submitted_date,
        fields=spec.fields
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_wheel_specifications(db: Session, filters: schemas.WheelSpecificationCreate):
    query = db.query(models.WheelSpecification)
    
    if filters.form_number:
        query = query.filter(models.WheelSpecification.form_number == filters.form_number)
    if filters.submitted_by:
        query = query.filter(models.WheelSpecification.submitted_by == filters.submitted_by)
    if filters.submitted_date:
        query = query.filter(models.WheelSpecification.submitted_date == filters.submitted_date)
    
    return query.all()