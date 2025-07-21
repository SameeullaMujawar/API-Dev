# KPA Form Data API

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Configure PostgreSQL connection in `database.py`
3. Run migrations: `alembic upgrade head`
4. Start server: `uvicorn app.main:app --reload`

## Implemented APIs

### 1. Bogie Checksheet API
- **POST /api/forms/bogie-checksheet**
  - Creates a new bogie checksheet record
  - Complex nested JSON structure
  - Returns created record with status

### 2. Wheel Specifications API
- **POST /api/forms/wheel-specifications**
  - Creates new wheel specification
  - Handles dynamic fields object
- **GET /api/forms/wheel-specifications**
  - Retrieves filtered wheel specifications
  - Supports query parameters for filtering

## Technologies
- Python 3.9+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic for data validation
