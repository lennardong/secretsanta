#!/bin/sh
port=${PORT:-8080}
uvicorn "main:app" --proxy-headers --host 0.0.0.0 --port "$port"