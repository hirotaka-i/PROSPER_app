# app/Dockerfile
FROM python:3.9.6

WORKDIR /app

EXPOSE 8080
COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

# COPY appp code and set working directory
COPY app.py app.py
COPY config.yaml config.yaml


# Run the application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

# WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/streamlit/streamlit-example.git .

# RUN pip3 install -r requirements.txt

# EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]



# streamlit run app.py --server.port=8080 --server.address=0.0.0.0
# streamlit run app.py --server.port=8501 --server.address=0.0.0.0