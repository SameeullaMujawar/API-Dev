# api/bogie_checksheet.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/bogie-checksheet", response_model=schemas.BogieChecksheet)
def create_bogie_checksheet(
    checksheet: schemas.BogieChecksheetCreate,
    db: Session = Depends(get_db)
):
    return crud.create_bogie_checksheet(db=db, checksheet=checksheet)