import datetime

from pydantic import BaseModel, Field

from ms import app
from ms.functions import get_model_response

model_name = 'Breast Cancer'
version = 'v1.0.0'

# data validation for Input
class Input(BaseModel):
    concavity_mean: float
    concave_points_mean: float
    perimeter_se: float
    area_se: float
    texture_worst: float
    area_worst: float

    class Config:
        schema_extra = {
             "concavity_mean": 0.3001,
            "concave_points_mean": 0.1471,
            "perimeter_se": 8.589,
            "area_se": 153.4,
            "texture_worst": 17.33,
            "area_worst": 2019.0,
        }


# data validation for output
class Output(BaseModel):
    label: str
    prediction: int

@app.route('/info', method=['GET'])
async def model_info():
    model_info = {}
    model_info['version'] = version
    model_info['model_name'] = model_name

    return model_info


@app.route('/health', method=['GET'])
async def service_health():
    '''
    
    ''' 
    return 'ok'

@app.route('/predict', method=['POST'])
async def predict(input):
    response = get_model_response(input)

    return response
