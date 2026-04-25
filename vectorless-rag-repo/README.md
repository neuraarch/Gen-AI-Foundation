# Vectorless RAG System

A Retrieval-Augmented Generation system that converts natural language queries into SQL, retrieves data from a database, enriches it with logs, and generates AI-powered insights.

## Overview

This project implements a Vectorless RAG system using **FastAPI**, **SQLite**, and **OpenAI's LLM**. Instead of traditional vector-based retrieval, it uses direct SQL queries to fetch relevant data and combines it with log information for comprehensive reasoning.

**Architecture Flow:**
```
User Query → LLM (SQL Generation) → SQLite DB → Logs Retrieval → LLM Reasoning → Final Answer
```

## Prerequisites

- Python 3.9 or higher
- pip package manager
- OpenAI API key
- Internet connection (for LLM API calls)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd vectorless-rag
```

### 2. Set OpenAI API Key

**Windows:**
```bash
setx OPENAI_API_KEY "your_api_key_here"
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

> Replace `your_api_key_here` with your actual OpenAI API key. You can get one from [OpenAI Platform](https://platform.openai.com/api-keys).

### 3. Install Dependencies

```bash
pip install fastapi uvicorn openai
```

### 4. Initialize the Database

Run this command **once** to create the SQLite database with sample data:

```bash
python setup_db.py
```

This creates `orders.db` with sample order data for testing.

## Running the Server

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

## Testing the System

### Option 1: Interactive API Documentation (Recommended)

1. Open your browser and navigate to: **http://127.0.0.1:8000/docs**
2. Find the **GET /ask** endpoint
3. Click **"Try it out"**
4. Enter a sample query in the query field:
   ```
   Why are high-value orders delayed in Pune?
   ```
5. Click **Execute**

### Option 2: Using curl

```bash
curl "http://127.0.0.1:8000/ask?query=Why%20are%20high-value%20orders%20delayed%20in%20Pune?"
```

### Example Response

```json
{
  "generated_sql": "SELECT * FROM orders WHERE status='delayed' AND city='Pune' AND amount > 5000;",
  "db_result": [
    {
      "order_id": 1001,
      "amount": 8500,
      "city": "Pune",
      "status": "delayed"
    }
  ],
  "logs": [
    "Order 1001: Delayed due to inventory shortage",
    "Order 1001: Shipped on hold"
  ],
  "final_answer": "High-value orders in Pune are delayed due to inventory shortages and supply chain delays..."
}
```

## System Components

### Core Modules

- **main.py**: FastAPI application entry point with `/ask` endpoint
- **query_rewriter.py**: Converts natural language queries to SQL using LLM
- **db_query.py**: Executes SQL queries against SQLite database
- **search_logs.py**: Retrieves relevant logs for context enrichment
- **reasoning.py**: Generates final answers using LLM reasoning
- **setup_db.py**: Database initialization script
- **db.py**: Database schema and connection handling
- **chat_config.py**: Configuration settings
- **logs.py**: Log management utilities

## Important Notes

📌 **Experimental Project:**
- This is an **experimental RAG system** currently designed for proof-of-concept demonstrations
- The system is optimized for the following query pattern:
  ```
  Why are high-value orders delayed in Pune?
  ```
- While other queries may work, this is the **primary test case** for the current implementation

⚠️ **Security & Constraints:**
- Only **SELECT** queries are executed for safety
- Ensure your `OPENAI_API_KEY` environment variable is properly set before running
- Run `setup_db.py` only **once**
- Do not share your OpenAI API key in public repositories

## Project Structure

```
vectorless-rag/
├── README.md              # This file
├── main.py               # FastAPI application
├── query_rewriter.py     # SQL generation logic
├── db_query.py           # Database query execution
├── search_logs.py        # Log retrieval logic
├── reasoning.py          # Answer generation logic
├── setup_db.py           # Database initialization
├── db.py                 # Database schema & connection
├── chat_config.py        # Configuration
├── logs.py               # Log utilities
└── orders.db             # SQLite database (created after running setup_db.py)
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `OpenAI API key error` | Ensure `OPENAI_API_KEY` is set in environment variables |
| `Database not found error` | Run `python setup_db.py` to initialize the database |
| `Port 8000 already in use` | Run on a different port: `uvicorn main:app --port 8001` |
| `Module not found errors` | Reinstall dependencies: `pip install fastapi uvicorn openai` |

## Future Improvements

- [ ] SQL query guardrails and validation
- [ ] Enhanced log search capabilities
- [ ] Hybrid RAG system (combining vector + SQL approaches)
- [ ] Frontend UI dashboard
- [ ] Query caching for performance
- [ ] Multi-database support
- [ ] Rate limiting and authentication
- [ ] Comprehensive logging and monitoring

## Contributing

Feel free to fork this project, create a feature branch, and submit pull requests.

## License

This project is open-source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Happy querying! 🚀**
