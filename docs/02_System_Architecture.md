# System Architecture

# 1. Overview

The AI Audience Analytics Platform follows a layered architecture that separates responsibilities into independent modules.

This design improves:

- Scalability
- Maintainability
- Testability
- Reusability

The application consists of four major layers:

1. Data Layer
2. Machine Learning Layer
3. API Layer
4. Presentation Layer

---

# 2. High-Level Architecture

                   External Data Sources
        ┌─────────────────────────────────────┐
        │ MovieLens │ TMDB │ IMDb │ Synthetic │
        └─────────────────┬───────────────────┘
                          │
                          ▼
                  Data Ingestion Layer
                          │
                          ▼
                  Data Validation Layer
                          │
                          ▼
                    ETL Pipeline
                          │
                          ▼
                  PostgreSQL Database
                          │
      ┌───────────────────┼────────────────────┐
      ▼                   ▼                    ▼
Recommendation     Audience Analytics    Churn Prediction
      │                   │                    │
      └──────────────┬────┴────────────────────┘
                     ▼
                MLflow Tracking
                     │
                     ▼
               FastAPI Backend
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
    Streamlit Admin         Power BI Dashboard
                     │
                     ▼
                 Docker + AWS

---

# 3. Layers

## Layer 1 – Data Layer

Responsibilities

- Read datasets
- Download API data
- Validate data
- Clean data
- Store data

Components

- Data Loader
- Validators
- ETL Pipeline
- PostgreSQL

---

## Layer 2 – Machine Learning Layer

Responsibilities

- Feature Engineering
- Model Training
- Model Evaluation
- Experiment Tracking

Models

- Recommendation System
- Churn Prediction
- Audience Segmentation

---

## Layer 3 – API Layer

Responsibilities

- Accept requests
- Load trained models
- Generate predictions
- Return JSON responses

Technology

- FastAPI

---

## Layer 4 – Presentation Layer

Responsibilities

- Business Dashboard
- Reports
- Interactive Charts

Technologies

- Power BI
- Streamlit

---

# 4. Data Flow

Raw Data

↓

Validation

↓

Cleaning

↓

Database

↓

Feature Engineering

↓

Machine Learning

↓

REST API

↓

Dashboard

---

# 5. Scalability

The architecture allows:

- Independent model retraining
- Database replacement
- Cloud deployment
- Horizontal scaling
- API versioning

---

# 6. Advantages

- Modular
- Easy to maintain
- Easy to test
- Production ready
- Cloud ready