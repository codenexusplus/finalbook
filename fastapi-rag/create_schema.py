# fastapi-rag/create_schema.py

import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DATABASE_URL = os.getenv("NEON_DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("NEON_DATABASE_URL environment variable not set. Check your .env file.")

# --- SQL Schema Definition ---
# This table stores the raw text and metadata for each chunk.
# The `id` will serve as the primary key and the vector ID in Qdrant.
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS content_chunks (
    id SERIAL PRIMARY KEY,
    chapter_title VARCHAR(255) NOT NULL,
    source_file VARCHAR(255) NOT NULL,
    chunk_index INTEGER NOT NULL,
    chunk_text TEXT NOT NULL
);
"""

def create_table():
    """Connects to Neon Postgres and creates the content_chunks table."""
    conn = None
    try:
        # 1. Connect to the PostgreSQL database
        print("Connecting to the Neon Serverless Postgres database...")
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # 2. Execute the CREATE TABLE statement
        cur.execute(CREATE_TABLE_SQL)
        
        # 3. Commit the changes
        conn.commit()
        print("✅ Success: 'content_chunks' table created or already exists.")
        
        # 4. (Optional) Verification
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_name='content_chunks';")
        if cur.fetchone():
             print("   Database schema verification complete.")
        else:
             print("   Verification failed: table not found.")

        cur.close()

    except (Exception, psycopg2.Error) as error:
        print(f"❌ Error connecting to PostgreSQL or creating table: {error}")

    finally:
        # 5. Close the connection
        if conn is not None:
            conn.close()
            print("PostgreSQL connection closed.")

if __name__ == "__main__":
    create_table()
