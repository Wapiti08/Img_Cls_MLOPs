import datetime

from pydantic import BaseModel, Field

from ms import app
from ms.functions import get_model_response

model_name = 'Breast Cancer'
version = 'v1.0.0'

# data validation for Input
class Input(BaseModel):
    concavity_mean: float = Field(..., gt=0)

# data validation for output