@echo off
cd /d "C:\Users\batool1\Desktop\book-spec - Copy - Copy\fastapi-rag"

echo Starting the FastAPI RAG server...
echo Make sure your .env file has the correct API keys before running!

python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload