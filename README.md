# 🎬 Audience Analytics Platform

A scalable, production-oriented Audience Analytics Platform built with Python for large-scale movie audience analysis and feature engineering.

The platform is designed to process millions of user interactions using memory-efficient streaming pipelines instead of loading the entire dataset into memory.

---

# Project Status

**Current Version:** Development (v0.1.0)

Current Progress:

- ✅ Project Foundation
- ✅ Configuration Management
- ✅ Logging Framework
- ✅ Data Loaders
- ✅ Dataset Validation
- ✅ ETL Pipeline
- ✅ Streaming User Feature Engineering
- ✅ Feature Writer

Upcoming:

- ⏳ Movie Feature Engineering
- ⏳ TMDB Integration
- ⏳ IMDb Integration
- ⏳ Recommendation Engine
- ⏳ Audience Segmentation
- ⏳ FastAPI
- ⏳ Dashboard
- ⏳ Docker Deployment

---

# Project Objectives

The goal of this project is to build an end-to-end analytics platform capable of:

- Processing datasets containing tens of millions of records
- Engineering reusable analytical features
- Supporting recommendation systems
- Supporting audience segmentation
- Serving as a backend for analytics dashboards
- Demonstrating production-quality Data Engineering practices

---

# Dataset

## MovieLens 25M Dataset

Current dataset:

- 25 Million Ratings
- 162,000+ Users
- 62,000+ Movies

Future datasets:

- TMDB Metadata
- IMDb Metadata
- Synthetic Streaming Events

---

# Current Architecture

```
                 MovieLens Dataset
                        │
                        ▼
               Chunk Data Loader
                        │
                        ▼
             Streaming Feature Builder
                        │
                        ▼
              User Statistics Engine
                        │
                        ▼
                Feature Writer
                        │
                        ▼
         user_features.parquet / CSV
```

---

# Project Structure

```
Audience-Analytics-Platform/

│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── constants.py
│   │   └── logging.py
│   │
│   ├── data/
│   │   ├── loaders/
│   │   │   ├── base_loader.py
│   │   │   ├── chunk_loader.py
│   │   │   └── movielens_loader.py
│   │   │
│   │   ├── transformers/
│   │   └── validators/
│   │
│   └── features/
│       ├── models.py
│       ├── user_feature_builder.py
│       ├── feature_writer.py
│       ├── feature_aggregator.py
│       └── feature_reducer.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── features/
│   └── external/
│
├── logs/
│
├── scripts/
│
├── tests/
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

---

# Features Implemented

## Configuration Management

- Environment-based configuration
- `.env` support
- Centralized application settings

---

## Logging Framework

- Centralized logger
- File logging
- Console logging
- Timestamped logs
- Production-ready logging format

---

## Data Loading

Implemented:

- Base Data Loader
- MovieLens Loader
- Chunk Loader

Supports:

- CSV Loading
- Memory-efficient chunk processing
- Dataset validation

---

## Dataset Validation

Current validations include:

- Required columns
- Missing values
- Duplicate records
- Dataset integrity checks

---

## ETL Pipeline

Current ETL workflow:

```
Raw Dataset

↓

Validation

↓

Transformation

↓

Processed Dataset
```

---

## Streaming Feature Engineering

The project implements streaming feature engineering instead of loading the complete dataset into memory.

Pipeline:

```
ratings.csv

↓

Chunk Loader

↓

Chunk Aggregation

↓

Global User Statistics

↓

Feature Generation

↓

Parquet Output
```

---

# User Features Generated

Current engineered features:

- User ID
- Rating Count
- Average Rating
- Minimum Rating
- Maximum Rating
- Movies Watched
- Active Days
- First Rating Date
- Last Rating Date

---

# Output Files

Generated feature datasets:

```
data/features/

user_features.csv

user_features.parquet
```

---

# Technologies Used

Programming

- Python 3.12

Libraries

- Pandas
- PyArrow
- Pydantic
- python-dotenv

Development

- Git
- GitHub
- Virtual Environment

---

# Design Principles

The project follows several software engineering principles.

- Modular Architecture
- Single Responsibility Principle
- Streaming Data Processing
- Memory Efficient Algorithms
- Reusable Components
- Configuration Driven Design

---

# Current Pipeline

```
MovieLens Ratings

↓

Chunk Loader

↓

Vectorized Aggregation

↓

Streaming Statistics

↓

User Feature Builder

↓

Feature Writer

↓

Parquet Dataset
```

---

# Testing

Implemented unit tests for:

- Configuration
- Constants
- Logging
- Base Loader
- MovieLens Loader
- Chunk Loader
- Dataset Validation
- ETL Pipeline
- User Feature Builder
- Feature Writer

---

# Future Roadmap

## Phase 1 ✅

Project Foundation

- Configuration
- Logging
- Loaders
- ETL
- Streaming User Features

---

## Phase 2

Movie Feature Engineering

- Rating Statistics
- Popularity Metrics
- Genre Analytics

---

## Phase 3

Multi-source Integration

- TMDB
- IMDb

---

## Phase 4

Machine Learning

- Recommendation System
- Audience Segmentation

---

## Phase 5

Deployment

- FastAPI
- Dashboard
- Docker
- AWS

---

# License

This project is licensed under the MIT License.

---

# Author

**Thirunagari Navadeep**

GitHub:
https://github.com/ThirunagariNavadeep

LinkedIn:
(Add your LinkedIn profile)

---

⭐ This project is actively under development. New features and improvements are continuously being added.
