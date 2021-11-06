# Python imports
from typing import Optional

# Pydantic Imports
from pydantic import BaseModel, Field



#Player Model
class Player(BaseModel):
    """This is the model for creating new players"""
    first_name: str = Field(...,min_length=2, max_lenght=50, example="John")
    last_name: str = Field(...,min_length=2, max_lenght=50, example="Doe" )
    h_in: Optional[int] = Field(gt=21, lt=90, example=50 )
    h_meters: float = Field(gt=0.53, lt=2.28, example=1.70)