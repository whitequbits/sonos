from pydantic import BaseModel


class StockDetectionResponse(BaseModel):
    result: dict

    class Config:
        schema_extra = {
            "example": {
                "result": {
                    "5-day result": {
                        "0": 0.7523493766784668,
                        "1": 0.7928676605224609,
                        "2": 0.815296471118927,
                        "3": 0.8331950902938843,
                        "4": 0.8791333436965942,
                        "5": 0.890447735786438
                    }
                }
            }
        }
