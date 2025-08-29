from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated

class UserInput(BaseModel):

    age:Annotated[int,Field(...,description="write the age", gt=0,lt=150)]
    sex:Annotated[Literal["male",'female'],Field(description = "gender of patient")]
    children:Annotated[int,Field(...,description="no of childs",lt=30)]
    smoker:Annotated[Literal["yes","no"],Field(...,description="smoking habit",max_length=3)]
    region: Annotated[Literal["northeast","northwest","southeast","southwest"],Field(...,description="pls satate the region",max_length=10)]
    bmi:Annotated[float,Field(...,description="pls mention your bmi",lt=50,gt=5)]

@computed_field
@property
def risk_factor(self) -> str:
    if self.bmi > 35.0 and self.smoker == "yes":
        return "high"
    elif self.smoker == "yes" and self.bmi < 35.0:
        return "medium"
    elif self.smoker == "no" and self.bmi < 35.0:
        return "low"