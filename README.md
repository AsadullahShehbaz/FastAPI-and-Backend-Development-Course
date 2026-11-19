<div align="center">

# ⚡ FastAPI Full Course: Zero to Production-Ready Backend

### Part 1: Foundations, Auth & Async · Part 2: Relations, Migrations, Email & Real-World Features · Part 3: Celery, Testing, React, Docker & AWS

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-6BA81E?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logoColor=white)

<br>

| 🎬 Part 1 | 🎬 Part 2 | 🎬 Part 3 (Final) |
|:-:|:-:|:-:|
| [![FastAPI Full Course Part 1](https://img.youtube.com/vi/CG4WyImo72s/maxresdefault.jpg)](https://www.youtube.com/watch?v=CG4WyImo72s) | [![FastAPI Full Course Part 2](https://img.youtube.com/vi/hj81HI2AsG4/maxresdefault.jpg)](https://www.youtube.com/watch?v=hj81HI2AsG4) | [![FastAPI Full Course Part 3](https://img.youtube.com/vi/G3UEDZEVw5g/maxresdefault.jpg)](https://www.youtube.com/watch?v=G3UEDZEVw5g) |
| **[Watch Part 1](https://www.youtube.com/watch?v=CG4WyImo72s)** | **[Watch Part 2](https://www.youtube.com/watch?v=hj81HI2AsG4)** | **[Watch Part 3](https://www.youtube.com/watch?v=G3UEDZEVw5g)** |

<sub>👆 Click a thumbnail to watch the full course on YouTube</sub>

</div>

---

## 📖 About This Course

This repository is the companion code for the **FastAPI Full Course series**, a project-driven path from API basics to a deployed, production-ready backend. **The series is now complete: all three parts are live.**

| Part | What you build | Length | Modules | Code folders |
|:-:|:--|:-:|:-:|:-:|
| **Part 1** | A secure, database-backed, asynchronous REST API with registration, OAuth2 + JWT login, and Redis-powered logout | ~10 hrs | 14 | `m01` – `n11` |
| **Part 2** | Real-world backend features: SQL relationships, Alembic migrations, delivery partners, product events, email sending, email verification, password reset, Jinja templates, and reviews | 9+ hrs | 10 | `n12` – `n20` |
| **Part 3** | Production readiness: Celery background tasks, many-to-many relationships, error handling, middleware & CORS, API documentation, Pytest and API testing, a React frontend, Login with Google, WebSockets, Docker, and AWS deployment | ~7 hrs | 12 | `n21` – `n30` |

Every module builds on the previous one, so you won't just learn FastAPI's features. You'll understand **how they fit together in a real backend**.

📘 **Prefer reading?** Every topic and module tutorial is also available as written notes on the course website: **[asadullah-ai.vercel.app](https://asadullah-ai.vercel.app/)**

> 🎯 **Who is this for?**
> Python developers, aspiring backend engineers, and AI engineers who want to build APIs for real-world applications.
> **Part 2 assumes you know the Part 1 material** (FastAPI basics, SQLModel, async, and JWT auth), and **Part 3 continues the same project** from Parts 1 and 2. If you are new to FastAPI, start with Part 1.
> Part 3 is not for complete beginners to Python.

---

## 🗺️ The Learning Roadmap

| Part | Stage | What You'll Master | Modules |
|:-:|:--|:--|:--:|
| 1 | 🌐 **Foundations** | What APIs are, why FastAPI, and a clean dev environment | 1 – 2 |
| 1 | 🧩 **Core API Skills** | Type hints, path & query parameters, your first full CRUD API | 3 – 5 |
| 1 | ✅ **Data Validation** | Pydantic models, schemas, and bulletproof request/response validation | 6 |
| 1 | 🗄️ **Databases** | SQL fundamentals, SQLAlchemy, SQLModel, and database integration | 7 – 8 |
| 1 | ⚡ **Async & Cloud DB** | Async IO, asynchronous APIs, PostgreSQL on Supabase | 9 – 10 |
| 1 | 🏗️ **Architecture** | Structuring a growing codebase with API Routers | 10.1 |
| 1 | 🔐 **Security** | Registration, OAuth2 password flow, JWT login, Redis-based logout | 11 – 11.2 |
| 2 | 🔗 **Data Modelling** | One-to-many and many-to-many SQL relationships, safe schema changes with Alembic | 1 – 2 |
| 2 | 📦 **Core Features** | Delivery partners and product events built end to end | 3 – 4 |
| 2 | ✉️ **Email & Templates** | Sending email, Jinja HTML templates, custom response classes | 5 – 7 |
| 2 | 🔐 **Account Flows** | Email verification and password reset | 8 – 9 |
| 2 | ⭐ **Reviews** | A product review feature that ties the backend together | 10 |
| 3 | ⚙️ **Background Jobs** | Celery workers and Redis for tasks that shouldn't block a request | 1 |
| 3 | 🔗 **Advanced Modelling** | Many-to-many relationships with SQLModel | 2 |
| 3 | 🛡️ **Reliability & API Layer** | Error handling, middleware, CORS, and API documentation | 3 – 5 |
| 3 | 🧪 **Testing** | Pytest fundamentals and full API testing | 6 – 7 |
| 3 | 🖥️ **Frontend & Social Login** | A React frontend and Login with Google (OAuth) | 8 – 9 |
| 3 | 🚀 **Real-Time & Deployment** | WebSockets, Docker, and deploying FastAPI to AWS | 10 – 12 |

---

## 📚 Course Curriculum

### 🎬 Part 1: Foundations, Auth & Async

📺 **[Watch Part 1 on YouTube](https://www.youtube.com/watch?v=CG4WyImo72s)**

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

### 🎬 Part 2: Relations, Migrations, Email & Real-World Features

📺 **[Watch Part 2 on YouTube](https://www.youtube.com/watch?v=hj81HI2AsG4)**

| # | Module | Timestamp | Approx. Length | Level |
|:-:|:--|:--:|:--:|:--:|
| 0 | **Introduction & What We're Building** | [`00:00:00`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=0s) | ~3 min | 🟡 Intermediate |
| 1 | **SQL Relations** | [`00:02:40`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=160s) | ~34 min | 🟡 Intermediate |
| 2 | **Alembic: DB Migrations** | [`00:36:33`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=2193s) | ~26 min | 🟡 Intermediate |
| 3 | **Delivery Partner** | [`01:02:25`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=3745s) | ~2 hr 26 min | 🔴 Advanced |
| 4 | **Product Event** | [`03:28:15`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=12495s) | ~1 hr 21 min | 🔴 Advanced |
| 5 | **Send Mail** | [`04:48:54`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=17334s) | ~1 hr 10 min | 🔴 Advanced |
| 6 | **Jinja Template (HTML + FastAPI)** | [`05:58:29`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=21509s) | ~30 min | 🔴 Advanced |
| 7 | **Response Classes** | [`06:28:30`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=23310s) | ~25 min | 🔴 Advanced |
| 8 | **Email Verification** | [`06:53:31`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=24811s) | ~57 min | 🔴 Advanced |
| 9 | **Password Reset** | [`07:50:23`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=28223s) | ~38 min | 🔴 Advanced |
| 10 | **Product Review** | [`08:28:29`](https://www.youtube.com/watch?v=hj81HI2AsG4&t=30509s) | Final module | 🔴 Advanced |

### 🎬 Part 3 (Final): Celery, Testing, React, Docker & AWS

📺 **[Watch Part 3 on YouTube](https://www.youtube.com/watch?v=G3UEDZEVw5g)**

| # | Module | Timestamp | Approx. Length | Level |
|:-:|:--|:--:|:--:|:--:|
| 0 | **Intro** | [`00:00:00`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=0s) | ~3 min | 🟡 Intermediate |
| 1 | **Celery** | [`00:02:30`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=150s) | ~46 min | 🔴 Advanced |
| 2 | **Many to Many Relationship** | [`00:48:10`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=2890s) | ~35 min | 🔴 Advanced |
| 3 | **Error Handling** | [`01:23:34`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=5014s) | ~32 min | 🔴 Advanced |
| 4 | **Middleware & CORS** | [`01:55:57`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=6957s) | ~22 min | 🔴 Advanced |
| 5 | **API Documentation** | [`02:18:07`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=8287s) | ~19 min | 🟡 Intermediate |
| 6 | **Pytest** | [`02:37:36`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=9456s) | ~24 min | 🟡 Intermediate |
| 7 | **API Testing** | [`03:01:36`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=10896s) | ~1 hr 21 min | 🔴 Advanced |
| 8 | **Frontend: React** | [`04:22:19`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=15739s) | ~1 hr 9 min | 🔴 Advanced |
| 9 | **Login with Google** | [`05:31:09`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=19869s) | ~20 min | 🔴 Advanced |
| 10 | **WebSocket** | [`05:51:12`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=21072s) | ~18 min | 🔴 Advanced |
| 11 | **Docker** | [`06:09:34`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=22174s) | ~20 min | 🔴 Advanced |
| 12 | **AWS Deployment** | [`06:30:02`](https://www.youtube.com/watch?v=G3UEDZEVw5g&t=23402s) | Final module | 🔴 Advanced |

---

## 🧭 Module-by-Module Guide

## Part 1

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

## Part 2

<details>
<summary><b>🔗 Stage 8: Data Modelling (Modules 1-2)</b></summary>

### Module 1: SQL Relations
- Modelling one-to-many and many-to-many relationships in SQL
- Defining relationships between your SQLModel tables
- Querying related data

### Module 2: Alembic, DB Migrations
- Why `create_all` isn't enough once your app has real data
- Generating and applying migrations safely
- Evolving your schema without losing data

**✅ Outcome:** A relational schema you can change safely over time.
</details>

<details>
<summary><b>📦 Stage 9: Core Features (Modules 3-4)</b></summary>

### Module 3: Delivery Partner
- Building the delivery partner feature end to end
- Models, relationships, schemas, and routes working together
- Extending your existing auth system to a new type of user

### Module 4: Product Event
- Building the product event feature end to end
- Tracking changes to a product over time
- Applying the relationships and migrations from earlier modules

**✅ Outcome:** Multi-entity backend features built on a real relational schema.
</details>

<details>
<summary><b>✉️ Stage 10: Email & Templates (Modules 5-7)</b></summary>

### Module 5: Send Mail
- Sending emails from FastAPI
- Configuring a mail service and keeping credentials out of your code

### Module 6: Jinja Template (HTML + FastAPI)
- Rendering HTML pages with Jinja templates
- Passing data from your endpoints into templates

### Module 7: Response Classes
- Returning custom responses beyond plain JSON
- Choosing the right response class for the job

**✅ Outcome:** An API that can send email and serve HTML as well as JSON.
</details>

<details>
<summary><b>🔐 Stage 11: Account Flows (Modules 8-9)</b></summary>

### Module 8: Email Verification
- Confirming a user's email address after registration
- Generating and validating verification links

### Module 9: Password Reset
- A complete forgot-password and reset flow
- Sending reset links and handling the reset page

**✅ Outcome:** Production-style account flows on top of your JWT authentication.
</details>

<details>
<summary><b>⭐ Stage 12: Reviews (Module 10)</b></summary>

### Module 10: Product Review
- Building a product review feature
- Bringing together relationships, auth, and validation in one feature

**✅ Outcome:** A feature-complete, real-world backend.
</details>

## Part 3

<details>
<summary><b>⚙️ Stage 13: Background Jobs (Module 1)</b></summary>

### Module 1: Celery
- Why slow work (email, notifications) shouldn't run inside a request
- Setting up Celery workers with Redis as the broker
- Writing and triggering background tasks from FastAPI endpoints

**✅ Outcome:** An API that offloads slow work to background workers.
</details>

<details>
<summary><b>🔗 Stage 14: Advanced Modelling (Module 2)</b></summary>

### Module 2: Many to Many Relationship
- Modelling many-to-many relationships with SQLModel link tables
- Reading and writing related records on both sides
- Applying schema changes with the migrations workflow from Part 2

**✅ Outcome:** A relational schema that supports real many-to-many data.
</details>

<details>
<summary><b>🛡️ Stage 15: Reliability & API Layer (Modules 3-5)</b></summary>

### Module 3: Error Handling
- Raising and handling errors consistently across the API
- Custom exceptions and clean, predictable error responses

### Module 4: Middleware & CORS
- Writing middleware that runs on every request
- Configuring CORS so a browser frontend can call your API safely

### Module 5: API Documentation
- Improving the auto-generated OpenAPI docs
- Making endpoints easier to understand, test, and share

**✅ Outcome:** A robust, well-documented API that a frontend can consume.
</details>

<details>
<summary><b>🧪 Stage 16: Testing (Modules 6-7)</b></summary>

### Module 6: Pytest
- Pytest fundamentals: tests, assertions, and fixtures
- Structuring a test suite for a FastAPI project

### Module 7: API Testing
- Testing endpoints end to end
- Overriding dependencies and using a test database
- Testing authenticated routes

**✅ Outcome:** An automated test suite you can run before every release.
</details>

<details>
<summary><b>🖥️ Stage 17: Frontend & Social Login (Modules 8-9)</b></summary>

### Module 8: Frontend: React
- Building a React frontend for the backend
- Calling your API from the browser

### Module 9: Login with Google
- Adding Google sign-in (OAuth) to the app
- Connecting social login to your existing authentication

**✅ Outcome:** A full-stack app with a working frontend and Google login.
</details>

<details>
<summary><b>🚀 Stage 18: Real-Time & Deployment (Modules 10-12)</b></summary>

### Module 10: WebSocket
- Real-time, two-way communication with WebSockets
- Pushing live updates from the backend to clients

### Module 11: Docker
- Containerizing the FastAPI app
- Running the full stack (API, Redis, Celery worker) with containers

### Module 12: AWS Deployment
- Deploying the containerized FastAPI backend to AWS
- Going from a local project to a live, production-style deployment

**✅ Outcome:** A production-ready FastAPI backend, containerized and deployed to the cloud.
</details>

---

## 🛠️ Tech Stack

| Layer | Technology |
|:--|:--|
| **Framework** | FastAPI |
| **Language** | Python 3 |
| **Validation** | Pydantic |
| **ORM** | SQLAlchemy, SQLModel |
| **Migrations** | Alembic |
| **Database** | PostgreSQL (hosted on Supabase) |
| **Concurrency** | Async IO (`async` / `await`) |
| **Auth** | OAuth2 Password Flow, JWT, Login with Google (OAuth) |
| **Cache / Token Store / Broker** | Redis |
| **Background Tasks** | Celery |
| **Templates** | Jinja |
| **Email** | Transactional email from FastAPI (verification and password reset) |
| **Real-Time** | WebSockets |
| **Testing** | Pytest |
| **Frontend** | React |
| **Containers** | Docker |
| **Cloud** | AWS |

---

## 💼 Skills Demonstrated

*A quick view for recruiters and hiring managers.*

- ✅ Designing and building **RESTful APIs** with FastAPI
- ✅ **Data validation and serialization** with Pydantic
- ✅ **Relational database design** and SQL, including **one-to-many and many-to-many relationships**
- ✅ **ORM-based persistence** with SQLAlchemy and SQLModel
- ✅ **Database migrations** with Alembic
- ✅ **Asynchronous programming** for high-throughput services
- ✅ Working with **managed PostgreSQL** (Supabase)
- ✅ **Modular architecture** using API Routers
- ✅ **Secure authentication**: password hashing, OAuth2, JWT, and **Login with Google**
- ✅ **Token invalidation** using Redis
- ✅ **Email sending**, **email verification**, and **password reset** flows
- ✅ **Custom response classes** and **Jinja-rendered HTML** from FastAPI
- ✅ **Background task processing** with Celery and Redis
- ✅ **Error handling, middleware, and CORS** configuration
- ✅ **Automated testing** with Pytest, including API and authenticated-route tests
- ✅ **React frontend** integrated with a FastAPI backend
- ✅ **Real-time features** with WebSockets
- ✅ **Containerization** with Docker
- ✅ **Cloud deployment** of a FastAPI backend to AWS
- ✅ Building **real-world features**: delivery partners, product events, and reviews
- ✅ Using **auto-generated OpenAPI documentation** for testing and collaboration

---

## 📂 Repository Structure

Each folder is one module of the course, so you can open the code for the exact lesson you're watching.

| Folder | Part | Covers |
|:--|:-:|:--|
| `m01 Introduction` | 1 | Introduction to APIs and FastAPI |
| `m02 Getting Started` | 1 | Environment setup |
| `m03 Path Params` | 1 | Type hints & path parameters |
| `m04 Query Params` | 1 | Query parameters |
| `m05 CRUD API` | 1 | Build a CRUD API |
| `m06 Pydantic` | 1 | Pydantic for data validation |
| `m07 SQL Database` | 1 | SQL database |
| `m08 SQL Model` | 1 | SQLAlchemy, SQLModel & database integration |
| `m09 AsyncIO` | 1 | Async IO and asynchronous APIs |
| `m10 Postgres` | 1 | PostgreSQL (Supabase) + FastAPI |
| `n11 Authentication` | 1 | Register, login (OAuth2 + JWT), and logout |
| `n12 SQL Relations` | 2 | SQL relationships |
| `n13 Alembic` | 2 | Database migrations |
| `n14 DeliveryPartner` | 2 | Delivery partner feature |
| `n15 Event Product` | 2 | Product event feature |
| `n16 Send Mail` | 2 | Sending email from FastAPI |
| `n17 Response Classes` | 2 | Custom response classes |
| `n18 Email Verification` | 2 | Email verification flow |
| `n19 Reset Password` | 2 | Password reset flow |
| `n20 Review` | 2 | Product review feature |
| `n21 Celery` | 3 | Background tasks with Celery and Redis |
| `n22 Many to Many` | 3 | Many-to-many relationships with SQLModel |
| `n23 Error Handling` | 3 | Error handling |
| `n24 API Middleware` | 3 | Middleware and CORS |
| `n25 API Documentation` | 3 | API documentation |
| `n26 websocket` | 3 | WebSockets |
| `n27 Pytest` | 3 | Pytest fundamentals |
| `n27 API Testing` | 3 | API testing |
| `n28 React` | 3 | React frontend |
| `n29 frontend` | 3 | Frontend (React app and Login with Google) |
| `n30 Deployment` | 3 | Docker and AWS deployment |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Basic Python knowledge (functions, classes, dictionaries)
- A code editor such as VS Code
- For Part 2: familiarity with Part 1 (FastAPI basics, SQLModel, and JWT authentication)
- For Part 3: Parts 1 and 2 completed, since Part 3 continues the same project
- Optional: a free [Supabase](https://supabase.com) account (Part 1, Module 10 onward) and Redis (Part 1, Module 11.2; also used as the Celery broker in Part 3)
- Optional: an email account or SMTP service for testing Part 2's email modules (Send Mail, Email Verification, Password Reset)
- Optional, for Part 3: [Node.js](https://nodejs.org) (React frontend), [Docker](https://www.docker.com/) (containers), a Google Cloud project for OAuth credentials (Login with Google), and an [AWS](https://aws.amazon.com/) account (deployment)

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

# 4. Move into the module you want to run and start the dev server
cd "n12 SQL Relations"
uvicorn app.main:app --reload
```

> 💡 Modules with an `app/` folder are run from inside their module folder. Part 1's earlier modules use `uvicorn main:app --reload`.

### Working with migrations (Part 2, Alembic)

```bash
# Generate a migration after changing your models
alembic revision --autogenerate -m "describe your change"

# Apply all pending migrations
alembic upgrade head
```

### Running tests (Part 3, Pytest)

```bash
# From inside the testing module folder
pytest
```

> 💡 Part 3 modules that need extra services (a Celery worker, the React dev server, or Docker containers) are explained in the matching lesson, so follow the video for the exact commands.

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
6. **Compare with the repo.** If your code differs from the video, check the matching module folder.
7. **Read the written notes.** Every module has a tutorial on [asadullah-ai.vercel.app](https://asadullah-ai.vercel.app/) for quick revision.

---

## 🏁 Course Complete

With Part 3, the **FastAPI Full Course** is finished: you've gone from your first endpoint to a tested, containerized backend with background jobs, a React frontend, and an AWS deployment.

⭐ **Star this repo** if it helped you, and subscribe to the channel for more AI engineering, backend development, and MLOps content.

### 📺 Full Playlist
- **Part 1** (Python basics, SQLModel, Async, Auth, JWT): https://youtu.be/CG4WyImo72s
- **Part 2** (Alembic, relations, email, password reset, Jinja): https://youtu.be/hj81HI2AsG4
- **Part 3** (Celery, Pytest, React, Docker, AWS): https://youtu.be/G3UEDZEVw5g

---

## 👨‍💻 About the Instructor

**Asadullah Shehbaz**
Full Stack AI Engineer & Educator · Ex-Kaggle GM

Subscribe to **Asadullah AI** for practical AI engineering, backend development, and MLOps.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/asadullahai)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AsadullahShehbaz)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/asadullahgenai)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/asad_ullahshehbaz/)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/profile.php?id=61576230402114)

---

<div align="center">

**If this course helped you, give the repo a ⭐ and share it with a friend who is learning backend development.**

`#FastAPI` `#Python` `#BackendDevelopment` `#Docker`

</div>