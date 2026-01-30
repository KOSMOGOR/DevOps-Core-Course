FROM python:3.14-slim
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -r python && useradd --no-log-init -r -g python python
USER python:python

ENV HOST=0.0.0.0
ENV PORT=8000
EXPOSE 8000

ENTRYPOINT ["python", "app.py"]