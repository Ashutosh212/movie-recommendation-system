#!/bin/bash

echo "Starting FastAPI..."
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

sleep 2

echo "Starting Streamlit..."
streamlit run frontend/app.py --server.port 8501
