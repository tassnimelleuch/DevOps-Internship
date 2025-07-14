FROM python:3.10-slim

# Install system dependencies (optional, but often needed for torch/transformers)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /DevOps-Internship

COPY DevOps-Internship/app/requirements.txt app/requirements.txt

RUN pip install --no-cache-dir -r app/requirements.txt

COPY DevOps-Internship/ .

EXPOSE 5000

CMD ["python", "run.py"]