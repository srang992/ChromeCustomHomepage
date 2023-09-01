FROM python:3.10.0-slim-bullseye

WORKDIR /MyHomepage

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8500

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8500"]