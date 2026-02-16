from fastapi import FastAPI
from src.scoring import score, risk_bucket
from src.decision import dispatch_decision
from src.schemas import DispatchRequest

app = FastAPI(title="Hospital Staff Dispatch API")

@app.post("/dispatch-decision")
def dispatch(request: DispatchRequest):
    input_data = request.dict()

    s = score(input_data)
    risk = risk_bucket(s)
    decision = dispatch_decision(risk)

    return {
        "hospital_context": {
            "department": request.department,
            "shift_type": request.shift_type,
        },
        "risk_score": round(s, 3),
        "risk_level": risk,
        **decision
    }
