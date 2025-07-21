# api/wheel_specifications.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/wheel-specifications", response_model=schemas.WheelSpecification)
def create_wheel_specification(
    spec: schemas.WheelSpecificationCreate,
    db: Session = Depends(get_db)
):
    return crud.create_wheel_specification(db=db, spec=spec)

@router.get("/wheel-specifications", response_model=list[schemas.WheelSpecification])
def get_wheel_specifications(
    form_number: Optional[str] = None,
    submitted_by: Optional[str] = None,
    submitted_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    filters = schemas.WheelSpecificationFilter(
        form_number=form_number,
        submitted_by=submitted_by,
        submitted_date=submitted_date
    )
    return crud.get_wheel_specifications(db=db, filters=filters)