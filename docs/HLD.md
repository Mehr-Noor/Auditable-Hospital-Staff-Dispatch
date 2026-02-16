# High Level Design (HLD)
## Auditable Hospital Staff Dispatch System

---

## 1. Architecture Overview

Client / Hospital System
|
v
FastAPI Gateway (Validation)
|
v
Feature Engineering Layer
|
v
ML Scoring Layer (Ensemble)
|
v
Risk Bucketing
|
v
Decision Engine (Rules)
|
v
Audit-Friendly Response


---

## 2. Design Principles

- Separation of scoring and decision logic
- Explainability-first modeling
- Deterministic feature processing
- Auditability and compliance by design

---

## 3. Component Responsibilities

### API Layer
- Input validation
- Orchestration
- Response formatting

### Feature Layer
- Feature computation
- Schema stability

### Scoring Layer
- Model inference
- Ensemble aggregation

### Decision Layer
- Rule-based decisions
- Deterministic outputs

---

## 4. Deployment Architecture

Client
|
Load Balancer
|
Dockerized FastAPI Service
|
ML Model Artifacts
|
Audit Logs


---

## 5. Security and Compliance Considerations

- No PII processing
- Stateless API design
- Containerized deployment
