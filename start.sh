#!/bin/bash
# start.sh

# Run the FastAPI app using uvicorn
uvicorn main:app --host 0.0.0.0 --port $PORT
