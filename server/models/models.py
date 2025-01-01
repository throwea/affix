from pydantic import BaseModel

class DataSubmit(BaseModel):
    tabular_data: str | None
