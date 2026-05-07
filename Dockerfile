FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader punkt_tab

COPY . .

EXPOSE 10000

CMD streamlit run streamlit_app.py --server.port 10000 --server.address 0.0.0.0