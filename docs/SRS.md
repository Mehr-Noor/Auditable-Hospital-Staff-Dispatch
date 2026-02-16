# Software Requirements Specification (SRS)
## Auditable Hospital Staff Dispatch System

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements of an **Auditable Hospital Staff Dispatch System** designed for regulated healthcare environments such as Germany and the EU.

The system uses Machine Learning strictly for **risk scoring**, while all operational decisions are handled by explicit, auditable business rules.

---

### 1.2 Scope
The system:
- Predicts staff shortage risk per hospital shift
- Supports real-time and batch inference
- Produces audit-friendly outputs
- Does not automate final staffing decisions

---

### 1.3 Definitions

| Term | Description |
|----|------------|
| Scoring | ML-based probabilistic risk estimation |
| Decision Engine | Deterministic rule-based logic |
| Auditability | Ability to explain and justify decisions |
| MVP | Minimum Viable Product |

---

## 2. Overall Description

### 2.1 System Context
The system integrates with hospital operations systems and provides decision support to staffing coordinators.

### 2.2 User Classes
- Hospital Operations Manager
- Staffing Coordinator
- System Auditor
- ML Engineer

---

## 3. Functional Requirements

### FR-1: Data Input
The system shall accept structured JSON inputs representing hospital shift staffing context.

### FR-2: Feature Engineering
Feature transformations shall be deterministic, reproducible, and independent from model logic.

### FR-3: Risk Scoring
The system shall produce a probabilistic risk score between 0 and 1 using ensemble ML models.

### FR-4: Decision Logic
Decisions shall be derived from explicit and configurable rules, not ML predictions.

### FR-5: API Inference
The system shall expose a RESTful API documented via OpenAPI.

### FR-6: Audit Output
Each response shall include risk score, risk bucket, decision, reason code, and contextual metadata.

---

## 4. Non-Functional Requirements

### 4.1 Explainability
Interpretable models shall be included as baselines for audit purposes.

### 4.2 Reliability
Decision logic shall be unit-tested and deterministic.

### 4.3 Compliance
- No personal data is processed or stored
- Synthetic or anonymized data only
- GDPR-aware design principles

### 4.4 Performance
API latency shall be below 500 ms per request under normal load.

---

## 5. Assumptions and Constraints
- MVP uses synthetic data
- Categorical domain fields are not used for model training
- The system provides decision support only
