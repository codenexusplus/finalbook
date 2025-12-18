@echo off
REM Script to run Vercel URL ingestion for the RAG chatbot

echo Setting up RAG chatbot with Vercel URL ingestion...
echo Target URL: https://finalbook-ss4z.vercel.app

REM Check if we're in the right directory
if not exist "ingest.py" (
    echo Error: ingest.py not found. Please run this script from the fastapi-rag directory.
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo Creating .env file with default values...
    echo # Cohere API Key - required for embeddings and generation > .env
    echo COHERE_API_KEY="your-cohere-api-key" >> .env
    echo. >> .env
    echo # Qdrant Configuration - required for vector storage >> .env
    echo QDRANT_URL="https://your-qdrant-cloud-url.qdrant.tech:6333" >> .env
    echo QDRANT_API_KEY="your-qdrant-api-key" >> .env
    echo. >> .env
    echo # For Vercel URL ingestion >> .env
    echo VERCEL_URL="https://finalbook-ss4z.vercel.app" >> .env
    echo. >> .env
    echo Please update the .env file with your actual API keys before running ingestion.
    echo Visit https://dashboard.cohere.com/api-keys for COHERE_API_KEY
    echo Visit https://cloud.qdrant.io/ for QDRANT credentials
    pause
    exit /b 1
)

echo Starting ingestion from Vercel URL
echo This may take several minutes depending on the site size...
python ingest.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ^) Ingestion completed successfully!
    echo.
    echo To start the chatbot API server, run:
    echo   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
    echo.
    echo Then visit http://localhost:8000/docs to access the API documentation
) else (
    echo.
    echo ^( Ingestion failed. Please check the error messages above.
    pause
    exit /b 1
)

pause