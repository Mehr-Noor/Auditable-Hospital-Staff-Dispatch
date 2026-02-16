# Low Level Design (LLD)
## Auditable Hospital Staff Dispatch System

---

## 1. Module Overview

### data_generation.py
- Generates GDPR-safe synthetic hospital staffing data

---

### features.py
**Responsibilities**
- Deterministic feature engineering
- Ignores non-feature domain fields

**Input**
- Raw JSON / DataFrame

**Output**
- Numerical feature vector

---

### train.py
**Responsibilities**
- Train ML models
- Evaluate performance
- Persist model artifacts

Models:
- Logistic Regression
- XGBoost

---

### scoring.py
**Responsibilities**
- Load trained models
- Produce ensemble risk score
- No business logic

---

### decision.py
**Responsibilities**
- Rule-based decision mapping
- Deterministic and testable

---

### api.py
**Responsibilities**
- Input schema validation
- Inference orchestration
- Audit-friendly response generation

---

### batch.py
**Responsibilities**
- Offline batch inference
- CSV input/output

---

## 2. Data Flow

Request
→ Validation
→ Feature Engineering
→ ML Scoring
→ Risk Bucket
→ Decision Rules
→ Response


---

## 3. Error Handling

- Invalid input → HTTP 422
- Missing model → Fail fast
- Decision always resolvable

---

## 4. Testing Strategy

- Unit tests for decision logic
- Deterministic feature tests
