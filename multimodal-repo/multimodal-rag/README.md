# Multimodal RAG (Retrieval-Augmented Generation)

A multimodal Retrieval-Augmented Generation (RAG) system that processes images, generates captions, creates embeddings, and enables semantic search and question-answering based on visual content.

## Features

- **Image Ingestion**: Automatically processes images from a specified folder, generating descriptive captions.
- **Embedding Generation**: Converts captions into vector embeddings for efficient similarity search.
- **Vector Database**: Uses FAISS for storing and retrieving image embeddings and metadata.
- **Semantic Search**: Performs similarity search based on image captions.
- **LLM Integration**: Generates answers to queries using retrieved image context via OpenAI's GPT models.
- **Modular Design**: Separate modules for ingestion, embedding, search, and answer generation.

## Requirements

- Python 3.7+
- OpenAI API key (for caption generation and LLM answers)
- Dependencies listed in `requirements.txt`

## Installation

1. Clone or download the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key in `config.py` or as an environment variable.

## Usage

### Data Preparation

- Place images to be ingested in the `data/` folder.
- Place query images in the `query/` folder.

### Running the System

Execute the main script to ingest images and perform a sample query:

```bash
python main.py
```

This will:
1. Initialize the FAISS index.
2. Ingest all images in `data/`, generating captions and storing embeddings.
3. Perform a sample query using `query/cartoon.jpg`.

### Custom Query

To query with a different image, modify the `query_with_image` call in `main.py`:

```python
query_with_image("path/to/your/query/image.jpg")
```

## Project Structure

- `config.py`: Configuration settings (e.g., embedding dimensions, API keys).
- `connector.py`: Handles connections to external services (e.g., OpenAI API).
- `embedding.py`: Functions for generating text embeddings.
- `ingestion.py`: Image processing and caption generation.
- `llm_answer.py`: LLM-based answer generation using retrieved context.
- `main.py`: Main script for running the ingestion pipeline and queries.
- `search.py`: Vector similarity search functionality.
- `vector_db.py`: FAISS vector database operations.
- `requirements.txt`: Python dependencies.
- `data/`: Folder for images to be ingested.
- `query/`: Folder for query images.

## How It Works

1. **Ingestion Pipeline**:
   - Images are processed to generate captions using AI models.
   - Captions are converted to vector embeddings.
   - Embeddings and metadata are stored in a FAISS index.

2. **Query Process**:
   - A query image is processed to generate a caption.
   - The caption embedding is used to search for similar images in the vector database.
   - Retrieved results are passed to an LLM to generate a contextual answer.

## Configuration

Edit `config.py` to customize:
- Embedding dimensions
- OpenAI model settings
- API keys

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

[Specify your license here]