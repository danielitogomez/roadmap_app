FROM python:3.8-slim

WORKDIR .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME RoadmapApp

CMD ["python", "app.py"]