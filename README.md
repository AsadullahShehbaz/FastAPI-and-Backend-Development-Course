<div align="center">

# ⚡ FastAPI Full Course: Zero to Production-Ready Backend

### 10 hours · 14 modules · From Python basics to JWT auth, async APIs, PostgreSQL & Redis

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

**📺 [Watch the full course on YouTube](https://www.youtube.com/watch?v=CG4WyImo72s)** · **Part 1 of the FastAPI Series**

</div>

---

## 📖 About This Course

This repository is the companion code for a **10-hour, project-driven FastAPI course**. You start with the fundamentals of APIs and type hints, and finish by building a **secure, database-backed, asynchronous REST API** with user registration, OAuth2 + JWT login, and Redis-powered logout.

Every module builds on the previous one, so by the end you won't just know FastAPI's features. You'll understand **how they fit together in a real backend**.

> 🎯 **Who is this for?**
> Python developers, aspiring backend engineers, and AI engineers who want to build APIs for real-world applications.

---

## 🗺️ The Learning Roadmap

```mermaid
flowchart LR
    A["🌐 Foundations<br/>Modules 1-2"] --> B["🧩 Core API Skills<br/>Modules 3-5"]
    B --> C["✅ Data Validation<br/>Module 6"]
    C --> D["🗄️ Databases<br/>Modules 7-8"]
    D --> E["⚡ Async & Cloud DB<br/>Modules 9-10"]
    E --> F["🏗️ Architecture<br/>Module 10.1"]
    F --> G["🔐 Security<br/>Modules 11-11.2"]

    style A fill:#e3f2fd,stroke:#1976d2,color:#000
    style B fill:#e8f5e9,stroke:#388e3c,color:#000
    style C fill:#fff8e1,stroke:#f9a825,color:#000
    style D fill:#fce4ec,stroke:#c2185b,color:#000
    style E fill:#f3e5f5,stroke:#7b1fa2,color:#000
    style F fill:#e0f7fa,stroke:#00838f,color:#000
    style G fill:#ffebee,stroke:#c62828,color:#000
```

| Stage | What You'll Master | Modules |
|:--|:--|:--:|
| 🌐 **1. Foundations** | What APIs are, why FastAPI, and a clean dev environment | 1 – 2 |
| 🧩 **2. Core API Skills** | Type hints, path & query parameters, your first full CRUD API | 3 – 5 |
| ✅ **3. Data Validation** | Pydantic models, schemas, and bulletproof request/response validation | 6 |
| 🗄️ **4. Databases** | SQL fundamentals, SQLAlchemy, SQLModel, and database integration | 7 – 8 |
| ⚡ **5. Async & Cloud DB** | Async IO, asynchronous APIs, PostgreSQL on Supabase | 9 – 10 |
| 🏗️ **6. Architecture** | Structuring a growing codebase with API Routers | 10.1 |
| 🔐 **7. Security** | Registration, OAuth2 password flow, JWT login, Redis-based logout | 11 – 11.2 |

---

## 📚 Course Curriculum

| # | Module | Timestamp | Approx. Length | Level |
|:-:|:--|:--:|:--:|:--:|
| 1 | **Introduction to APIs and FastAPI** | [`00:04:19`](https://www.youtube.com/watch?v=CG4WyImo72s&t=259s) | ~14 min | 🟢 Beginner |
| 2 | **Environment Setup** | [`00:18:22`](https://www.youtube.com/watch?v=CG4WyImo72s&t=1102s) | ~8 min | 🟢 Beginner |
| 3 | **Type Hints & Path Parameters** | [`00:26:23`](https://www.youtube.com/watch?v=CG4WyImo72s&t=1583s) | ~53 min | 🟢 Beginner |
| 4 | **Query Parameters** | [`01:19:31`](https://www.youtube.com/watch?v=CG4WyImo72s&t=4771s) | ~26 min | 🟢 Beginner |
| 5 | **Build a CRUD API** | [`01:45:05`](https://www.youtube.com/watch?v=CG4WyImo72s&t=6305s) | ~13 min | 🟡 Intermediate |
| 6 | **Pydantic for Data Validation** | [`01:57:44`](https://www.youtube.com/watch?v=CG4WyImo72s&t=7064s) | ~1 hr 48 min | 🟡 Intermediate |
| 7 | **SQL Database** | [`03:46:08`](https://www.youtube.com/watch?v=CG4WyImo72s&t=13568s) | ~1 hr 3 min | 🟡 Intermediate |
| 8 | **SQLAlchemy, SQLModel & Database Integration** | [`04:49:10`](https://www.youtube.com/watch?v=CG4WyImo72s&t=17350s) | ~1 hr 10 min | 🟡 Intermediate |
| 9 | **Async IO and Asynchronous APIs** | [`05:58:58`](https://www.youtube.com/watch?v=CG4WyImo72s&t=21538s) | ~33 min | 🔴 Advanced |
| 10 | **PostgreSQL (Supabase) + FastAPI** | [`06:31:32`](https://www.youtube.com/watch?v=CG4WyImo72s&t=23492s) | ~34 min | 🔴 Advanced |
| 10.1 | **API Routers** | [`07:05:44`](https://www.youtube.com/watch?v=CG4WyImo72s&t=25544s) | ~43 min | 🔴 Advanced |
| 11 | **Authentication: Register** | [`07:48:48`](https://www.youtube.com/watch?v=CG4WyImo72s&t=28128s) | ~47 min | 🔴 Advanced |
| 11.1 | **OAuth2 Password Flow & JWT Tokens: Login** | [`08:35:57`](https://www.youtube.com/watch?v=CG4WyImo72s&t=30957s) | ~1 hr 19 min | 🔴 Advanced |
| 11.2 | **Logout (Redis Database)** | [`09:55:10`](https://www.youtube.com/watch?v=CG4WyImo72s&t=35710s) | ~5 min+ | 🔴 Advanced |

---

## 🧭 Module-by-Module Guide

<details>
<summary><b>🌐 Stage 1: Foundations (Modules 1-2)</b></summary>

### Module 1: Introduction to APIs and FastAPI
- What an API is and how clients and servers communicate
- REST concepts: HTTP methods, status codes, JSON
- Why FastAPI: speed, automatic docs, type-driven design

### Module 2: Environment Setup
- Python environment and dependency management
- Installing FastAPI and an ASGI server
- Running your first app and exploring the auto-generated docs

**✅ Outcome:** A working FastAPI project running locally.
</details>

<details>
<summary><b>🧩 Stage 2: Core API Skills (Modules 3-5)</b></summary>

### Module 3: Type Hints & Path Parameters
- Python type hints and why FastAPI relies on them
- Defining and validating path parameters
- Automatic documentation driven by your types

### Module 4: Query Parameters
- Optional and required query parameters
- Defaults, filtering, searching, and pagination patterns
- Validating query input

### Module 5: Build a CRUD API
- Create, Read, Update, Delete endpoints
- Applying HTTP methods and status codes correctly
- Your first end-to-end working API

**✅ Outcome:** A complete CRUD API you can test from the interactive docs.
</details>

<details>
<summary><b>✅ Stage 3: Data Validation (Module 6)</b></summary>

### Module 6: Pydantic for Data Validation
- Defining request and response models
- Field constraints, validators, and nested models
- Separating input schemas from output schemas
- Returning clean, predictable, well-documented responses

**✅ Outcome:** An API that rejects bad data automatically and documents itself.
</details>

<details>
<summary><b>🗄️ Stage 4: Databases (Modules 7-8)</b></summary>

### Module 7: SQL Database
- Relational database fundamentals
- Writing SQL queries
- Tables, relationships, and data modelling

### Module 8: SQLAlchemy, SQLModel & Database Integration
- Using an ORM instead of raw SQL
- SQLAlchemy and SQLModel models
- Sessions and dependency injection
- Connecting your CRUD API to a real database

**✅ Outcome:** A persistent API backed by a real database.
</details>

<details>
<summary><b>⚡ Stage 5: Async & Cloud Database (Modules 9-10)</b></summary>

### Module 9: Async IO and Asynchronous APIs
- Synchronous vs asynchronous execution
- `async` / `await` in Python
- Writing non-blocking endpoints and database calls

### Module 10: PostgreSQL (Supabase) + FastAPI
- Provisioning a managed PostgreSQL database with Supabase
- Connecting FastAPI to a cloud database
- Moving from local development toward production-style infrastructure

**✅ Outcome:** An async API connected to a hosted PostgreSQL database.
</details>

<details>
<summary><b>🏗️ Stage 6: Architecture (Module 10.1)</b></summary>

### Module 10.1: API Routers
- Splitting a growing app into modular routers
- Organizing endpoints, schemas, and models
- Building a maintainable project structure

**✅ Outcome:** A clean, scalable codebase ready for authentication.
</details>

<details>
<summary><b>🔐 Stage 7: Security (Modules 11-11.2)</b></summary>

### Module 11: Authentication, Register
- User registration flow
- Password hashing and secure credential storage

### Module 11.1: OAuth2 Password Flow & JWT Tokens, Login
- OAuth2 password flow in FastAPI
- Creating and verifying JWT access tokens
- Protecting routes with dependencies

### Module 11.2: Logout (Redis Database)
- Why stateless JWTs need a logout strategy
- Using Redis to manage token invalidation

**✅ Outcome:** A complete authentication system: register, login, protected routes, and logout.
</details>

---

## 🛠️ Tech Stack

| Layer | Technology |
|:--|:--|
| **Framework** | FastAPI |
| **Language** | Python 3 |
| **Validation** | Pydantic |
| **ORM** | SQLAlchemy, SQLModel |
| **Database** | PostgreSQL (hosted on Supabase) |
| **Concurrency** | Async IO (`async` / `await`) |
| **Auth** | OAuth2 Password Flow, JWT |
| **Cache / Token Store** | Redis |

---

## 💼 Skills Demonstrated

*A quick view for recruiters and hiring managers.*

- ✅ Designing and building **RESTful APIs** with FastAPI
- ✅ **Data validation and serialization** with Pydantic
- ✅ **Relational database design** and SQL
- ✅ **ORM-based persistence** with SQLAlchemy and SQLModel
- ✅ **Asynchronous programming** for high-throughput services
- ✅ Working with **managed PostgreSQL** (Supabase)
- ✅ **Modular architecture** using API Routers
- ✅ **Secure authentication**: password hashing, OAuth2, JWT
- ✅ **Token invalidation** using Redis
- ✅ Using **auto-generated OpenAPI documentation** for testing and collaboration

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Basic Python knowledge (functions, classes, dictionaries)
- A code editor such as VS Code
- Optional: a free [Supabase](https://supabase.com) account (Module 10 onward) and Redis (Module 11.2)

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/AsadullahShehbaz/FastAPI-and-Backend-Development-Course.git
cd FastAPI-and-Backend-Development-Course

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
uvicorn main:app --reload
```

Then open:
- **Interactive docs (Swagger UI):** http://127.0.0.1:8000/docs
- **Alternative docs (ReDoc):** http://127.0.0.1:8000/redoc

---

## 🎓 How to Get the Most From This Course

1. **Follow the modules in order.** Each one depends on the last.
2. **Code along.** Pause the video and type it yourself.
3. **Break things on purpose.** Send invalid data and read the errors.
4. **Use `/docs` constantly.** It's your testing playground.
5. **Finish each module's outcome** before moving to the next stage.

---

## 🔭 What's Next

This is **Part 1** of the series. Coming soon:

- **Part 2:** Intermediate FastAPI concepts
- **Part 3:** Advanced FastAPI concepts

⭐ **Star this repo** to get notified when new parts land.

---

## 👨‍💻 About the Instructor

**Asadullah Shehbaz**
AI Engineer & Educator · Former Kaggle Grandmaster (#26 Peak Global Rank)

Subscribe to **Asadullah AI** for practical AI engineering, backend development, and MLOps.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/asadullahai)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AsadullahShehbaz)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://kaggle.com/ahmed920)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/asadullahgenai)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/asad_ullahshehbaz/)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/profile.php?id=61576230402114)

---

<div align="center">

**If this course helped you, give the repo a ⭐ and share it with a friend who is learning backend development.**

`#FastAPI` `#Python` `#BackendDevelopment`

</div>