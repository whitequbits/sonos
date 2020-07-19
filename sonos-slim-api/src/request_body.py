from pydantic import BaseModel


class StockDetectionRequest(BaseModel):
    symbol: str
    future_day: int


    class Config:
        schema_extra = {
            "example": {
                "symbol": "AAPL",
                "future_day": 5,
            }
        }
