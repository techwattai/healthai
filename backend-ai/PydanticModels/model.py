from pydantic import BaseModel
from typing import List


class UserSymptoms(BaseModel):
    symptoms: List[str]
    user_description: str

class PossibleCauses(BaseModel):
    urgency_level: str
    possible_conditions: List[str]
    recommended_department: str
    summary: str
    confidence_score: float
