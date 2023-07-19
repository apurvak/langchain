from pydantic import BaseModel, Field
from pydantic.fields import List


class Result(BaseModel):
    sql: str = Field()
    x_axis: List[str]
    y_axis: List[str]
    time_grain: str
    chart_type: str
    title: str

