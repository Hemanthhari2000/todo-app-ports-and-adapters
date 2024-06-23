# Todo Application using the  Ports and Adapters Pattern

## Introduction

This project showcases the implementation of the Ports and Adapters pattern, also known as Hexagonal Architecture, using FastAPI and Alembic.

## About the Project

This application is a simple yet powerful Todo management system that allows users to perform CRUD (Create, Read, Update, Delete) operations on their tasks. Built with Python's FastAPI framework, it leverages SQLite3 for its database and employs Alembic for seamless database migrations. The core business logic is encapsulated in a way that decouples it from external systems, providing a clean, modular, and maintainable codebase.

Key Features
FastAPI Framework: Utilizes FastAPI for building a high-performance, easy-to-use API.
SQLite3 Database: Employs SQLite3 as a lightweight database for storing todo items.
Alembic Migrations: Integrates Alembic to manage database migrations efficiently.
Ports and Adapters Pattern: Demonstrates the Hexagonal Architecture by clearly separating the core business logic from external interfaces and implementations.
Benefits of the Ports and Adapters Pattern
The ports and adapters pattern offers several advantages, including:

- **Decoupled Code**: The core logic is independent of external systems, promoting better code modularity.

- **Enhanced Flexibility**: Adapters can be easily modified or swapped out without affecting the core application.

- **Improved Testability**: The core business logic can be tested in isolation from external dependencies.

- **Scalability**: Facilitates adding new features or integrating with additional systems as the application evolves.

## Getting Started

To get started with this project, and to know more about this pattern, please checkout my [medium article](https://medium.com/@hemanthhari2000/the-ports-and-adapters-pattern-unraveling-the-mystery-2efbf678ab9b) which goes in detail about what is the ports and adapters pattern, why you should consider it, pros and cons of using it and also using it to build this todo application.

