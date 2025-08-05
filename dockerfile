FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /DevOps-Internship

# Install dependencies
COPY app/requirements.txt app/requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

# Copy only necessary files (not tests)
COPY app ./app
COPY run.py .
COPY check_db.py .
COPY README.md .

EXPOSE 5000

CMD ["sh", "-c", "python check_db.py && python run.py"]