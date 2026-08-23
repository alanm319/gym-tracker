from pydantic import BaseModel

class MetricPoint(BaseModel):
    start_time: str
    value: float
    
class ExerciseMetrics(BaseModel):
    start_time: str
    heaviest: float
    session_volume: float
    best_volume: float
    estimated_1rm: float