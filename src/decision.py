def dispatch_decision(risk_level: str) -> dict:
    if risk_level == "LOW":
        return {"decision": "NO_ACTION", "reason": "LOW_RISK"}
    if risk_level == "MEDIUM":
        return {"decision": "STANDBY", "reason": "MEDIUM_RISK"}
    return {"decision": "DISPATCH", "reason": "CRITICAL_SHORTAGE"}
