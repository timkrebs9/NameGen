#!/bin/bash
# Start the FastAPI application using Uvicorn from the app/backend directory

cd app/backend
python -m uvicorn main:app --host 0.0.0.0
