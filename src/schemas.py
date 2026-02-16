from pydantic import BaseModel

class DispatchRequest(BaseModel):
    department: str
    shift_type: str
    required_staff: int
    available_staff: int
    avg_patient_load: int
    historical_shortage_rate: float
    region_staff_pool: int
