FROM python:3.11-slim
WORKDIR .
COPY ./main.py .
RUN pip install fastapi pydantic uvicorn
EXPOSE 5555
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5555"]