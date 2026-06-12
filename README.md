# FastAPI RAG Application

A FastAPI-based application with JWT authentication, role-based access control (RBAC), document management, and RAG (Retrieval-Augmented Generation) pipeline with semantic search and reranking.

## Features

- **JWT Authentication** - User registration and login with secure token-based auth
- **Role-Based Access Control (RBAC)** - Admin, Analyst, Auditor, Client roles with different permissions
- **Document Management** - Upload, search, and manage documents with metadata
- **RAG Pipeline** - PDF text extraction, chunking, embeddings, and vector storage
- **Semantic Search** - Cross-encoder reranking for improved search relevance

## Installation

1. Clone or navigate to the project directory:
   ```bash
   cd "C:\Users\suresh vijaya\OneDrive\Desktop\Nimap"
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy `.env` file and update values:
     ```
     SECRET_KEY=your-secret-key-here
     DATABASE_URL=sqlite+aiosqlite:///./app.db
     ```

## Running the Application

Start the server with auto-reload:
```bash
uvicorn main:app --reload
```

The API will be available at:
- **Base URL**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Health Check
| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Check API health status |

### Authentication
| Method | Path | Description |
|--------|------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get JWT token |

### Roles (Admin only)
| Method | Path | Description |
|--------|------|-------------|
| POST | `/roles/create` | Create a new role |
| POST | `/users/assign-role` | Assign a role to a user |
| GET | `/users/{id}/roles` | Get all roles of a user |
| GET | `/users/{id}/permissions` | Get permissions of a user |

### Documents
| Method | Path | Description |
|--------|------|-------------|
| POST | `/documents/upload` | Upload a document (multipart form) |
| GET | `/documents` | Get all documents |
| GET | `/documents/{document_id}` | Get document metadata |
| DELETE | `/documents/{document_id}` | Delete a document |
| GET | `/documents/search` | Search documents by metadata |

### RAG Pipeline
| Method | Path | Description |
|--------|------|-------------|
| POST | `/rag/index-document` | Index a document for semantic search |
| DELETE | `/rag/remove-document/{id}` | Remove document from vector store |
| POST | `/rag/search-document` | Search within a specific document |
| POST | `/rag/search` | Semantic search with reranking (global) |
| GET | `/rag/context/{document_id}` | Get all chunks for a document |

## Testing with Swagger UI

1. Start the server: `uvicorn main:app --reload`
2. Open http://localhost:8000/docs in your browser
3. For protected endpoints:
   - First, register a user via `POST /auth/register`
   - Login via `POST /auth/login` to get a token
   - Click the lock icon and enter: `Bearer <your-token>`

## Role Permissions

| Role | Permissions |
|------|-------------|
| Admin | create, read, update, delete, upload, edit, review, view |
| Analyst | upload, edit, view |
| Auditor | review, view |
| Client | view |

## Project Structure

```
Nimap/
├── main.py              # Application entry point
├── database.py          # Database configuration
├── models.py            # SQLAlchemy models
├── config.py            # Settings and environment
├── dependencies.py      # JWT and auth dependencies
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── auth/                # Authentication module
├── roles/               # Role-based access control
├── documents/           # Document management
└── rag/                 # RAG pipeline and semantic search
```

## Error Handling

| Status Code | Description |
|-------------|-------------|
| 401 | Unauthenticated request (invalid/missing token) |
| 403 | Unauthorized (insufficient role permissions) |
| 404 | Resource not found |
| 422 | Validation error (invalid request body) |
| 500 | Internal server error |
