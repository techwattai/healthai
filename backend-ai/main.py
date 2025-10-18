from Endpoints import body_vitals, ai_appointments
from fastapi import FastAPI


# ----------------------------
# FastAPI App
# ----------------------------
app = FastAPI(
    title="Hospital Vitals Live ML API",
    description="API to stream live patient vitals and get ML-based health predictions.",
    version="1.0.0"
    
    )



app.include_router(body_vitals.router)
app.include_router(ai_appointments.router)