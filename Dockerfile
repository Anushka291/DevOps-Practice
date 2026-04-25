FROM python:3.11

WORKDIR /app

COPY . .

# Create data folder and file with permissions
RUN mkdir -p /app/data \
    && touch /app/data/content.txt \
    && chmod -R 777 /app/data

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "app.py"]