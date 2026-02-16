from src.decision import dispatch_decision

def test_high_risk_dispatch():
    result = dispatch_decision("HIGH")
    assert result["decision"] == "DISPATCH"
